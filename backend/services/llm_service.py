from openai import OpenAI

from config.settings import NVIDIA_API_KEY

client = OpenAI(
    api_key=NVIDIA_API_KEY,
    base_url="https://integrate.api.nvidia.com/v1"
)

def generate_answer(
    question,
    context
):

    prompt = f"""
    Use the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="nvidia/llama-3.3-nemotron-super-49b-v1",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0.1,
        max_tokens=512
    )

    return response.choices[0].message.content