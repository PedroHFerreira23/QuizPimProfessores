import streamlit as st


st.set_page_config(page_title="Quiz Segurança Digital", layout="centered")

st.title("🔐 Quiz sobre Segurança Digital")


if "cadastro_ok" not in st.session_state:
    st.session_state.cadastro_ok = False
if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0
if "etapa" not in st.session_state:
    st.session_state.etapa = 0


perguntas = [
    {
        "pergunta": "1. O que é uma senha segura?",
        "alternativas": {
            "A": "Senha com letras, números e símbolos diferentes",
            "B": "Senha fácil como 1234",
            "C": "Senha igual em todas as contas",
            "D": "Nome da minha família"
        },
        "correta": "A"
    },
    {
        "pergunta": "2. Por que não devemos clicar em links de e-mails ou mensagens de desconhecidos?",
        "alternativas": {
            "A": "Porque o celular vai travar",
            "B": "Porque pode ser perigoso e roubar seus dados",
            "C": "Porque vai gastar muita internet",
            "D": "Porque o computador pode ficar lento"
        },
        "correta": "B"
    },
    {
        "pergunta": "3. O que fazer se uma mensagem pedir seus dados bancários?",
        "alternativas": {
            "A": "Compartilhar com amigos",
            "B": "Ignorar e apagar a mensagem",
            "C": "Postar nas redes sociais",
            "D": "Responder com os dados"
        },
        "correta": "B"
    },
    {
        "pergunta": "4. Qual é a função de um antivírus?",
        "alternativas": {
            "A": "Proteger contra vírus e ameaças",
            "B": "Apagar arquivos antigos",
            "C": "Ajudar a encontrar senhas esquecidas",
            "D": "Deixar vídeos mais rápidos"
        },
        "correta": "A"
    },
    {
        "pergunta": "5. Por que não devemos compartilhar senhas?",
        "alternativas": {
            "A": "Outras pessoas podem acessar sua conta",
            "B": "Pode gastar seu saldo",
            "C": "A senha pode estragar",
            "D": "A pessoa pode esquecer"
        },
        "correta": "A"
    },
    {
        "pergunta": "6. O que é um golpe digital?",
        "alternativas": {
            "A": "Uma brincadeira online",
            "B": "Um vídeo engraçado",
            "C": "Forma de enganar para roubar dados ou dinheiro",
            "D": "Uma promoção verdadeira"
        },
        "correta": "C"
    },
    {
        "pergunta": "7. O que fazer ao usar um computador público?",
        "alternativas": {
            "A": "Instalar apps pessoais",
            "B": "Usar com cuidado e sair da conta depois",
            "C": "Salvar senhas no navegador",
            "D": "Deixar conta conectada"
        },
        "correta": "B"
    },
    {
        "pergunta": "8. O que é uma rede Wi-Fi aberta?",
        "alternativas": {
            "A": "Rede segura e protegida",
            "B": "Internet mais rápida",
            "C": "Rede exclusiva de bancos",
            "D": "Rede onde qualquer um pode acessar"
        },
        "correta": "D"
    },
    {
        "pergunta": "9. Como saber se um site é seguro para compras?",
        "alternativas": {
            "A": "Muitas cores chamativas",
            "B": "Pede dados antes de mostrar produtos",
            "C": "Preço muito barato",
            "D": "Começa com 'https://' e tem um cadeado"
        },
        "correta": "D"
    },
    {
        "pergunta": "10. Se alguém pede dinheiro no WhatsApp dizendo ser parente?",
        "alternativas": {
            "A": "Ignorar e bloquear",
            "B": "Confirmar com a pessoa por telefone",
            "C": "Transferir logo",
            "D": "Mandar a mensagem para outros"
        },
        "correta": "B"
    }
]


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
                st.session_state.pontuacao = 0
                st.session_state.etapa = 0
                st.success("Cadastro concluído! Boa sorte no quiz 🚀")


elif st.session_state.etapa < len(perguntas):
    atual = perguntas[st.session_state.etapa]
    st.subheader(atual["pergunta"])
    escolha = st.radio("Escolha uma alternativa:", list(atual["alternativas"].keys()), format_func=lambda x: f"{x}) {atual['alternativas'][x]}")
    if st.button("Responder"):
        if escolha == atual["correta"]:
            st.session_state.pontuacao += 1
            st.success("✅ Resposta correta!")
        else:
            st.error(f"❌ Resposta incorreta. A correta era ({atual['correta']}) {atual['alternativas'][atual['correta']]}")
        st.session_state.etapa += 1
        st.rerun()


else:
    st.success(f"🎉 Parabéns, {st.session_state.nome}! Você concluiu o quiz.")
    st.write(f"Sua pontuação foi: **{st.session_state.pontuacao} de {len(perguntas)}**")
    if st.button("Refazer o quiz"):
        st.session_state.cadastro_ok = False
        st.session_state.etapa = 0
        st.session_state.pontuacao = 0
        st.rerun()

