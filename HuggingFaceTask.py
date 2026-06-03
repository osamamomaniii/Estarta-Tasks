import requests

HF_TOKEN = ""

URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json",
}

messages = []

while True:
    question = input("You: ")
    if question.lower() in ("exit", "quit"):
        break

    messages.append({"role": "user", "content": question})

    payload = {
        "model": "Qwen/Qwen2.5-72B-Instruct",
        "messages": messages,
        "max_tokens": 200,
    }

    response = requests.post(URL, headers=headers, json=payload)
    data = response.json()
    answer = data["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": answer})
    print(f"AI: {answer}\n")
