# Teste PEI V

### Esta é a branch principal
  - Aqui quem fez o commit foi o __Diego__
  - Novo

### Agregação do __Vinicius__
Teste do Git
from os import system, name
from stdiomask import getpass
from time import sleep
from adm import usuario_adm, senha_adm

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css'rel='stylesheet'> 
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">


    <title>Marketplace de Produtos</title>
</head>
<body>
    <main class="container">
        <form><!--aqui vai ser a parte que solicita o login e senha-->
            <h1>login</h1>
            <div class="input-box">
                <input placeholder="Usuario" type="email">
                <i class='bx bxs-user' ></i><!--icone de usuario-->
            </div>
            <div class="input-box">
                <input placeholder="Senha" type="password">
                <i class='bx bxs-lock-alt' ></i><!--icone de senha-->
            </div>

            <div class="lembrar-senha"><!--aqui vai ser o botao de lembrar a senha-->
                <label>
                    <input type="checkbox">
                    Lembrar a minha senha
                </label>
                <a href="#">esqueceu a senha?</a><!--aqui vou criar um link para levar em algum lugar--> 
            </div>
            <button type="submit">login</button>
            <div>
                <p>Não tem uma conta? <a href="#">cadastre-se</a></p>
            </div>
        </form>

    </main>
</body>
</html>

### Agragação do __Fábio__
 - como sou um cara humilde e não quero humilhar "uzamigu" tomae
print("Hello, World!")


import streamlit as st

# Configuração da página
st.set_page_config(page_title="Cadastro de Usuário", layout="centered")

# Título
st.title("📋 Cadastro de Usuário")

# Formulário de cadastro
with st.form("form_cadastro"):
    nome = st.text_input("Nome completo")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    confirmar = st.text_input("Confirmar senha", type="password")
    enviar = st.form_submit_button("Cadastrar")

    # Validação
    if enviar:
        if not nome or not email or not senha or not confirmar:
            st.warning("⚠️ Todos os campos são obrigatórios.")
        elif senha != confirmar:
            st.error("❌ As senhas não coincidem.")
        else:
            st.success(f"✅ Usuário '{nome}' cadastrado com sucesso!")
            # Aqui você pode adicionar lógica para salvar os dados
            # Exemplo: salvar em banco de dados ou arquivo

é muita humilhacao 
