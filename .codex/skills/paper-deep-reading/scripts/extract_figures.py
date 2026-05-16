#!/usr/bin/env python3
"""Extract embedded PDF images or render selected pages for paper notes.

This helper intentionally stays small. It relies on PyMuPDF (`fitz`) when
available and writes all outputs to a paper-local figures directory.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

try:
    import fitz
except ImportError as exc:
    raise SystemExit("PyMuPDF is required. Install it with: pip install pymupdf") from exc


def parse_pages(spec: str | None, page_count: int) -> list[int]:
    if not spec:
        return list(range(page_count))

    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_text, end_text = part.split("-", 1)
            start = int(start_text)
            end = int(end_text)
            pages.update(range(start - 1, end))
        else:
            pages.add(int(part) - 1)

    return sorted(page for page in pages if 0 <= page < page_count)


def image_ext(image_info: tuple) -> str:
    ext = image_info[7] if len(image_info) > 7 else "png"
    return ext if ext else "png"


def extract_embedded_images(doc, out_dir: Path, min_width: int, min_height: int) -> int:
    saved = 0
    for page_index in range(len(doc)):
        page = doc[page_index]
        for image_index, image_info in enumerate(page.get_images(full=True), start=1):
            xref = image_info[0]
            width = image_info[2]
            height = image_info[3]
            if width < min_width or height < min_height:
                continue

            image = doc.extract_image(xref)
            ext = image.get("ext") or image_ext(image_info)
            filename = out_dir / f"page{page_index + 1:03d}_img{image_index:02d}.{ext}"
            filename.write_bytes(image["image"])
            saved += 1
    return saved


def render_pages(doc, pages: Iterable[int], out_dir: Path, dpi: int) -> int:
    saved = 0
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)

    for page_index in pages:
        page = doc[page_index]
        pixmap = page.get_pixmap(matrix=matrix, alpha=False)
        filename = out_dir / f"page{page_index + 1:03d}.png"
        pixmap.save(filename)
        saved += 1
    return saved


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract embedded PDF images and optionally render PDF pages."
    )
    parser.add_argument("pdf", type=Path, help="Path to paper PDF")
    parser.add_argument("--out", type=Path, default=Path("figures"), help="Output directory")
    parser.add_argument("--min-width", type=int, default=160, help="Minimum embedded image width")
    parser.add_argument("--min-height", type=int, default=160, help="Minimum embedded image height")
    parser.add_argument(
        "--render-pages",
        help="Optional 1-based pages to render, for example '1,3,5-7'.",
    )
    parser.add_argument("--dpi", type=int, default=180, help="DPI for rendered pages")
    args = parser.parse_args()

    if not args.pdf.exists():
        raise SystemExit(f"PDF not found: {args.pdf}")

    args.out.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(args.pdf)
    embedded_count = extract_embedded_images(
        doc,
        args.out,
        min_width=args.min_width,
        min_height=args.min_height,
    )
    rendered_count = 0
    if args.render_pages:
        pages = parse_pages(args.render_pages, len(doc))
        rendered_count = render_pages(doc, pages, args.out, args.dpi)

    print(f"Saved {embedded_count} embedded images and {rendered_count} rendered pages to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
