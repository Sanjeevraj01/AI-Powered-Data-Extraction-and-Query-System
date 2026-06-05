from fastapi import APIRouter

from models.schemas import QueryRequest

from services.pinecone_db import (
    search_vectors
)

from services.llm_service import (
    generate_answer
)

router = APIRouter()

@router.post("/query")
def query_data(data: QueryRequest):

    results = search_vectors(
        data.query
    )

    context = "\n".join(
        [
            match["metadata"]["text"]
            for match in results["matches"]
        ]
    )

    answer = generate_answer(
        data.query,
        context
    )

    return {
        "answer": answer
    }