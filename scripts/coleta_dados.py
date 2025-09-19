import requests
from dotenv import load_dotenv
import os

# VARIÁVEL QUE DEFINE A MINHA CHAVE DA API NASA
CHAVE_API = os.getenv('NASA_API_KEY') 
# URL DA API COM A VARAIVEL DEFINIDA DA CHAVE
url = f'https://api.nasa.gov/planetary/apod?api_key={CHAVE_API}'

# ENVIA REQUISIÇÃO (GET) PARA A URL DA API E ARMAZENA A RESPOSTA NA VARIÁVEL RESPONSE
response = requests.get(url)

# CONVERTE A RESPOSTA PARA JSON E ARMAZENA NA VARIÁVEL DATA 
data = response.json()

# IMPRIME O CONTEÚDO DA VARIÁVEL DATA
print(data)

# VALIDANDO E TRATANDO DADOS

# VERIFICA SE A REQUISIÇÃO FOI BEM SUCEDIDA (CÓDIGO 200)
if response.status_code == 200:

# RESPONDE COM SUCESSO CASO SEJA 200
    print("Requisição bem sucedida!")

# IMPRIME O TÍTULO, DATA E URL DA IMAGEM
    print("Título:", data.get('title'))

# IMPRIME A DATA DA IMAGEM
    print("Data:", data.get('date'))

# IMPRIME A URL DA IMAGEM
    print("URL da imagem:", data.get('url'))
    
# UTILIZAR .GET POIS É MAIS SEGURO, NÃO LEVA A ERRO CASO A CHAVE NÃO EXISTA, APENAS RETORNA NONE

# RESPONDE COM FALHA CASO NÃO SEJA 200    
else:
    print("Erro ao acessar a API", response.status_code)
