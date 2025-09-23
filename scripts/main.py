from coleta_dados import coleta_dados # IMPORTA A FUNÇÃO COLETA_DADOS DO ARQUIVO COLETA_DADOS.PY

data =  coleta_dados()
if data:
    print("Titulo da imagem do dia:", data.get("title"))  # IMPRIME OS DADOS COLETADOS
else:
    print("Não foi possível obter os dados.")

