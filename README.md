# ◆ FlaskShop

> Template de e-commerce completo, moderno e pronto para produção — construído com **Python + Flask** e um front-end escuro de alto nível.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## ✨ Visão Geral

FlaskShop é um template de e-commerce funcional e visualmente sofisticado, com tema escuro e identidade dourada. Ideal para pequenos negócios que querem vender produtos físicos ou digitais com integração direta ao **WhatsApp** e **Instagram**, sem depender de plataformas de terceiros.

---

## 🚀 Funcionalidades

- 🔐 **Autenticação completa** — Cadastro, login e sessões seguras com hash de senha
- 🛍️ **Catálogo de produtos** — Grade responsiva com imagem, categoria, preço e status de estoque
- 📦 **Pedidos e histórico** — Criação de pedidos e visualização no perfil do usuário
- 💬 **Integração WhatsApp** — Botão de compra que abre conversa direta com mensagem pré-preenchida
- 📷 **Integração Instagram** — Link direto para o perfil da loja em toda a interface
- 🔌 **API REST (JSON)** — Endpoints para produtos, cadastro, login e pedidos
- 🌑 **Design dark premium** — Interface elegante com tipografia Playfair Display + DM Sans

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.8+, Flask 2.x |
| Banco de dados | SQLite 3 (via módulo nativo) |
| Segurança | Werkzeug (hash de senha) |
| Frontend | HTML5, CSS3 puro, Jinja2 |
| Fontes | Google Fonts (Playfair Display, DM Sans) |

---

## 📁 Estrutura de Pastas

```
flaskshop/
├── app.py                  # Aplicação principal e rotas
├── database.db             # Banco de dados SQLite (gerado automaticamente)
└── templates/
    ├── base.html           # Layout base com navbar e estilos globais
    ├── index.html          # Página inicial — catálogo de produtos
    ├── produto.html        # Página de detalhes do produto
    ├── login.html          # Tela de login
    ├── cadastro.html       # Tela de cadastro
    └── perfil.html         # Perfil do usuário e histórico de pedidos
```

---

## ⚙️ Como Instalar e Rodar

### Pré-requisitos
- Python 3.8 ou superior
- pip

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/flaskshop.git
cd flaskshop

# 2. (Recomendado) Crie um ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate

# 3. Instale as dependências
pip install flask werkzeug

# 4. Configure suas redes sociais em app.py
# WHATSAPP_NUMBER = '5511999999999'
# INSTAGRAM_USER  = 'seuusername'

# 5. Rode o servidor
python app.py
```

Acesse em: **http://localhost:5000**

> O banco de dados e os produtos de exemplo são criados automaticamente na primeira execução.

---

## 🔌 Endpoints da API

| Método | Rota | Descrição |
|---|---|---|
| GET | `/api/produtos` | Lista todos os produtos ativos |
| GET | `/api/produto/<id>` | Detalhes de um produto |
| POST | `/api/cadastro` | Cadastrar novo usuário |
| POST | `/api/login` | Autenticar usuário |
| POST | `/api/pedido` | Criar pedido (requer login) |
| GET | `/api/social` | Retorna links das redes sociais |

---

## 🌐 Deploy

### Render (gratuito)
1. Crie uma conta em [render.com](https://render.com)
2. Novo serviço → **Web Service** → conecte seu repositório GitHub
3. Build command: `pip install flask werkzeug`
4. Start command: `python app.py`

### Railway
1. Acesse [railway.app](https://railway.app) e conecte o GitHub
2. O Railway detecta Flask automaticamente
3. Adicione a variável de ambiente `PORT=5000`

### PythonAnywhere (gratuito)
1. Faça upload dos arquivos em [pythonanywhere.com](https://pythonanywhere.com)
2. Configure um Web App Flask apontando para `app.py`

> **Importante para produção:** troque o valor de `app.secret_key` por uma string longa e aleatória antes de publicar.

---

## 🗺️ Roadmap

- [ ] Painel administrativo com CRUD de produtos
- [ ] Upload de imagens direto pela interface
- [ ] Integração com Stripe / Mercado Pago
- [ ] Filtro e busca de produtos por categoria
- [ ] E-mails transacionais (confirmação de pedido)
- [ ] Suporte a múltiplas imagens por produto
- [ ] PWA (Progressive Web App)

---

## 📄 Licença

Distribuído sob a licença **MIT**. Veja o arquivo [`LICENSE`](./LICENSE) para mais detalhes.
