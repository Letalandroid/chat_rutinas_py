from modules import t
from time import sleep
from threading import Thread
import ollama
import json
import pandas as pd

question = t.send_question('Del 1 al 5, ¿En que nivel de entrenamiento te encuentras?')

def init(r):
    res = ollama.chat(
    model="llama3.2",
    messages=[
            {'role': 'user',
            'content': f'Genera dia y rutina para nivel de entrenamiento {r} y solo genera un JSON'},
            {'role': 'user',
            'content': 'Siguiendo el formato {dia, rutina[{ejercicio, sets, repeticiones, descanso}]}'},
            {'role': 'user',
            'content': 'Formato comprimido: "{lunes":[{"ejercicio":"Peso Básico","sets":4,"repeticiones":10,"peso":60},{"ejercicio":"Sentadillas con mancuernas","sets":3,"repeticiones":12,"peso":45},{"ejercicio":"Flexiones de piernas","sets":3,"repeticiones":15,"peso":30},{"ejercicio":"Curl de bíceps con mancuernas","sets":3,"repeticiones":10,"peso":45}]}'}
        ]
    )

    rutinas = {}
    response = res['message']['content'].replace('```json', '').replace('```','')

    try:
        rutinas = json.loads(response)
    except json.JSONDecodeError as e:
        print(response)
        print("Error al cargar JSON")
        exit(1)

    dataframes = []

    for dia, ejercicios in rutinas.items():
        df_dia = pd.DataFrame(ejercicios)
        df_dia['día'] = dia
        dataframes.append(df_dia)

    df_total = pd.concat(dataframes, ignore_index=True)

    print(df_total.to_string())

    hilo = Thread(target=t.say, args=(df_total.to_string(),))

    hilo.start()
    hilo.join()
    print('')
    exit(0)

if question:
    r1 = t.res1(question)
    h = Thread(target=init, args=(r1,))
    h.start()

    sleep(3)
    print('\nPreparando rutinas...')

    sleep(6)
    print('Nada como una taza de café para empezar el día eh? ☕...')

    sleep(8)
    print('[!] Esto podria demorar un poco...\n')
    h.join()
