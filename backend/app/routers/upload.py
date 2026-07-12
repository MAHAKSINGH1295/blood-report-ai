import uuid
from pathlib import Path

from fastapi import APIRouter, UploadFile, File

from app.core.config import UPLOAD_DIR
from app.core.validators import validate_file_type, validate_file_size
from app.models.upload import UploadResponse

router = APIRouter(prefix="/upload", tags=["upload"])


@router.post("", response_model=UploadResponse)
async def upload_report(file: UploadFile = File(...)) -> UploadResponse:
    validate_file_type(file)

    file_bytes = await file.read()
    validate_file_size(file_bytes)

    file_id = str(uuid.uuid4())
    extension = Path(file.filename).suffix
    stored_filename = f"{file_id}{extension}"
    destination = UPLOAD_DIR / stored_filename

    with open(destination, "wb") as out_file:
        out_file.write(file_bytes)

    return UploadResponse(
        file_id=file_id,
        original_filename=file.filename,
        stored_filename=stored_filename,
        content_type=file.content_type,
        size_bytes=len(file_bytes),
        status="uploaded",
    )