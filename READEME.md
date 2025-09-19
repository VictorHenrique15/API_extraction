### Backup local

Este projeto mantém uma pasta `backup/` com cópias de segurança dos arquivos principais.  
Essa pasta está listada no `.gitignore` e não é versionada no repositório público.

### Segurança e boas práticas aplicadas

- Remoção da chave da API do código-fonte para evitar exposição pública
- Implementação do uso de variáveis de ambiente via `.env` com a biblioteca `python-dotenv`
- Adição do arquivo `.env` ao `.gitignore` para garantir que credenciais não sejam versionadas
- Reescrita do histórico do Git com `git filter-repo` para remover commits antigos que continham dados sensíveis
- Criação de uma pasta `backup/` para preservar versões anteriores e garantir segurança durante operações críticas
- Refatoração do script `coleta_dados.py` para consumir a API da NASA de forma segura e reutilizável
- Início da integração com banco de dados PostgreSQL para armazenar os dados coletados
