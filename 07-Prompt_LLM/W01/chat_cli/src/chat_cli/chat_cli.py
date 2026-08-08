import ollama

MODEL = "qwen2.5:1.5b"

def main():
    history = []
    system = {
        "role": "system",
        "content": "你是一位耐心的中文助教"
    }

    history.append(system)
    print(
        f"模型 {MODEL}，输入 /quit退出"
    )

    while True:
        user = input("\nuser> ").strip()
        if user == "/quit":
            break

        if user == "/clear":
            history=[system]
            print("clear history")
            continue

        history.append({
            "role": "user",
            "content": user,
        })

        print("AI> ", end="")

        stream = ollama.chat(
            model=MODEL,
            messages=history,
            stream=True
        )

        answer = ""

        for chunk in stream:
            text=chunk["message"]["content"]
            print(text, end="", flush=True)
            answer+=text

        print()

        history.append({
            "role": "assistant",
            "content": answer,
        })


