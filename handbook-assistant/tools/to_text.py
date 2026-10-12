"""Turn a source of almost any format into a text file for sources/, with the standard header.

Usage:
    python tools/to_text.py <file or URL> --id S012 --chosen-by developer [--title "..."] [--pages 3-12]

Handles: web pages (HTML), PDF (text layer), Word (.docx), PowerPoint (.pptx), Excel (.xlsx),
CSV/TSV, plain text and Markdown, JSON, and subtitle or transcript files (.vtt, .srt).
Refuses audio and video files and anything that looks like interview material: those never enter
the project. Images and scanned PDFs have no text layer; the script says so and stops.
Needs: Python 3.9+, and `pypdf` for PDFs (pip install -r requirements.txt).
"""
import argparse
import csv
import datetime
import io
import json
import os
import re
import sys
import urllib.request
import zipfile
from html.parser import HTMLParser
from xml.etree import ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_VIDEO = {".mp3", ".mp4", ".m4a", ".wav", ".mov", ".webm", ".ogg", ".aac", ".flac", ".avi", ".mkv", ".wma", ".amr"}
IMAGES = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff", ".webp", ".heic"}
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
S = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"


def stop(message):
    print("STOPPED:", message)
    sys.exit(2)


# ---------- readers: each returns (title, text, what_was_read) ----------

class _HTML(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "nav", "footer", "form"}
    BREAK = {"p", "br", "li", "h1", "h2", "h3", "h4", "h5", "tr", "div", "td", "th", "section", "article", "caption"}

    def __init__(self):
        super().__init__()
        self.out, self.skip, self.title, self._in_title = [], 0, "", False

    def handle_starttag(self, tag, attrs):
        self.skip += tag in self.SKIP
        self._in_title = tag == "title"
        if tag in self.BREAK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        if tag == "title":
            self._in_title = False
        if tag in self.BREAK:
            self.out.append("\n")

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        elif not self.skip:
            self.out.append(data)


def read_html(raw):
    p = _HTML()
    p.feed(raw)
    lines = [re.sub(r"[ \t\xa0]+", " ", l).strip() for l in "".join(p.out).split("\n")]
    return p.title.strip(), "\n".join(l for l in lines if l), "whole page (visible text)"


def page_range(spec, n):
    if not spec:
        return list(range(n))
    a, _, b = spec.partition("-")
    return list(range(int(a) - 1, min(int(b or a), n)))


def read_pdf(data, pages=None):
    try:
        from pypdf import PdfReader
    except ImportError:
        stop("PDF support needs pypdf: run  python -m pip install -r requirements.txt")
    reader = PdfReader(io.BytesIO(data))
    n = len(reader.pages)
    chosen = page_range(pages, n)
    parts = [f"[page {i + 1}]\n{(reader.pages[i].extract_text() or '').strip()}" for i in chosen]
    text = "\n\n".join(parts)
    if len(re.sub(r"\[page \d+\]|\s", "", text)) < 50 * max(1, len(chosen)) // 10:
        stop("this PDF has (almost) no text layer: it is probably scanned. It needs OCR, or a team member types the passages by hand.")
    title = ((reader.metadata or {}).get("/Title") or "").strip() if reader.metadata else ""
    read = f"pages {chosen[0] + 1}–{chosen[-1] + 1} of {n}" if pages else f"all {n} pages (text layer)"
    return title, text, read


def read_docx(data):
    z = zipfile.ZipFile(io.BytesIO(data))
    root = ET.fromstring(z.read("word/document.xml"))
    paras = ["".join(t.text or "" for t in p.iter(W + "t")) for p in root.iter(W + "p")]
    title = ""
    if "docProps/core.xml" in z.namelist():
        m = re.search(r"<dc:title>(.*?)</dc:title>", z.read("docProps/core.xml").decode("utf-8", "replace"))
        title = m.group(1) if m else ""
    return title, "\n".join(p for p in paras if p.strip()), "whole document"


def read_pptx(data):
    z = zipfile.ZipFile(io.BytesIO(data))
    slides = sorted((n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)), key=lambda n: int(re.findall(r"\d+", n)[-1]))
    parts = []
    for i, name in enumerate(slides, 1):
        root = ET.fromstring(z.read(name))
        lines = ["".join(t.text or "" for t in p.iter(A + "t")) for p in root.iter(A + "p")]
        parts.append(f"[slide {i}]\n" + "\n".join(l for l in lines if l.strip()))
    return "", "\n\n".join(parts), f"all {len(slides)} slides (text only)"


def read_xlsx(data):
    z = zipfile.ZipFile(io.BytesIO(data))
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(S + "si"):
            shared.append("".join(t.text or "" for t in si.iter(S + "t")))
    sheets = sorted(n for n in z.namelist() if re.match(r"xl/worksheets/sheet\d+\.xml$", n))
    parts = []
    for i, name in enumerate(sheets, 1):
        rows = []
        for row in ET.fromstring(z.read(name)).iter(S + "row"):
            cells = []
            for c in row.iter(S + "c"):
                v, t = c.find(S + "v"), c.get("t")
                if t == "s" and v is not None:
                    cells.append(shared[int(v.text)])
                elif t == "inlineStr":
                    cells.append("".join(x.text or "" for x in c.iter(S + "t")))
                else:
                    cells.append(v.text if v is not None else "")
            rows.append("\t".join(cells))
        parts.append(f"[sheet {i}]\n" + "\n".join(rows))
    return "", "\n\n".join(parts), f"all {len(sheets)} sheets (cell values, tab-separated)"


