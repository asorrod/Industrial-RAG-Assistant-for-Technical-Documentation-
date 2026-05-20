
def chunk_embedding(chunks: list, config, model):
    embedding_output = []
    batch_size = config["embeddings"]["batch_size"]

    for i in range(0, len(chunks), batch_size):

        batch_chunks = chunks[i:i+batch_size]

        batch_texts = [chunk["text"] for chunk in batch_chunks]
        
        batch_vectors = model.encode(inputs=batch_texts, batch_size=batch_size, normalize_embeddings=True)

        for chunk, vector in zip(batch_chunks, batch_vectors):
        
            embedding_output.append({
                "embedding": vector,
                "file": chunk["file"],
                "chunk_id": chunk["chunk_id"],
                "page_start": chunk["page_start"],
                "page_end": chunk["page_end"],
                "text": chunk["text"]
            })

    return embedding_output