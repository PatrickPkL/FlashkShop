from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from functools import wraps
from datetime import datetime

# Garante que o Flask encontra os templates independente de onde o script é rodado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))
app.secret_key = 'sua-chave-secreta-troque-em-producao'

DB_PATH = os.path.join(BASE_DIR, 'database.db')


#  REDES SOCIAIS

WHATSAPP_NUMBER = '5511999999999'   # Número com DDI+DDD, sem espaços
INSTAGRAM_USER  = 'seuusername'     # Só o user sem o @




#  BANCO DE DADOS


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.executescript('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nome        TEXT    NOT NULL,
            email       TEXT    NOT NULL UNIQUE,
            senha       TEXT    NOT NULL,
            telefone    TEXT,
            criado_em   TEXT    DEFAULT (datetime('now','localtime'))
        );

        CREATE TABLE IF NOT EXISTS produtos (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nome        TEXT    NOT NULL,
            descricao   TEXT,
            preco       REAL    NOT NULL,
            estoque     INTEGER DEFAULT 0,
            imagem_url  TEXT,
            categoria   TEXT,
            ativo       INTEGER DEFAULT 1,
            criado_em   TEXT    DEFAULT (datetime('now','localtime'))
        );

        CREATE TABLE IF NOT EXISTS pedidos (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id   INTEGER NOT NULL,
            total        REAL    NOT NULL,
            status       TEXT    DEFAULT 'pendente',
            criado_em    TEXT    DEFAULT (datetime('now','localtime')),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        );

        CREATE TABLE IF NOT EXISTS itens_pedido (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            pedido_id   INTEGER NOT NULL,
            produto_id  INTEGER NOT NULL,
            quantidade  INTEGER NOT NULL,
            preco_unit  REAL    NOT NULL,
            FOREIGN KEY (pedido_id)  REFERENCES pedidos(id),
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        );
    ''')

    # Produtos de exemplo
    cur.execute('SELECT COUNT(*) FROM produtos')
    if cur.fetchone()[0] == 0:
        produtos_exemplo = [
            ('Produto Exemplo 1', 'Descrição do produto 1', 20.00, 50, '', 'Categoria A'),
            ('Produto Exemplo 2', 'Descrição do produto 2', 490.99, 0,  '', 'Categoria B'),
            ('Produto Exemplo 3', 'Descrição do produto 3', 10.99, 0, '', 'Categoria A'),
        ]
        cur.executemany(
            'INSERT INTO produtos (nome, descricao, preco, estoque, imagem_url, categoria) VALUES (?,?,?,?,?,?)',
            produtos_exemplo
        )

    conn.commit()
    conn.close()



#  DECORADORES

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated



#  ROTAS — PÁGINAS


@app.route('/')
def index():
    conn = get_db()
    produtos = conn.execute(
        'SELECT * FROM produtos WHERE ativo=1 ORDER BY criado_em DESC'
    ).fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos,
                           whatsapp=WHATSAPP_NUMBER, instagram=INSTAGRAM_USER)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome     = request.form.get('nome', '').strip()
        email    = request.form.get('email', '').strip().lower()
        senha    = request.form.get('senha', '')
        telefone = request.form.get('telefone', '').strip()

        if not nome or not email or not senha:
            flash('Preencha todos os campos obrigatórios.', 'erro')
            return render_template('cadastro.html')

        if len(senha) < 6:
            flash('A senha deve ter ao menos 6 caracteres.', 'erro')
            return render_template('cadastro.html')

        conn = get_db()
        existente = conn.execute('SELECT id FROM usuarios WHERE email=?', (email,)).fetchone()
        if existente:
            flash('Este e-mail já está cadastrado.', 'erro')
            conn.close()
            return render_template('cadastro.html')

        hash_senha = generate_password_hash(senha)
        conn.execute(
            'INSERT INTO usuarios (nome, email, senha, telefone) VALUES (?,?,?,?)',
            (nome, email, hash_senha, telefone)
        )
        conn.commit()
        conn.close()

        flash('Cadastro realizado! Faça login.', 'sucesso')
        return redirect(url_for('login'))

    return render_template('cadastro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        senha = request.form.get('senha', '')

        conn = get_db()
        usuario = conn.execute('SELECT * FROM usuarios WHERE email=?', (email,)).fetchone()
        conn.close()

        if usuario and check_password_hash(usuario['senha'], senha):
            session['usuario_id']   = usuario['id']
            session['usuario_nome'] = usuario['nome']
            flash(f'Bem-vindo, {usuario["nome"]}!', 'sucesso')
            return redirect(url_for('index'))

        flash('E-mail ou senha incorretos.', 'erro')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/perfil')
@login_required
def perfil():
    conn = get_db()
    usuario = conn.execute('SELECT * FROM usuarios WHERE id=?', (session['usuario_id'],)).fetchone()
    pedidos = conn.execute(
        'SELECT * FROM pedidos WHERE usuario_id=? ORDER BY criado_em DESC',
        (session['usuario_id'],)
    ).fetchall()
    conn.close()
    return render_template('perfil.html', usuario=usuario, pedidos=pedidos)


@app.route('/produto/<int:id>')
def produto(id):
    conn = get_db()
    p = conn.execute('SELECT * FROM produtos WHERE id=? AND ativo=1', (id,)).fetchone()
    conn.close()
    if not p:
        flash('Produto não encontrado.', 'erro')
        return redirect(url_for('index'))
    return render_template('produto.html', produto=p,
                           whatsapp=WHATSAPP_NUMBER, instagram=INSTAGRAM_USER)



#  ROTAS — API JSON 


@app.route('/api/produtos')
def api_produtos():
    categoria = request.args.get('categoria')
    conn = get_db()
    if categoria:
        rows = conn.execute(
            'SELECT * FROM produtos WHERE ativo=1 AND categoria=?', (categoria,)
        ).fetchall()
    else:
        rows = conn.execute('SELECT * FROM produtos WHERE ativo=1').fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


@app.route('/api/produto/<int:id>')
def api_produto(id):
    conn = get_db()
    p = conn.execute('SELECT * FROM produtos WHERE id=? AND ativo=1', (id,)).fetchone()
    conn.close()
    if not p:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    return jsonify(dict(p))


@app.route('/api/cadastro', methods=['POST'])
def api_cadastro():
    data     = request.get_json() or {}
    nome     = data.get('nome', '').strip()
    email    = data.get('email', '').strip().lower()
    senha    = data.get('senha', '')
    telefone = data.get('telefone', '').strip()

    if not nome or not email or not senha:
        return jsonify({'erro': 'Campos obrigatórios: nome, email, senha'}), 400
    if len(senha) < 6:
        return jsonify({'erro': 'Senha deve ter ao menos 6 caracteres'}), 400

    conn = get_db()
    if conn.execute('SELECT id FROM usuarios WHERE email=?', (email,)).fetchone():
        conn.close()
        return jsonify({'erro': 'E-mail já cadastrado'}), 409

    hash_senha = generate_password_hash(senha)
    conn.execute('INSERT INTO usuarios (nome, email, senha, telefone) VALUES (?,?,?,?)',
                 (nome, email, hash_senha, telefone))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Cadastro realizado com sucesso'}), 201


@app.route('/api/login', methods=['POST'])
def api_login():
    data  = request.get_json() or {}
    email = data.get('email', '').strip().lower()
    senha = data.get('senha', '')

    conn = get_db()
    usuario = conn.execute('SELECT * FROM usuarios WHERE email=?', (email,)).fetchone()
    conn.close()

    if usuario and check_password_hash(usuario['senha'], senha):
        session['usuario_id']   = usuario['id']
        session['usuario_nome'] = usuario['nome']
        return jsonify({'mensagem': 'Login realizado', 'nome': usuario['nome']})

    return jsonify({'erro': 'Credenciais inválidas'}), 401


@app.route('/api/pedido', methods=['POST'])
@login_required
def api_pedido():
    """
    Corpo esperado:
    {
      "itens": [
        {"produto_id": 1, "quantidade": 2},
        {"produto_id": 3, "quantidade": 1}
      ]
    }
    """
    data  = request.get_json() or {}
    itens = data.get('itens', [])

    if not itens:
        return jsonify({'erro': 'Envie pelo menos um item'}), 400

    conn  = get_db()
    total = 0.0
    detalhes = []

    for item in itens:
        prod = conn.execute(
            'SELECT * FROM produtos WHERE id=? AND ativo=1', (item['produto_id'],)
        ).fetchone()
        if not prod:
            conn.close()
            return jsonify({'erro': f'Produto {item["produto_id"]} não encontrado'}), 404
        if prod['estoque'] < item['quantidade']:
            conn.close()
            return jsonify({'erro': f'Estoque insuficiente para "{prod["nome"]}"'}), 400
        subtotal = prod['preco'] * item['quantidade']
        total   += subtotal
        detalhes.append({'prod': prod, 'qtd': item['quantidade'], 'preco': prod['preco']})

    cur = conn.execute(
        'INSERT INTO pedidos (usuario_id, total) VALUES (?,?)',
        (session['usuario_id'], total)
    )
    pedido_id = cur.lastrowid

    for d in detalhes:
        conn.execute(
            'INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unit) VALUES (?,?,?,?)',
            (pedido_id, d['prod']['id'], d['qtd'], d['preco'])
        )
        conn.execute(
            'UPDATE produtos SET estoque = estoque - ? WHERE id=?',
            (d['qtd'], d['prod']['id'])
        )

    conn.commit()
    conn.close()

    msg  = f'Olá! Meu pedido #{pedido_id} - Total: R${total:.2f}'
    link = f'https://wa.me/{WHATSAPP_NUMBER}?text={msg.replace(" ", "%20")}'

    return jsonify({'mensagem': 'Pedido criado', 'pedido_id': pedido_id,
                    'total': total, 'whatsapp_link': link}), 201


@app.route('/api/social')
def api_social():
    return jsonify({
        'whatsapp': f'https://wa.me/{WHATSAPP_NUMBER}',
        'instagram': f'https://instagram.com/{INSTAGRAM_USER}'
    })



#  Commando pra iniciar

if __name__ == '__main__':
    init_db()
    print('✅  Banco de dados iniciado.')
    print('🚀  Servidor rodando em http://localhost:5000')
    app.run(debug=True)
