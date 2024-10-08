import ollama
from modules import t
from time import sleep
import json

question = t.send_question('Del 1 al 5, ¿En que nivel de entrenamiento te encuentras?')

if question:
    r1 = t.res1(question)
    sleep(2)
    print('\n[!] Preparando rutinas...')
    sleep(3)
    print('Nada como una taza de café para empezar el día ☕...')
    sleep(5)
    print('[!] Esto podria demorar un poco...\n')

res = ollama.chat(
model="llama3.2",
messages=[
        {'role': 'user',
        'content': f'Genera dia y rutina para nivel de entrenamiento {r1} y solo genera un JSON'},
        {'role': 'user',
        'content': 'Siguiendo el formato {dia, rutina[{ejercicio, sets, repeticiones, descanso}]}'},
        {'role': 'user',
        'content': 'Formato: "lunes": [{"ejercicio": "Peso Básico", "sets": 4, "repeticiones": 10, "peso": 60},{"ejercicio": "Sentadillas con mancuernas", "sets": 3, "repeticiones": 12, "peso": 45},{"ejercicio": "Flexiones de piernas", "sets": 3, "repeticiones": 15, "peso": 30},{"ejercicio": "Curl de bíceps con mancuernas", "sets": 3, "repeticiones": 10, "peso": 45}]'}
    ]
)

# response = json.loads(res['message']['content'].replace('```json', '').replace('```',''))
response = res['message']['content'].replace('```json', '').replace('```','')
print(response)