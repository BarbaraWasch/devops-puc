import pytest
from app import create_app # Importamos a função que cria nossa aplicação

# Fixture para criar um cliente de teste para nossa aplicação
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# --- Nossos 5 Testes Unitários ---

# Teste 1: Verifica se a página inicial retorna o status code 200 (OK)
def test_pagina_inicial_status_code(client):
    """Verifica se a página inicial está acessível."""
    response = client.get('/')
    assert response.status_code == 200

# Teste 2: Verifica se a página inicial contém o texto esperado
def test_conteudo_pagina_inicial(client):
    """Verifica se o conteúdo da página inicial está correto."""
    response = client.get('/')
    assert b"Projeto DevOps" in response.data
    assert b"disciplina" in response.data

# Teste 3: Verifica se a página de "health check" retorna o status code 200 (OK)
def test_health_check_status_code(client):
    """Verifica se a página de health check está acessível."""
    response = client.get('/health')
    assert response.status_code == 200

# Teste 4: Verifica se a página de "health check" retorna o JSON correto
def test_conteudo_health_check(client):
    """Verifica se o JSON da página de health check está correto."""
    response = client.get('/health')
    assert response.json == {"status": "ok"}

# Teste 5: Verifica se uma página que não existe retorna o erro 404 (Not Found)
def test_pagina_nao_encontrada(client):
    """Verifica o comportamento para uma rota inexistente."""
    response = client.get('/pagina-que-nao-existe')
    assert response.status_code == 404