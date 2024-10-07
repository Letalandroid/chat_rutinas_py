import openai

text = 'oli'

openai.Completion.create(engine='text-davinci-003',
                         prompt=text,
                         max_token=2048)