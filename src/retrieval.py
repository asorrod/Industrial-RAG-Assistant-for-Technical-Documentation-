def retrieve(query: str, embeddings: list, config, model):
    query_vector = model.encode(inputs=query, normalize_embeddings=True)
    retrieval_output = []

    batch_size = config["retrieval"]["batch_size"]
    top_k = config["retrieval"]["top_k"]

    for i in range(0, len(embeddings), batch_size):
        batch = embeddings[i:i+batch_size]

        batch_vectors = [item["embedding"] for item in batch]

        similarities = model.similarity(query_vector, batch_vectors)[0]

        for item, score in zip(batch, similarities):
            retrieval_output.append({
                "score": float(score),
                "file": item["file"],
                "chunk_id": item["chunk_id"],
                "page_start": item["page_start"],
                "page_end": item["page_end"],
                "text": item["text"]
            })

        retrieval_output = sorted(
            retrieval_output,
            key=lambda x: x["score"],
            reverse=True
        )
    
    return retrieval_output[:top_k]