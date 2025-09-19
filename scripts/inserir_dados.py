import psycopg2 # CONECTA AO BANCO DE DADOS POSTGRESQL
from dotenv import load_dotenv # CARREGA VARIÁVEIS DE AMBIENTE DO ARQUIVO .ENV COMO SENHAS E CAHVES DE API
import os # PERMITE ACESSAR AS VARIÁVEIS DE AMBIENTE QUE FORAM CARREGADAS NO ARQUIVO .ENV

from coleta_dados import coleta_dados # IMPORTA A FUNÇÃO COLETA_DADOS DO ARQUIVO COLETA_DADOS.PY

response = coleta_dados()
data = response.json() # CHAMA A FUNÇÃO COLETA_DADOS E ARMAZENA O RESULTADO NA VARIÁVEL DATA

load_dotenv()

# CRIA CONEXÃO COM O BANCO DE DADOS POSTGRESQL USANDO PARAMETROS DE AMBIENTE
conn = psycopg2.connect( 
    dbname= os.getenv ('DB_NAME'),
    user= os.getenv('DB_USER'),
    password= os.getenv('DB_PASSWORD'),
    host= os.getenv('DB_HOST'),
    port= int(os.getenv('DB_PORT'))
)

cur = conn.cursor() # CRIA "CANAL DE COMUNICAÇÃO" ENTRE PYTHON E O BANCO DE DADOS
# EXCUTA COMANDO SQL PARA INSERIR DADOS NA TABELA "INSERT INTO" E DEFINE VALOR DE VARIÁVEIS USANDO PLACEHOLDERS (%s)
cur.execute("""     
    INSERT INTO nasa_apod (title, date, explanation, url, hdurl, media_type, copyright)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", (
    data.get("title"), # EXTRAI VALORES DO DICIONÁRIO DATA USANDO O MÉTODO .GET
    data.get("date"),
    data.get("explanation"),
    data.get("url"),
    data.get("hdurl"),
    data.get("media_type"),
    data.get("copyright")
))

conn.commit() # SALVA AS ALTERAÇÕES NO BANCO DE DADOS SEM ISSO, AS ALTERAÇÕES NÃO SERÃO SALVAS
cur.close() # FECHA O CANAL DE COMUNICAÇÃO ENTRE PYTHON E O BANCO DE DADOS
conn.close() #FECHA A CONEXÃO COM O BANCO DE DADOS
