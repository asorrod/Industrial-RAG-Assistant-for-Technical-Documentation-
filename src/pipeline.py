from src.retrieval import retrieve
from src.prompt import build_prompt
from src.llm import generate_response

def run_pipeline(query:str, embeddings, config, model):
    retrieved_chunks = retrieve(query, embeddings, config, model)
    prompt = build_prompt(query, retrieved_chunks, config)
    answer = generate_response(prompt, config)

    if not retrieved_chunks:
        return "No relevan context found."

    return answer


