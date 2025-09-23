import requests # PARA FAZER REQUISIÇÕES NA API
from dotenv import load_dotenv # Para carregar variáveis de ambiente
import os # Para acessar as variáveis carregadas

load_dotenv()

# INICIA A FUNÇÃO DE COLETA DE DADOS

def coleta_dados(): # FUNÇÃO PARA COLETAR DADOS DA API NASA  Retorna um dicionário com os dados ou None em caso de erro.
                        
    CHAVE_API = os.getenv('NASA_API_KEY') # VARIÁVEL QUE DEFINE A CHAVE DA API NASA
    url = f'https://api.nasa.gov/planetary/apod?api_key={CHAVE_API}'  # URL DA API COM A VARAIVEL DEFINIDA DA CHAVE
    
    try:
        response = resquests.get(url) # FAZ A REQUISIÇÃO GET PARA A API
        if response.status_code == 200: # VERIFICA SE A REQUISIÇÃO FOI BEM SUCEDIDA
            try:
                data = response.json() # TENTA CONVERTER A RESPOSTA PARA JSON
                return data # RETORNA O DICIONÁRIO COM OS DADOS

            except ValueError:
                print('Erro: resposta não está em formato JSON.')
                print('Conteúdo bruto:', response.text)
                return None

        else: # RESPONDE COM FALHA CASO NÃO SEJA 200
            print('Erro ao acessar a API', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Erro na conexão com a API:{e}')
        return None # RETORNA NONE EM CASO DE ERRO NA CONEXÃO
