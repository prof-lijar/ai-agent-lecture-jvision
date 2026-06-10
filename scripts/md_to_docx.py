#!/usr/bin/env python3
"""
강의계획서.md → 강의계획서.docx 변환 스크립트.

사전 요구: pandoc 설치 (`brew install pandoc` 또는 https://pandoc.org/installing.html).

사용법:
    python scripts/md_to_docx.py
    python scripts/md_to_docx.py --reference docx_reference.docx
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="강의계획서 Markdown → docx 변환")
    parser.add_argument(
        "--input",
        default="강의계획서.md",
        help="입력 마크다운 파일 (기본: 강의계획서.md)",
    )
    parser.add_argument(
        "--output",
        default="강의계획서.docx",
        help="출력 docx 파일 (기본: 강의계획서.docx)",
    )
    parser.add_argument(
        "--reference",
        default=None,
        help="docx 스타일 참조 파일 (선택). 학교 양식에 맞추려면 빈 docx를 만들어 폰트/여백 설정 후 지정.",
    )
    parser.add_argument(
        "--toc",
        action="store_true",
        help="목차 자동 생성",
    )
    args = parser.parse_args()

    if shutil.which("pandoc") is None:
        print("ERROR: pandoc이 설치되어 있지 않습니다.", file=sys.stderr)
        print("  macOS:  brew install pandoc", file=sys.stderr)
        print("  Ubuntu: sudo apt-get install pandoc", file=sys.stderr)
        print("  Windows: https://pandoc.org/installing.html", file=sys.stderr)
        return 1

    project_root = Path(__file__).resolve().parent.parent
    input_path = (project_root / args.input).resolve()
    output_path = (project_root / args.output).resolve()

    if not input_path.exists():
        print(f"ERROR: 입력 파일이 없습니다: {input_path}", file=sys.stderr)
        return 1

    cmd = [
        "pandoc",
        str(input_path),
        "-o",
        str(output_path),
        "--from",
        "gfm+yaml_metadata_block",
        "--to",
        "docx",
        "--standalone",
    ]
    if args.toc:
        cmd.extend(["--toc", "--toc-depth=2"])
    if args.reference:
        ref_path = (project_root / args.reference).resolve()
        if not ref_path.exists():
            print(f"ERROR: 참조 docx가 없습니다: {ref_path}", file=sys.stderr)
            return 1
        cmd.extend(["--reference-doc", str(ref_path)])

    print(f"실행: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("ERROR: pandoc 변환 실패", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        return result.returncode

    print(f"OK: {output_path} 생성됨 ({output_path.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
