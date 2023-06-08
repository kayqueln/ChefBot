import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

ingredientes = []
cont = 1

def IA(quantidade, ingredientes):
    frase = (f"Mê dê uma receita nutritiva usando apenas {quantidade} ingredientes: {ingredientes}")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= frase,
        temperature=0.7,
        max_tokens=2048,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()



quantidade = int(input("Digite a quantidade de alimentos que você tem disponível: "))

for i in range(quantidade):
    ingrediente = input(f"Digite o {cont}° ingredinte: ")
    ingredientes.append(ingrediente)
    cont += 1

print(IA(quantidade, ingredientes))