def read_subtitles(raw):
    lines = []
    for line in raw.splitlines():
        line = line.strip()
        if not line or line == "WEBVTT" or line.isdigit() or "-->" in line or line.startswith(("NOTE", "Kind:", "Language:")):
            continue
        line = re.sub(r"<[^>]+>", "", line)
        if not lines or lines[-1] != line:
            lines.append(line)
    return "", " ".join(lines), "full transcript (timestamps removed)"


def read_csv_text(raw, delimiter):
    rows = list(csv.reader(io.StringIO(raw), delimiter=delimiter))
    return "", "\n".join("\t".join(r) for r in rows), f"all {len(rows)} rows"


def convert(name, data, pages):
    ext = os.path.splitext(name.split("?")[0].lower())[1]
    head = data[:5]
    if ext == ".pdf" or head.startswith(b"%PDF"):
        return "PDF", read_pdf(data, pages)
    if ext == ".docx":
        return "Word document", read_docx(data)
    if ext == ".pptx":
        return "PowerPoint slides", read_pptx(data)
    if ext == ".xlsx":
        return "Excel workbook", read_xlsx(data)
    raw = data.decode("utf-8-sig", "replace")
    if ext in {".vtt", ".srt"}:
        return "video transcript (subtitle file)", read_subtitles(raw)
    if ext in {".csv", ".tsv"}:
        return "table (CSV)", read_csv_text(raw, "\t" if ext == ".tsv" else ",")
    if ext == ".json":
        return "JSON data", ("", json.dumps(json.loads(raw), indent=2, ensure_ascii=False), "whole file")
    if ext in {".txt", ".md"}:
        return "text", ("", raw.strip(), "whole file")
    if ext in {".html", ".htm", ""} or "<html" in raw[:2000].lower():
        return "web page", read_html(raw)
    stop(f"unsupported format '{ext}'. Supported: web pages, .pdf, .docx, .pptx, .xlsx, .csv, .tsv, .txt, .md, .json, .vtt, .srt")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="a file path or an http(s) address")
    ap.add_argument("--id", required=True, help="next free source ID, e.g. S012")
    ap.add_argument("--chosen-by", required=True, help="the team member's role")
    ap.add_argument("--title", default="", help="title, if the file does not carry one")
    ap.add_argument("--pages", default="", help="PDF page range, e.g. 3-12")
    ap.add_argument("--short-name", default="", help="short name for the file, e.g. oecd-d4sme-2026")
    args = ap.parse_args()
    src = args.source

    if re.search(r"interview|protected|opname|transcript[-_ ]?interview", src, re.I):
        stop("this path looks like interview or protected material. It never enters the project.")
    ext = os.path.splitext(src.split("?")[0].lower())[1]
    if ext in AUDIO_VIDEO:
        stop("audio and video files are not taken in (interview recordings must never enter). For a published video, use its transcript: a .vtt/.srt subtitle file or the transcript text.")
    if ext in IMAGES:
        stop("images have no text layer. The assistant can read an image itself and type out what it shows, marked 'machine-transcribed, check before quoting'.")
    if not re.fullmatch(r"S\d{3}", args.id):
        stop("--id must look like S012")
    if any(f.startswith(args.id + "-") for f in os.listdir(os.path.join(ROOT, "sources"))):
        stop(f"{args.id} is already used in sources/. Source IDs are never reused.")

    if src.startswith(("http://", "https://")):
        req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
        try:
            data = urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:  # blocked sites and certificate problems: download by other means first
            stop(f"could not download ({e}). Download the file with  curl -L -o <file> \"{src}\"  and run this script on the file.")
        address = src
    else:
        if not os.path.exists(src):
            stop(f"file not found: {src}")
        data = open(src, "rb").read()
        address = f"local file: {os.path.basename(src)}"

    fmt, (title, text, read) = convert(src, data, args.pages or None)
    title = args.title or title or os.path.basename(src.split("?")[0])
    short = args.short_name or re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:50] or "source"
    out = os.path.join(ROOT, "sources", f"{args.id}-{short}.md")
    header = (
        f"# {args.id} · {title}\n"
        f"- **Address:** {address}\n"
        f"- **Accessed:** {datetime.date.today():%d %b %Y}\n"
        f"- **Format:** {fmt}\n"
        f"- **What was read:** {read}\n"
        f"- **Chosen by:** {args.chosen_by}\n"
        f"- **Converted by:** tools/to_text.py (text extracted unchanged; tables and layout may be lost)\n\n---\n\n"
    )
    with open(out, "w", encoding="utf-8") as f:
        f.write(header + text + "\n")
    words = len(text.split())
    print(f"SAVED {os.path.relpath(out, ROOT)} · {fmt} · {read} · {words} words")
    if words < 80:
        print("WARNING: very little text came out. Check the file before appraising it.")


if __name__ == "__main__":
    main()
