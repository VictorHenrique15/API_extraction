# API Extraction - NASA APOD

Este projeto realiza a extração de dados da API pública da NASA (Astronomy Picture of the Day) e armazena as informações em um banco de dados PostgreSQL. Idealizado como parte do meu portfólio, ele demonstra boas práticas de segurança, consumo de APIs e integração com banco de dados.

---

## Funcionalidades

- Consumo da API da NASA com autenticação via chave
- Armazenamento dos dados em PostgreSQL
- Uso de variáveis de ambiente para proteger credenciais
- Scripts organizados para coleta e inserção de dados

---

## Tecnologias utilizadas

- Python
- Requests
- psycopg2
- python-dotenv
- PostgreSQL
- Git

---

## Segurança e boas práticas aplicadas

- Remoção da chave da API do código-fonte para evitar exposição pública
- Implementação do uso de variáveis de ambiente via `.env` com a biblioteca `python-dotenv`
- Adição do arquivo `.env` ao `.gitignore` para garantir que credenciais não sejam versionadas
- Reescrita do histórico do Git com `git filter-repo` para remover commits antigos que continham dados sensíveis
- Criação de uma pasta `backup/` para preservar versões anteriores e garantir segurança durante operações críticas
- Refatoração do script `coleta_dados.py` para consumir a API da NASA de forma segura e reutilizável
- Início da integração com banco de dados PostgreSQL para armazenar os dados coletados

---

## Backup local

Este projeto mantém uma pasta `backup/` com cópias de segurança dos arquivos principais.  
Essa pasta está listada no `.gitignore` e não é versionada no repositório público.

---

## Objetivo

Este projeto foi desenvolvido com foco em aprendizado e construção de portfólio. Ele representa minha evolução como desenvolvedor.

## Uso de Inteligência Artificial

Durante o desenvolvimento deste projeto, utilizei ferramentas de Inteligência Artificial como suporte técnico e consultivo — especialmente para esclarecer dúvidas, revisar boas práticas e validar decisões. Com a IA atuando como aliada no processo de aprendizado e não como fonte de cópia e cola.
