from app.utils import count_tokens
from app.router import get_relevant_section

MAX_TOKENS = 800

def get_chunked_response(query, session_id):
    section = get_relevant_section(query)
    chunks = []
    current_chunk = ""

    for paragraph in section.split("\n"):
        if count_tokens(current_chunk + paragraph) < MAX_TOKENS:
            current_chunk += paragraph + "\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = paragraph + "\n"
    if current_chunk:
        chunks.append(current_chunk.strip())

    # Return the first chunk (can be extended later with context)
    return chunks[0]