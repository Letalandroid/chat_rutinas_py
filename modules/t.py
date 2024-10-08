import pyttsx3 as px

def send_question(t):
    print(t)
    print('> ', end='')

    try:
        res = int(input(''))
        return res
    except ValueError:
        print('Por favor ingresa un número.')
        return False

def res1(res):
    if isinstance(res, int) and (res < 1 or res > 5):
        print('Error, por favor ingresa un número entre 1 y 5')
        return False

    return res

def say(t):
    say_text = px.init()
    say_text.say(t)
    say_text.runAndWait()