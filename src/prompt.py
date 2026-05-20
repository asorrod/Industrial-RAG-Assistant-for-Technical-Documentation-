
def build_prompt(query:str, retrieved_chunks:list, config):

    context = ""

    for i, chunk in enumerate(retrieved_chunks):
        context += f"\n[Chunk {i}]\n{chunk['text']}\n"
    
    system_prompt = config["prompt"]["system"]
    template = config["prompt"]["template"]

    prompt = template.format(
        context=context,
        query=query
    )

    return system_prompt + "\n\n" + prompt