# Testes da API no Thunder Client

1. Inicie a API na raiz do projeto com `python app.py`.
2. No Thunder Client, abra **Collections** e escolha **Import**.
3. Importe `RoomHub.postman_collection.json`.
4. Execute os requests na ordem exibida. Os requests de criação guardam os IDs nas variáveis da coleção para os requests seguintes.

A coleção cobre os endpoints de usuários e moradias, incluindo validação de campos, email duplicado, preço negativo e respostas 404. Ao executar novamente, o email de usuário de exemplo pode já existir; remova o registro anterior ou troque o email no request **POST Criar usuario** antes de repetir.