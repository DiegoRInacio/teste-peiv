# Teste PEI V

### Esta é a branch principal
  - Aqui quem fez o commit foi o Diego

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