import pinecone

from config.settings import (
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME
)

from services.embeddings import (
    generate_document_embeddings,
    generate_query_embedding
)

pc = pinecone.Pinecone(
    api_key=PINECONE_API_KEY
)   

index = pc.Index(
    PINECONE_INDEX_NAME
)



def store_vectors(
    chunks,
    source_type,
    source_name
):

    vectors = []

    embeddings = generate_document_embeddings(
        chunks
    )

    for idx, (chunk, embedding) in enumerate(
        zip(chunks, embeddings)
    ):

        vectors.append(
            {
                "id": f"{source_type}_{source_name}_{idx}",

                "values": embedding,

                "metadata": {
                    "source_type": source_type,
                    "source_name": source_name,
                    "chunk_id": idx,
                    "text": chunk
                }
            }
        )

    index.upsert(
        vectors=vectors
    )

#similarity

def search_vectors(
    query,
    top_k=5
):

    query_embedding = generate_query_embedding(
        query
    )

    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )

    return results