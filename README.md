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

## 📸 Preview

<img width="1907" height="879" alt="Captura_de_tela_20260424_132604" src="https://github.com/user-attachments/assets/1d9965c6-8b2c-4999-8872-f8b05ab701cc" />
<br><br>
<img width="1894" height="879" alt="Captura_de_tela_20260424_132630" src="https://github.com/user-attachments/assets/e474a8dc-827e-4b36-9f11-78126b76af15" />
<br><br>
<img width="1914" height="877" alt="Captura_de_tela_20260424_132642" src="https://github.com/user-attachments/assets/d09fe103-b2bd-423e-966f-395153b42d62" />
<br><br>
<img width="1914" height="881" alt="Captura_de_tela_20260424_132656" src="https://github.com/user-attachments/assets/b3577be7-b7c3-48b2-b17d-619284d4cdef" />
<br><br>
<img width="1914" height="881" alt="Captura_de_tela_20260424_132709" src="https://github.com/user-attachments/assets/e219028b-5882-4c74-9936-2005af74b682" />
<br><br>
<img width="1914" height="881" alt="Captura_de_tela_20260424_132715" src="https://github.com/user-attachments/assets/465a999f-f11b-4b5d-b548-31ab318df987" />

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
