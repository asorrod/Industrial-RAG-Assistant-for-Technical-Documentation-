
def token_text_chunking(text_pdf: list, config):
    chunk_buffer = []
    chunk_size_control = config["chunking"]["chunk_size"]
    overlap = int(chunk_size_control * config["chunking"]["overlap"])

    chunk_output = []
    chunk_id = 0

    page_start = None
    page_end = None
    current_file = None

    def flush_chunk():
        """Save the current chunk if it has content"""
        nonlocal chunk_id, chunk_buffer, page_start, page_end, current_file

        if chunk_buffer:
            chunk_output.append({
                "file": current_file,
                "chunk_id": chunk_id,
                "page_start": page_start,
                "page_end": page_end,
                "text": " ".join(chunk_buffer)
            })

            chunk_id+=1

            chunk_buffer = chunk_buffer[-overlap:]

            page_start = page_end

    for page in text_pdf:
        file = page["file"]
        page_num = page["page_num"]
        text = page["text"]
        tokens = text.split()

        if current_file is not None and file != current_file:
            flush_chunk()
            chunk_buffer = []
            page_start = None
            page_end = None

        current_file = file

        for token in tokens:

            if page_start is None:
                page_start = page_num
            
            page_end = page_num

            chunk_buffer.append(token)

            if len(chunk_buffer) >= chunk_size_control:
                flush_chunk()
                
    flush_chunk()

    return chunk_output