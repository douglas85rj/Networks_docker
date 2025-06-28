
# Networks_docker

Projeto de exemplo para integração de múltiplos containers Docker utilizando Flask, MySQL e comunicação entre serviços.

## Estrutura do Projeto

```

Networks_docker/

├── Api_json/

│   ├── app.py

│   └── Dockerfile

├── Conn_Containers/

│   ├── flask/

│   │   ├── app.py

│   │   └── Dockerfile

│   └── mysql/

│       ├── Dockerfile

│       └── schema.sql

├── Host/

│   ├── app.py

│   └── Dockerfile

└── README.md

```

## Serviços

- **MySQL**: Banco de dados relacional, inicializado com o script `schema.sql`.
- **Flask (Conn_Containers/flask)**: API Flask conectada ao banco MySQL.
- **Host**: Outro serviço Flask, também pode se conectar ao banco.
- **Api_json**: Serviço Flask para manipulação de dados JSON.

## Como rodar

1. **Build dos containers**

Acesse cada pasta de serviço e execute:

```sh

docker build -t <nome_da_imagem> .

```

Exemplo para o MySQL:

```sh

cd Conn_Containers/mysql

docker build -t mysqlnetapi .

```

2. **Criação de rede Docker**

```sh

docker network create flasknet

```

3. **Suba o container MySQL**

```sh

docker run -d -p 3307:3306 --name mysql_api_container --rm --network flasknet -e MYSQL_ALLOW_EMPTY_PASSWORD=yes mysqlnetapi

```

4. **Suba os containers Flask**

Exemplo para o serviço Flask:

```sh

cd Conn_Containers/flask

docker build -t flaskapi .

docker run -d --name flask_api_container --rm --network flasknet -p 5000:5000 flaskapi

```

Repita para os outros serviços conforme necessário.

## Configuração do Banco de Dados

O banco de dados e as tabelas são criados automaticamente via `schema.sql` ao iniciar o container MySQL.

- Usuário: `flaskuser`
- Senha: `280903`
- Banco: `flaskhost` ou `flaskdocker` (ajuste conforme seu app)

## Exemplos de uso

- Acesse o endpoint principal do Flask:

  ```

  http://localhost:5000/

  ```
- Para inserir um usuário aleatório:

  ```

  POST http://localhost:5000/inserthost

  ```

## Observações

- Certifique-se de que as portas 3306/3307 e 5000/5001 estejam livres no seu sistema.
- Ajuste as variáveis de ambiente conforme necessário para produção.

---

Projeto para fins didáticos. Sinta-se à vontade para adaptar!
