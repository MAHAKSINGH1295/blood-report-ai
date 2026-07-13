import fitz  # PyMuPDF
import easyocr

# Module-level singleton. Loaded once, the first time it's actually
# needed, and reused for every call afterward — loading this repeatedly
# would be extremely slow and wasteful.
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