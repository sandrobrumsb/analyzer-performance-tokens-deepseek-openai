"""
Projeto que calcula e compara os custos de uma requisição entre as APIs DEEPSEEK e OPENAI.

 ----AQUI VAMOS OBTER:----
1- Quantidade de tokens de entrada do usuário.
2- Quantidade de tokens de resposta do modelo.
3- Total de tokens usados na requisição.
4- Tempo de duração da requisição.
5- Custo estimado da requisição para cada API.
"""

from openai import OpenAI as OpenAIClient  # Importa a classe com alias
from dotenv import load_dotenv  # Para carregar variáveis de ambiente do .env
import os  # Para acessar as variáveis de ambiente
import time  # Para medir o tempo de execução da requisição

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa os clientes das APIs
client_deepseek = OpenAIClient(
    api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
)

client_openai = OpenAIClient(api_key=os.getenv("OPENAI_API_KEY"))

# Modelos utilizados para cada API
model_deepseek = "deepseek-chat"
model_gpt = "gpt-4o"

# Mensagens de entrada para teste
prompt_user = "Calcule a área de um triângulo com base de 12 cm e altura de 8 cm."
prompt_system = """
Quero que me retorne a resposta nesse formato:
A área de um triângulo é dada pela fórmula: Área = (base × altura) / 2
Substituindo os valores: Área = (6 × 4) / 2 = 24 / 2 = 12 cm²
"""


# Função que realiza a requisição à API Deepseek
def deepseek_response(prompt_user):
    start = time.time()  # Marca o início da requisição

    response = client_deepseek.chat.completions.create(
        model=model_deepseek,
        messages=[
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": prompt_user},
        ],
        stream=False,
    )

    end = time.time()  # Marca o final da requisição
    duration = end - start  # Tempo total de execução

    usage = response.usage  # Informações de uso de tokens
    cost = round(
        (usage.total_tokens / 1_000_000) * 2.19, 5
    )  # Custo estimado em dólares

    return response.choices[0].message.content, duration, usage, cost


# Função que realiza a requisição à API OpenAI
def gpt_response(prompt_user):
    start = time.time()  # Início da requisição

    response = client_openai.chat.completions.create(
        model=model_gpt,
        messages=[
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": prompt_user},
        ],
        stream=False,
    )

    end = time.time()  # Fim da requisição
    duration = end - start

    usage = response.usage
    cost = round(
        (usage.total_tokens / 1_000_000) * 2.19, 5
    )  # Mesma taxa para comparação

    return response.choices[0].message.content, duration, usage, cost


# -------------------------------
# EXECUÇÃO E IMPRESSÃO DOS RESULTADOS
# -------------------------------

# Resultado da API Deepseek
response, duration, usage, cost = deepseek_response(prompt_user)

print(f"\n---- RESPOSTA DEEPSEEK ({model_deepseek}) ----\n{response}\n")
print(
    f"""PROMPT_TOKENS (entrada do usuário): {usage.prompt_tokens}
COMPLETION_TOKENS (resposta do modelo): {usage.completion_tokens}
TOTAL DE TOKENS USADOS: {usage.total_tokens}
TEMPO DE DURAÇÃO: {duration:.2f} segundos
CUSTO ESTIMADO: ${cost}
"""
)

# Resultado da API OpenAI (GPT)
response, duration, usage, cost = gpt_response(prompt_user)

print(f"\n---- RESPOSTA OPENAI GPT ({model_gpt}) ----\n{response}\n")
print(
    f"""PROMPT_TOKENS (entrada do usuário): {usage.prompt_tokens}
COMPLETION_TOKENS (resposta do modelo): {usage.completion_tokens}
TOTAL DE TOKENS USADOS: {usage.total_tokens}
TEMPO DE DURAÇÃO: {duration:.2f} segundos
CUSTO ESTIMADO: ${cost}
"""
)
