# Networks_docker

Projeto de exemplo para integração de múltiplos containers Docker utilizando Flask, MySQL e comunicação entre serviços.

## Estrutura do projeto (resumida)

```
Networks_docker/
├── Api_json/            # Serviço Flask para manipulação de JSON
│   ├── app.py
│   └── Dockerfile
├── Conn_Containers/     # Conteúdo principal com docker-compose e serviços de conexão
│   ├── docker-compose.yaml
│   ├── config/
│   │   └── db.env
│   ├── flask/
│   │   ├── app.py
│   │   └── Dockerfile
│   └── mysql/
│       ├── Dockerfile
│       └── schema.sql
├── Host/                # Serviço adicional (expõe 5001)
│   ├── app.py
│   └── Dockerfile
└── README.md
```

## Serviços principais

- `db` (MySQL): definido em `Conn_Containers/docker-compose.yaml`, inicializa o banco usando `schema.sql`.
- `backend` (Flask): Flask app definido em `Conn_Containers/flask` e referenciado pelo `docker-compose`.
- `Api_json` e `Host`: serviços Flask independentes (podem ser executados separadamente). `Host` expõe por padrão a porta 5001.

> Observação: o `docker-compose.yaml` presente em `Conn_Containers/` já declara os serviços `db` e `backend`. Recomenda-se usar o docker-compose para orquestração local.

## Credenciais e banco

O script `Conn_Containers/mysql/schema.sql` cria o banco e o usuário com as seguintes informações:

- Banco: `flaskdocker`
- Usuário: `flaskuser`
- Senha: `280903`

Além disso, `Conn_Containers/config/db.env` define `MYSQL_ALLOW_EMPTY_PASSWORD=True` por conveniência em ambiente de teste.

## Como rodar (modo recomendado: docker-compose)

1. Construa as imagens necessárias localmente com as tags esperadas pelo `docker-compose` (opcional, se já existirem imagens com esses nomes). A configuração atual do `docker-compose` usa as imagens `mysqlcompose` e `flaskcompose`.

```sh
# build da imagem MySQL (contexto: Conn_Containers/mysql)
cd Conn_Containers/mysql
docker build -t mysqlcompose .

# build do backend Flask (contexto: Conn_Containers/flask)
cd ../flask
docker build -t flaskcompose .

# volte para a pasta do compose
cd ..
```

1. Inicie os serviços com o docker-compose (dentro de `Conn_Containers/`):

```sh
cd Conn_Containers
docker-compose up -d
```

Isso irá criar a rede de backend e subir os serviços:

- MySQL: mapeamento de porta `3306:3306`
- backend (Flask): mapeamento de porta `5000:5000`

1. (Opcional) Se quiser executar `Host` ou `Api_json` separadamente e conectá-los à mesma rede criada pelo docker-compose:

```sh
# encontre a rede criada pelo compose (geralmente contém a palavra 'backend')
docker network ls

# build e rode o Host anexado à rede do compose (ajuste o nome da rede conforme o output acima)
cd ../../Host
docker build -t hostapp .
docker run -d --name host_app_container --network <NOME_DA_REDE_DO_COMPOSE> -p 5001:5001 hostapp
```

## Como acessar

-- Backend Flask (definido em `Conn_Containers/flask`): `http://localhost:5000/`
-- Host (quando rodando separadamente): `http://localhost:5001/`

Exemplo de endpoint (quando o backend estiver ativo):

`POST http://localhost:5000/inserthost`

## Observações e dicas

- Se você preferir que o `docker-compose` faça o build das imagens automaticamente, podemos alterar o `docker-compose.yaml` para usar `build:` em vez de `image:` — me avise que eu ajusto o arquivo.
- As portas 3306 e 5000 devem estar livres para evitar conflitos.
- Este repositório é um ambiente de teste/demonstração. Para produção, configure senhas seguras, volumes persistentes e políticas de reinício adequadas.

---

Projeto para fins didáticos. Sinta-se à vontade para adaptar!

