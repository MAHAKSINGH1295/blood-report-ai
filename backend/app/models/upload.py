from pydantic import BaseModel


class UploadResponse(BaseModel):
    file_id: str
    original_filename: str
    stored_filename: str
    content_type: str
    size_bytes: int
    status: str