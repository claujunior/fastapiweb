[README.md](https://github.com/user-attachments/files/27574148/README.md)
# 🔐 FastAPI Users API

API REST assíncrona para gerenciamento de usuários com autenticação JWT, construída com **FastAPI**, **MongoDB** e **Docker**.

---

## 🚀 Tecnologias

| Tecnologia | Descrição |
|---|---|
| [FastAPI](https://fastapi.tiangolo.com/) | Framework web assíncrono para construção de APIs |
| [MongoDB](https://www.mongodb.com/) | Banco de dados NoSQL orientado a documentos |
| [Motor](https://motor.readthedocs.io/) | Driver assíncrono para MongoDB |
| [python-jose](https://python-jose.readthedocs.io/) | Geração e validação de tokens JWT |
| [Passlib + Argon2](https://passlib.readthedocs.io/) | Hash seguro de senhas |
| [Pydantic](https://docs.pydantic.dev/) | Validação de dados e serialização |
| [Docker Compose](https://docs.docker.com/compose/) | Containerização do banco de dados |

---

## 📁 Estrutura do Projeto

```
fastapiweb/
├── auth/
│   ├── password_handler.py   # Hash e verificação de senhas com Argon2
│   └── token_handler.py      # Geração e validação de tokens JWT
├── database/
│   └── mongodb.py            # Conexão assíncrona com o MongoDB (Motor)
├── dto/
│   └── user_dto.py           # DTO de resposta (expõe apenas username)
├── exceptions/
│   └── handler.py            # Handler centralizado de erros HTTP
├── model/
│   └── user_model.py         # Modelo de domínio (username + password)
├── repositories/
│   └── user_repository.py    # Acesso ao banco de dados
├── routers/
│   └── user_router.py        # Definição das rotas /users
├── services/
│   └── user_service.py       # Regras de negócio
├── main.py                   # Ponto de entrada da aplicação
├── docker-compose.yml        # Configuração do container MongoDB
└── requirements.txt          # Dependências do projeto
```

---

## ⚙️ Como executar

### Pré-requisitos

- Python 3.10+
- Docker e Docker Compose

### 1. Clone o repositório

```bash
git clone https://github.com/claujunior/fastapiweb.git
cd fastapiweb
```

### 2. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
MONGO_URL=mongodb://localhost:27017
JWT_SECRET=sua_chave_secreta_aqui
```

### 3. Suba o MongoDB com Docker

```bash
docker-compose up -d
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`.

A documentação interativa (Swagger) estará em `http://localhost:8000/docs`.

---

## 📡 Endpoints

### `POST /users` — Cadastrar usuário

Cria um novo usuário com senha hasheada.

**Request body:**
```json
{
  "username": "claudivan",
  "password": "minhasenha"
}
```

**Response `200`:**
```json
{
  "id": "664f1a2b3c4d5e6f7a8b9c0d",
  "message": "Usuário cadastrado"
}
```

---

### `POST /users/login` — Autenticar usuário

Valida as credenciais e retorna um token JWT.

**Request body:**
```json
{
  "username": "claudivan",
  "password": "minhasenha"
}
```

**Response `200`:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

---

### `GET /users` — Listar usuários 🔒

Retorna todos os usuários cadastrados. **Requer autenticação JWT.**

**Header:**
```
Authorization: Bearer <token>
```

**Response `200`:**
```json
[
  { "username": "claudivan" },
  { "username": "outro_usuario" }
]
```

---

## 🔒 Autenticação

A API utiliza **JWT (JSON Web Token)** com algoritmo `HS256` e expiração de **1 hora**.

Para acessar rotas protegidas, inclua o token no header:

```
Authorization: Bearer <seu_token>
```

As senhas são armazenadas com hash **Argon2**, um dos algoritmos mais seguros disponíveis para hashing de senhas.

---

## 🏗️ Arquitetura

A aplicação segue uma arquitetura em camadas com separação clara de responsabilidades:

```
Router → Service → Repository → MongoDB
```

- **Router**: recebe as requisições HTTP e delega para o Service
- **Service**: contém as regras de negócio (validação de usuário existente, autenticação)
- **Repository**: acesso direto ao banco de dados via Motor
- **DTO**: garante que dados sensíveis (como a senha) nunca sejam expostos nas respostas

---

## 🐳 Docker Compose

O `docker-compose.yml` sobe um container MongoDB com persistência de dados em volume:

```yaml
services:
  mongodb:
    image: mongo
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db
```
