#!/usr/bin/env python3
"""
강의계획서.md → 강의계획서.pdf 변환 스크립트.

전략: pandoc으로 한국어 친화 CSS가 적용된 HTML을 만들고, 헤드리스 Chrome으로 PDF 인쇄.
- 추가 PDF 엔진 설치 불필요 (xelatex, weasyprint, typst 모두 안 써도 됨)
- macOS 내장 Apple SD Gothic Neo로 한글 렌더링
- 표·코드블럭·헤더 모두 깔끔하게 유지

사전 요구:
  - pandoc (brew install pandoc)
  - Google Chrome (이미 macOS에 설치되어 있다고 가정)

사용법:
  python scripts/md_to_pdf.py
  python scripts/md_to_pdf.py --input materials/concepts-glossary.md --output 용어집.pdf
"""

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]

CSS = """
@page {
  size: A4;
  margin: 18mm 16mm 18mm 16mm;
}
html { font-size: 11pt; }
body {
  font-family: "Apple SD Gothic Neo", "Noto Sans CJK KR", "Malgun Gothic", -apple-system, sans-serif;
  line-height: 1.55;
  color: #1a1a1a;
  max-width: 100%;
}
h1, h2, h3, h4 {
  font-weight: 700;
  page-break-after: avoid;
}
h1 { font-size: 22pt; border-bottom: 2px solid #333; padding-bottom: 6pt; margin-top: 18pt; }
h2 { font-size: 16pt; border-bottom: 1px solid #999; padding-bottom: 4pt; margin-top: 16pt; }
h3 { font-size: 13pt; margin-top: 12pt; }
h4 { font-size: 11pt; margin-top: 10pt; }
p, li { font-size: 10.5pt; }
table {
  border-collapse: collapse;
  width: 100%;
  margin: 8pt 0 12pt 0;
  font-size: 9.5pt;
  page-break-inside: avoid;
}
th, td {
  border: 1px solid #bbb;
  padding: 5pt 7pt;
  vertical-align: top;
  text-align: left;
}
th { background: #f1f3f5; font-weight: 600; }
tr:nth-child(even) td { background: #fafbfc; }
code {
  font-family: "JetBrains Mono", "Menlo", monospace;
  background: #f4f6f8;
  padding: 1pt 4pt;
  border-radius: 3pt;
  font-size: 9.5pt;
}
pre {
  background: #f4f6f8;
  border: 1px solid #e0e3e7;
  border-radius: 4pt;
  padding: 8pt 10pt;
  overflow-x: auto;
  page-break-inside: avoid;
  font-size: 9pt;
}
pre code { background: transparent; padding: 0; }
blockquote {
  border-left: 3px solid #888;
  padding: 4pt 12pt;
  color: #444;
  background: #fafafa;
  margin: 8pt 0;
}
hr { border: 0; border-top: 1px solid #ccc; margin: 16pt 0; }
a { color: #0b62d6; text-decoration: none; }
ul, ol { padding-left: 22pt; }
li { margin: 2pt 0; }
strong { font-weight: 700; }
.title-block-header { text-align: center; margin-bottom: 24pt; }
.title-block-header h1.title { border: 0; font-size: 26pt; margin-bottom: 4pt; }
.title-block-header p.subtitle { font-size: 14pt; color: #555; margin: 2pt 0; }
.title-block-header p.author, .title-block-header p.date {
  font-size: 11pt; color: #666; margin: 0;
}
#TOC { page-break-after: always; }
#TOC > ul { list-style: none; padding-left: 0; }
"""


def find_chrome() -> str | None:
    for p in CHROME_PATHS:
        if Path(p).exists():
            return p
    return shutil.which("chromium") or shutil.which("google-chrome")


def main() -> int:
    parser = argparse.ArgumentParser(description="Markdown → PDF (헤드리스 Chrome 경유)")
    parser.add_argument("--input", default="강의계획서.md", help="입력 마크다운 파일")
    parser.add_argument("--output", default="강의계획서.pdf", help="출력 PDF 파일")
    parser.add_argument("--toc", action="store_true", default=True, help="목차 자동 생성 (기본 켜짐)")
    parser.add_argument("--no-toc", dest="toc", action="store_false", help="목차 비활성화")
    parser.add_argument("--keep-html", action="store_true", help="중간 HTML 파일 유지 (디버깅용)")
    args = parser.parse_args()

    if shutil.which("pandoc") is None:
        print("ERROR: pandoc이 필요합니다. brew install pandoc", file=sys.stderr)
        return 1

    chrome = find_chrome()
    if chrome is None:
        print("ERROR: Google Chrome / Chromium이 필요합니다.", file=sys.stderr)
        print("  https://www.google.com/chrome/", file=sys.stderr)
        return 1

    project_root = Path(__file__).resolve().parent.parent
    input_path = (project_root / args.input).resolve()
    output_path = (project_root / args.output).resolve()

    if not input_path.exists():
        print(f"ERROR: 입력 파일 없음: {input_path}", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory(prefix="md2pdf_") as tmpdir:
        tmpdir_path = Path(tmpdir)
        css_path = tmpdir_path / "style.css"
        css_path.write_text(CSS, encoding="utf-8")

        if args.keep_html:
            html_path = project_root / (input_path.stem + ".html")
        else:
            html_path = tmpdir_path / "doc.html"

        # 1. pandoc: md → 자립형 HTML (CSS 임베드)
        pandoc_cmd = [
            "pandoc",
            str(input_path),
            "-o", str(html_path),
            "--from", "gfm+yaml_metadata_block",
            "--to", "html5",
            "--standalone",
            "--embed-resources",
            "--css", str(css_path),
        ]
        if args.toc:
            pandoc_cmd.extend(["--toc", "--toc-depth=2"])

        print(f"[1/2] pandoc: md → html")
        r = subprocess.run(pandoc_cmd, capture_output=True, text=True)
        if r.returncode != 0:
            print("ERROR: pandoc 실패", file=sys.stderr)
            print(r.stderr, file=sys.stderr)
            return r.returncode

        # 2. Chrome 헤드리스: html → pdf
        # --no-pdf-header-footer로 페이지 머리/꼬리 제거 (URL, 날짜 등)
        chrome_cmd = [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--hide-scrollbars",
            "--no-pdf-header-footer",
            f"--print-to-pdf={output_path}",
            html_path.resolve().as_uri(),
        ]
        print(f"[2/2] Chrome: html → pdf")
        r = subprocess.run(chrome_cmd, capture_output=True, text=True)
        if r.returncode != 0:
            print("ERROR: Chrome PDF 인쇄 실패", file=sys.stderr)
            print(r.stderr, file=sys.stderr)
            return r.returncode

        if not output_path.exists():
            print("ERROR: PDF가 생성되지 않았습니다.", file=sys.stderr)
            return 1

    print(f"OK: {output_path} 생성됨 ({output_path.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
