import streamlit as st

# Página principal
st.set_page_config(page_title="Quiz Segurança Digital", layout="centered")

st.title("🔐 Quiz sobre Segurança Digital")

# Armazenamento temporário
if "cadastro_ok" not in st.session_state:
    st.session_state.cadastro_ok = False
if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0
if "etapa" not in st.session_state:
    st.session_state.etapa = 0
if "nivel" not in st.session_state:
    st.session_state.nivel = "Iniciante"

# Banco de perguntas por nível
perguntas_por_nivel = {
    "Iniciante": [
        {
            "pergunta": "O que é uma senha segura?",
            "alternativas": {
                "A": "Senha com letras, números e símbolos",
                "B": "Senha fácil como 1234",
                "C": "Mesma senha em tudo",
                "D": "Nome da família"
            },
            "correta": "A"
        },
        {
            "pergunta": "Por que não clicar em links de desconhecidos?",
            "alternativas": {
                "A": "Vai travar o celular",
                "B": "Pode roubar seus dados",
                "C": "Gasta internet",
                "D": "Deixa lento"
            },
            "correta": "B"
        }
    ],
    "Intermediário": [
        {
            "pergunta": "O que significa autenticação em dois fatores (2FA)?",
            "alternativas": {
                "A": "Acesso com nome e CPF",
                "B": "Verificação com dois dispositivos",
                "C": "Confirmação dupla para login",
                "D": "Senha digitada duas vezes"
            },
            "correta": "C"
        },
        {
            "pergunta": "Como evitar golpes de phishing?",
            "alternativas": {
                "A": "Clicando rápido nos links",
                "B": "Desconfiando de e-mails suspeitos",
                "C": "Reenviando para amigos",
                "D": "Usando a mesma senha em tudo"
            },
            "correta": "B"
        }
    ],
    "Avançado": [
        {
            "pergunta": "O que é um certificado digital SSL?",
            "alternativas": {
                "A": "Protocolo de login automático",
                "B": "Sistema de antivírus",
                "C": "Garantia de conexão segura via HTTPS",
                "D": "Extensão de navegador"
            },
            "correta": "C"
        },
        {
            "pergunta": "Qual a função de um firewall?",
            "alternativas": {
                "A": "Aumentar a velocidade da internet",
                "B": "Filtrar tráfego de rede e bloquear acessos maliciosos",
                "C": "Melhorar a imagem de vídeo",
                "D": "Acessar sites automaticamente"
            },
            "correta": "B"
        }
    ]
}

# Cadastro
if not st.session_state.cadastro_ok:
    st.subheader("📋 Cadastro do Participante")
    with st.form("formulario_cadastro"):
        nome = st.text_input("Seu nome")
        idade = st.number_input("Sua idade", min_value=5, max_value=120, step=1)
        nivel = st.selectbox("Seu nível de conhecimento sobre segurança digital", ["Iniciante", "Intermediário", "Avançado"])
        consentimento = st.checkbox("Autorizo o uso dos meus dados para fins educacionais (LGPD)")
        enviar = st.form_submit_button("Começar Quiz")

        if enviar:
            if not consentimento:
                st.warning("Você precisa aceitar o uso de dados para continuar.")
            elif nome.strip() == "":
                st.warning("Por favor, digite seu nome.")
            else:
                st.session_state.cadastro_ok = True
                st.session_state.nome = nome
                st.session_state.nivel = nivel
                st.session_state.pontuacao = 0
                st.session_state.etapa = 0
                st.success("Cadastro concluído! Boa sorte no quiz 🚀")

# Carregar perguntas do nível escolhido
nivel = st.session_state.nivel
perguntas = perguntas_por_nivel[nivel]

# Quiz
if st.session_state.cadastro_ok and st.session_state.etapa < len(perguntas):
    atual = perguntas[st.session_state.etapa]
    st.subheader(atual["pergunta"])
    escolha = st.radio("Escolha uma alternativa:", list(atual["alternativas"].keys()), format_func=lambda x: f"{x}) {atual['alternativas'][x]}")
    if st.button("Responder"):
        if escolha == atual["correta"]:
            st.session_state.pontuacao += 1
            st.success("✅ Resposta correta!")
        else:
            st.error(f"❌ Incorreta. A correta era ({atual['correta']}) {atual['alternativas'][atual['correta']]}")
        st.session_state.etapa += 1
        st.rerun()

# Resultado
elif st.session_state.cadastro_ok and st.session_state.etapa >= len(perguntas):
    st.success(f"🎉 {st.session_state.nome}, você finalizou o quiz!")
    st.write(f"Você acertou {st.session_state.pontuacao} de {len(perguntas)} perguntas.")

    if st.button("Refazer o quiz"):
        st.session_state.cadastro_ok = False
        st.session_state.etapa = 0
        st.session_state.pontuacao = 0
        st.rerun()
