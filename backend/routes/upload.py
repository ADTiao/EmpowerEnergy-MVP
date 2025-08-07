from fastapi import APIRouter, File, UploadFile, HTTPException
from backend.services import parse_prop
from fastapi.responses import JSONResponse
from backend.info import info
import tempfile

import os


router = APIRouter()

@router.post("/upload_file")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(400, "Incorrect submission type: PDF required")
    
    suffix = os.path.splitext(file.filename)[1] or ".pdf"
    with tempfile.NamedTemporaryFile("wb", suffix=suffix, delete=False) as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp.flush()
        tmp_path = tmp.name
    
    # 3. call your async LLM extractor
    try:
        proposal_data = await parse_prop.api_call(tmp_path)
        # store in shared info (or whatever you use downstream)
        info["proposal"] = proposal_data
    finally:
        # clean up temp file
        try:
            os.remove(tmp_path)
        except OSError:
            pass

    # 4. echo back the structured JSON
    return JSONResponse(content=proposal_data)




