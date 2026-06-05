from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    HTTPException
)
import os
import uuid

from services.url_extractor import (
    extract_text_from_url
)

from services.image_extractor import (
    extract_text_from_image
)

from services.pdf_extractor import (
    extract_text_from_pdf
)

from services.chunking import (
    create_chunks
)

from services.pinecone_db import (
    store_vectors
)

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

@router.post("/load/url")
async def load_url(url: str):

    try:

        text = extract_text_from_url(url)

        chunks = create_chunks(text)

        store_vectors(
            chunks=chunks,
            source_type="url",
            source_name=url
        )

        return {
            "status": "success",
            "source_type": "url",
            "chunks": len(chunks)
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@router.post("/load")
async def load_file(
    source_type: str = Form(...),
    file: UploadFile = File(...)
):

    try:

        filename = (
            f"{uuid.uuid4()}_{file.filename}"
        )

        filepath = os.path.join(
            UPLOAD_DIR,
            filename
        )

        with open(filepath, "wb") as f:
            f.write(
                await file.read()
            )

        text = ""

        if source_type == "image":

            text = extract_text_from_image(
                filepath
            )

        elif source_type == "file":

            text = extract_text_from_pdf(
                filepath
            )

        else:

            raise HTTPException(
                status_code=400,
                detail="Invalid source type"
            )

        chunks = create_chunks(text)

        store_vectors(
            chunks=chunks,
            source_type=source_type,
            source_name=file.filename
        )

        return {
            "status": "success",
            "source_type": source_type,
            "chunks": len(chunks)
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )