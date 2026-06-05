import pinecone
from config.settings import PINECONE_API_KEY

pc = pinecone.Pinecone(
    api_key=PINECONE_API_KEY
)

def generate_document_embeddings(chunks):

    response = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=chunks,
        parameters={
            "input_type": "passage"
        }
    )

    return [
        item.values
        for item in response.data
    ]


def generate_query_embedding(query):

    response = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=[query],
        parameters={
            "input_type": "query"
        }
    )

    return response.data[0].values