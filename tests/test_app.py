import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Teste 1: Verifica se a página inicial retorna o status code 200 (OK)
def test_pagina_inicial_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

# Teste 2: Verifica se a página inicial contém o texto esperado
def test_conteudo_pagina_inicial(client):
    response = client.get('/')
    assert b"Projeto DevOps" in response.data

# Teste 3: Verifica se a página de "health check" está acessível
def test_health_check_status_code(client):
    response = client.get('/health')
    assert response.status_code == 200

# Teste 4: Verifica se a página de "health check" retorna o JSON correto
def test_conteudo_health_check(client):
    response = client.get('/health')
    assert response.json == {"status": "ok"}

# Teste 5: Verifica se uma página que não existe retorna o erro 404
def test_pagina_nao_encontrada(client):
    response = client.get('/uma-pagina-qualquer-que-nao-existe')
    assert response.status_code == 404