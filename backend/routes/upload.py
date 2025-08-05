from fastapi import APIRouter, File, UploadFile
from backend.services import parse_prop
from fastapi.responses import JSONResponse
from backend.info import info

router = APIRouter()

@router.post("/upload_file")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return JSONResponse(content="Incorrect submission type", status_code=400)
    contents = await file.read()
    response = await parse_prop.api_call(contents)
    info["proposal"] = response
    return JSONResponse(content="file successfully uploaded", status_code=200)


