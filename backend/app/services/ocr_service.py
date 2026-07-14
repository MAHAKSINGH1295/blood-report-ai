from pathlib import Path

import fitz  # PyMuPDF
import easyocr
from pdf2image import convert_from_path

from app.core.config import POPPLER_PATH, OCR_DPI

_reader: easyocr.Reader | None = None


def get_reader() -> easyocr.Reader:
    """Lazily create and cache the EasyOCR reader instance."""
    global _reader
    if _reader is None:
        _reader = easyocr.Reader(["en"], gpu=False)
    return _reader


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text directly from a digital PDF's text layer using PyMuPDF.
    Returns an empty string if the PDF has no extractable text
    (which usually means it's a scanned/image-only PDF).
    """
    text_chunks = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text_chunks.append(page.get_text())
    return "\n".join(text_chunks).strip()


def extract_text_from_image(image_path: str) -> str:
    """
    Extract text from a standalone image (e.g. a scanned or
    photographed report page) using EasyOCR's neural network.
    """
    reader = get_reader()
    results = reader.readtext(image_path, detail=0)
    return "\n".join(results).strip()


def convert_pdf_to_images(pdf_path: str) -> list:
    """
    Rasterize every page of a PDF into a list of PIL.Image objects,
    so scanned PDF pages (which have no text layer) can be fed
    into EasyOCR one page at a time.
    """
    images = convert_from_path(
        pdf_path,
        dpi=OCR_DPI,
        poppler_path=POPPLER_PATH,
    )
    return images


def extract_text_from_scanned_pdf(pdf_path: str) -> str:
    """
    Full pipeline for a scanned/image-only PDF:
    1. Rasterize each page into an image.
    2. Run EasyOCR on each page image.
    3. Join all pages' text together, in page order.
    """
    reader = get_reader()
    images = convert_pdf_to_images(pdf_path)

    page_texts = []
    for page_number, image in enumerate(images, start=1):
        results = reader.readtext(image, detail=0)
        page_text = "\n".join(results).strip()
        page_texts.append(f"--- Page {page_number} ---\n{page_text}")

    return "\n\n".join(page_texts).strip()