"""
Standalone manual test script for the OCR service.
Run this directly — it is NOT part of the FastAPI app.

Usage:
    python scripts/test_ocr.py
"""

import sys
from pathlib import Path

# Make sure "app" is importable when running this script directly
# from the backend/ folder.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.services.ocr_service import extract_text_from_pdf, extract_text_from_image

SAMPLES_DIR = Path(__file__).resolve().parent.parent / "storage" / "samples"


def main():
    pdf_path = SAMPLES_DIR / "digital_sample.pdf"
    image_path = SAMPLES_DIR / "scanned_sample.jpg"

    print("=" * 60)
    print("Testing PyMuPDF extraction (digital PDF)")
    print("=" * 60)
    if pdf_path.exists():
        text = extract_text_from_pdf(str(pdf_path))
        print(text if text else "(empty — this PDF may have no text layer)")
    else:
        print(f"Sample file not found: {pdf_path}")

    print()
    print("=" * 60)
    print("Testing EasyOCR extraction (image)")
    print("=" * 60)
    if image_path.exists():
        text = extract_text_from_image(str(image_path))
        print(text if text else "(empty — EasyOCR found no readable text)")
    else:
        print(f"Sample file not found: {image_path}")


if __name__ == "__main__":
    main()