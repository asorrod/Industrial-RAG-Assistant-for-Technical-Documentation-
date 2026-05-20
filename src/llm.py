import requests

def generate_response(prompt:str, config):
    model = config["llm"]["model"]
    temperature= config["llm"]["temperature"]
    stream = config["llm"]["stream"]
    top_p = config["llm"]["top_p"]
    max_tokens= config["llm"]["max_tokens"]
    url = config["llm"]["url"]

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream,
        "options": {
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": max_tokens
            }
    }

    response = requests.post(url=url, json=payload)

    return response.json()["response"]
