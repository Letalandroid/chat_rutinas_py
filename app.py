import ollama

prompt = "Hola"

res = ollama.chat(
    model="llama3.2",
    messages=[
        {'role': 'user', 'content': prompt}
    ]
)

print(res['message']['content'])