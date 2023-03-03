import openai
import sys
import os

print("")
print("------- ChatGPT -------")
print(" API - Pedro Gonoring ")

# obtém os argumentos do script
args = sys.argv[1:]

def help():
    print("")
    print("Para utilizar o script")
    print("")

def exibirMensagem(response):
    print("")
    print(response["choices"][0]["text"])
    print("")

if(args[0] == "-h"):
    help()
else:
    # define a chave de API do OpenAI
    openai.api_key = "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"

    # define o prompt de entrada
    prompt = args[0]+". Em português"

    # define as configurações da solicitação
    model_engine = "text-davinci-002"
    temperature = 0.5
    max_tokens = 2000

    # envia a solicitação à API do OpenAI
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # exibe a resposta da API
    exibirMensagem(response)
    