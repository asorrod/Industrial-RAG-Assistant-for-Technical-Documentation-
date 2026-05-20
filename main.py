from src.pipeline import run_pipeline
from pathlib import Path
from utils import load_config, load_index
from sentence_transformers import SentenceTransformer
from src.index import build_index

def chat_loop(embeddings, config, model):
    print("[INFO] RAG ready! Type 'exit' to quit.\n")

    while True:
        query = input("Ask: ")

        if query.lower() in ["exit", "quit"]:
            break

        try:
            answer = run_pipeline(query, embeddings, config, model)
            print("\n--- ANSWER ---")
            print(answer)
            print("\n")
        except Exception as e:
            print(f"[ERROR] {e}")
    

def main():

    base_dir = Path(__file__).resolve().parent
    config = load_config(base_dir / "configs" / "config.yaml")

    model = SentenceTransformer(config["model"]["model_name"])

    print("[INFO] Loading index...")

    embeddings_path = base_dir / config["storage"]["embeddings_path"]


    if config["index"]["rebuild"] or not embeddings_path.exists():
        print("[INFO] Building index...")
        build_index(config, model)

    print("EXPECTED PATH:", embeddings_path)
    print("EXISTS:", embeddings_path.exists())
    print("ABSOLUTE:", embeddings_path.resolve())

    embeddings = load_index(embeddings_path)

    
    chat_loop(embeddings, config, model)



if __name__ == "__main__":
    main()