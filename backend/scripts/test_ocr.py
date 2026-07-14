"""
Standalone manual test script for the OCR service.
Run this directly — it is NOT part of the FastAPI app.

Usage:
    python scripts/test_ocr.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.services.ocr_service import (
    extract_text_from_pdf,
    extract_text_from_image,
    extract_text_from_scanned_pdf,
)

SAMPLES_DIR = Path(__file__).resolve().parent.parent / "storage" / "samples"


def main():
    digital_pdf = SAMPLES_DIR / "digital_sample.pdf"
    loose_image = SAMPLES_DIR / "scanned_sample.jpg"
    scanned_pdf = SAMPLES_DIR / "scanned_sample.pdf"

    print("=" * 60)
    print("Testing PyMuPDF extraction (digital PDF)")
    print("=" * 60)
    if digital_pdf.exists():
        print(extract_text_from_pdf(str(digital_pdf)) or "(empty — no text layer)")
    else:
        print(f"Sample file not found: {digital_pdf}")

    print()
    print("=" * 60)
    print("Testing EasyOCR extraction (loose image file)")
    print("=" * 60)
    if loose_image.exists():
        print(extract_text_from_image(str(loose_image)) or "(empty — no text found)")
    else:
        print(f"Sample file not found: {loose_image}")

    print()
    print("=" * 60)
    print("Testing scanned PDF pipeline (pdf2image + EasyOCR)")
    print("=" * 60)
    if scanned_pdf.exists():
        print(extract_text_from_scanned_pdf(str(scanned_pdf)) or "(empty — no text found)")
    else:
        print(f"Sample file not found: {scanned_pdf}")


if __name__ == "__main__":
    main()