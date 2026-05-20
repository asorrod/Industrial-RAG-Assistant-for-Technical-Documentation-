from pathlib import Path
import pickle

from src.ingestion import extract_pdfs
from src.chunking import token_text_chunking
from src.embeddings import chunk_embedding


def build_index(config, model):
    base_dir = Path(__file__).resolve().parent.parent
    data_path = base_dir / config["data"]["data_path"]
    output_path = base_dir / config["storage"]["embeddings_path"]

    print("[INFO] Extracting PDFs...")
    pages = extract_pdfs(data_path)

    print("[INFO] Chunking text...")
    chunks = token_text_chunking(pages, config)

    print("[INFO] Generating embeddings...")
    embeddings = chunk_embedding(chunks, config, model)

    print("[INFO] Saving index...")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        pickle.dump(embeddings, f)

    print(f"[INFO] Index saved at: {output_path}")

    return output_path
