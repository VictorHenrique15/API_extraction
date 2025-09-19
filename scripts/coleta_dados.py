import requests # PARA FAZER REQUISIÇÕES NA API
from dotenv import load_dotenv # CARREGA VARIÁVEIS DE AMBIENTE DO ARQUIVO .ENV COMO SENHAS E CAHVES DE API
import os # PERMITE ACESSAR AS VARIÁVEIS DE AMBIENTE QUE FORAM CARREGADAS NO ARQUIVO .ENV

load_dotenv()

# INICIA A FUNÇÃO DE COLETA DE DADOS
def coleta_dados(): # FUNÇÃO PARA COLETAR DADOS DA API NASA 
    CHAVE_API = os.getenv('NASA_API_KEY') # VARIÁVEL QUE DEFINE A CHAVE DA API NASA
    url = f'https://api.nasa.gov/planetary/apod?api_key={CHAVE_API}'  # URL DA API COM A VARAIVEL DEFINIDA DA CHAVE
    response = requests.get(url) # ENVIA REQUISIÇÃO (GET) PARA A URL DA API E ARMAZENA A RESPOSTA NA VARIÁVEL RESPONSE

    return response # FIM DA FUNÇÃO

response = coleta_dados() # FAZ REQUISIÇÃO E ARMAZENA NA VARIÁVEL RESPONSE

# INICIA VALIDAÇÃO E TRATANDO DE DADOS
if response.status_code == 200:  # VERIFICA SE A REQUISIÇÃO FOI BEM SUCEDIDA
    try:
        data = response.json()
        print(data.get("title"))
    except ValueError:
        print("Erro: resposta não está em formato JSON.")
        print("Conteúdo bruto:", response.text)

else:
    print("Erro ao acessar a API", response.status_code)  # RESPONDE COM FALHA CASO NÃO SEJA 200

