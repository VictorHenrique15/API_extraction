import psycopg2  # CONECTA AO BANCO DE DADOS POSTGRESQL
from dotenv import load_dotenv  # CARREGA VARIÁVEIS DE AMBIENTE DO ARQUIVO .ENV
import os  # PERMITE ACESSAR VARIÁVEIS DE AMBIENTE
from coleta_dados import coleta_dados  # IMPORTA A FUNÇÃO DE COLETA DE DADOS

load_dotenv()  # CARREGA AS VARIÁVEIS DO ARQUIVO .ENV

data = coleta_dados()  # CHAMA A FUNÇÃO E RECEBE OS DADOS COMO DICIONÁRIO

if data:  # VERIFICA SE OS DADOS FORAM COLETADOS COM SUCESSO
    try:
        # FAZ CONEXÃO COM O BANCO DE DADOS USANDO VARIÁVEIS DE AMBIENTE
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT'))
        )

        cur = conn.cursor()  # CRIA UM CURSOR PARA EXECUTAR COMANDOS SQL

        # EXECUTA COMANDO SQL PARA INSERIR OS DADOS NA TABELA
        cur.execute("""
            INSERT INTO nasa_apod (title, date, explanation, url, hdurl, media_type, copyright)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (date) DO NOTHING
        """, (
            data.get("title"),
            data.get("date"),
            data.get("explanation"),
            data.get("url"),
            data.get("hdurl"),
            data.get("media_type"),
            data.get("copyright")
        ))

        conn.commit()  # CONFIRMA AS ALTERAÇÕES NO BANCO DE DADOS
        cur.close()  # FECHA O CURSOR
        conn.close()  # FECHA A CONEXÃO COM O BANCO DE DADOS
        print("DADOS INSERIDOS COM SUCESSO!")

    except Exception as e:  # CAPTURA ERROS DURANTE O PROCESSO
        print(f"ERRO AO INSERIR DADOS: {e}")
else:
    print("NENHUM DADO FOI COLETADO.")
