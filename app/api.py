from fastapi import APIRouter, Request
from app.chunker import get_chunked_response
from app.logger import log_to_google_sheets

router = APIRouter()

@router.post("/get-info")
async def get_info(request: Request):
    body = await request.json()
    query = body.get("query")
    session_id = body.get("session_id", "default_session")

    response = get_chunked_response(query, session_id)
    log_to_google_sheets(session_id, query, response)

    return {"response": response}