import streamlit as st #import

st.set_page_config(page_title="Quiz Segurança Digital", layout="centered")
st.title("🔐 Quiz sobre Segurança Digital")

if "cadastro_ok" not in st.session_state:
    st.session_state.cadastro_ok = False
if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0
if "etapa" not in st.session_state:
    st.session_state.etapa = 0
if "nivel" not in st.session_state:
    st.session_state.nivel = "Iniciante"

perguntas_por_nivel = {
    "Iniciante": [
        {"pergunta": "O que é uma senha segura?", "alternativas": {"A": "Senha com letras, números e símbolos", "B": "Senha 1234", "C": "Mesma senha em tudo", "D": "Nome da família"}, "correta": "A"},
        {"pergunta": "Por que não clicar em links de desconhecidos?", "alternativas": {"A": "Vai travar", "B": "Pode roubar seus dados", "C": "Gasta internet", "D": "Deixa lento"}, "correta": "B"},
        {"pergunta": "O que fazer ao receber e-mail estranho?", "alternativas": {"A": "Abrir logo", "B": "Reenviar para colegas", "C": "Ignorar e deletar", "D": "Responder com dados"}, "correta": "C"},
        {"pergunta": "Onde não se deve colocar sua senha?", "alternativas": {"A": "Sites confiáveis", "B": "Papel guardado", "C": "Notas do celular", "D": "Sites duvidosos"}, "correta": "D"},
        {"pergunta": "O que é um antivírus?", "alternativas": {"A": "Programa de edição", "B": "App de música", "C": "Proteção contra vírus", "D": "Serviço de nuvem"}, "correta": "C"},
        {"pergunta": "Quando desconfiar de uma promoção online?", "alternativas": {"A": "Quando exigir seus dados bancários", "B": "Quando for no Instagram", "C": "Quando for de loja conhecida", "D": "Quando for domingo"}, "correta": "A"},
        {"pergunta": "Como proteger seu celular?", "alternativas": {"A": "Sem senha", "B": "Com senha forte", "C": "Com modo avião", "D": "Com brilho no máximo"}, "correta": "B"},
        {"pergunta": "Qual dessas é uma atitude segura?", "alternativas": {"A": "Usar mesma senha", "B": "Anotar a senha num caderno", "C": "Usar autenticação em 2 fatores", "D": "Ignorar atualizações"}, "correta": "C"},
        {"pergunta": "O que é phishing?", "alternativas": {"A": "Jogo online", "B": "Golpe para roubar dados", "C": "Tipo de Wi-Fi", "D": "Antivírus"}, "correta": "B"},
        {"pergunta": "Quando atualizar seus apps?", "alternativas": {"A": "Nunca", "B": "Apenas no Wi-Fi", "C": "Quando disponível", "D": "Quando pedir senha"}, "correta": "C"}
    ],
    "Intermediário": [
        {"pergunta": "O que é autenticação em dois fatores (2FA)?", "alternativas": {"A": "Login com dois nomes", "B": "Confirmação dupla", "C": "Senha digitada duas vezes", "D": "Acesso com CPF"}, "correta": "B"},
        {"pergunta": "Como evitar phishing?", "alternativas": {"A": "Clicando rápido", "B": "Respondendo e-mails", "C": "Ignorando e-mails suspeitos", "D": "Reenviando promoções"}, "correta": "C"},
        {"pergunta": "O que são dados sensíveis?", "alternativas": {"A": "Endereço de IP", "B": "Nome do pet", "C": "Religião, saúde, biometria", "D": "Nome da escola"}, "correta": "C"},
        {"pergunta": "O que é um software malicioso?", "alternativas": {"A": "Software pago", "B": "App do governo", "C": "Vírus ou spyware", "D": "Programa em teste"}, "correta": "C"},
        {"pergunta": "Qual site é mais seguro?", "alternativas": {"A": "http://", "B": "https:// com cadeado", "C": "Qualquer um com .com", "D": "Links curtos"}, "correta": "B"},
        {"pergunta": "O que fazer em redes Wi-Fi públicas?", "alternativas": {"A": "Acessar banco", "B": "Evitar logins importantes", "C": "Deixar senhas salvas", "D": "Assistir filmes"}, "correta": "B"},
        {"pergunta": "Como guardar senhas?", "alternativas": {"A": "Memorizar tudo", "B": "Usar o mesmo código", "C": "Salvar no navegador", "D": "Usar gerenciador de senhas"}, "correta": "D"},
        {"pergunta": "LGPD protege o quê?", "alternativas": {"A": "Bens físicos", "B": "Direito autoral", "C": "Dados pessoais", "D": "Carros"}, "correta": "C"},
        {"pergunta": "O que é backup?", "alternativas": {"A": "Atualização de sistema", "B": "Cópia de segurança", "C": "Antivírus", "D": "Permissão de acesso"}, "correta": "B"},
        {"pergunta": "Como criar uma senha forte?", "alternativas": {"A": "Usar nome + número", "B": "Palavra fácil", "C": "Misturar letras, símbolos e números", "D": "Data de nascimento"}, "correta": "C"}
    ],
    "Avançado": [
        {"pergunta": "O que é SSL?", "alternativas": {"A": "Login automático", "B": "Protocolo de segurança HTTPS", "C": "App de banco", "D": "Ferramenta de backup"}, "correta": "B"},
        {"pergunta": "Função do firewall?", "alternativas": {"A": "Proteger contra vírus", "B": "Filtrar e bloquear tráfego malicioso", "C": "Salvar arquivos", "D": "Gerar logins"}, "correta": "B"},
        {"pergunta": "Ataque DDoS significa?", "alternativas": {"A": "Acesso indevido", "B": "Ataque de negação de serviço", "C": "Antivírus moderno", "D": "Malware do Google"}, "correta": "B"},
        {"pergunta": "O que é hashing?", "alternativas": {"A": "Criptografia reversível", "B": "Método de login", "C": "Transformar dados em código fixo", "D": "Trocar senha automaticamente"}, "correta": "C"},
        {"pergunta": "VPN serve para quê?", "alternativas": {"A": "Conectar redes sociais", "B": "Ocultar IP e navegar com segurança", "C": "Aumentar velocidade", "D": "Desativar antivírus"}, "correta": "B"},
        {"pergunta": "Engenharia social é:", "alternativas": {"A": "Estudo de redes", "B": "Engenharia de sistemas", "C": "Manipulação para obter dados", "D": "Criação de perfis falsos"}, "correta": "C"},
        {"pergunta": "O que é autenticação biométrica?", "alternativas": {"A": "Login com código", "B": "Senha numérica", "C": "Reconhecimento físico", "D": "Verificação de CPF"}, "correta": "C"},
        {"pergunta": "LGPD exige o quê?", "alternativas": {"A": "Consentimento para tratar dados", "B": "Senha de 8 dígitos", "C": "Backup diário", "D": "Desbloqueio de redes"}, "correta": "A"},
        {"pergunta": "Como saber se um app é seguro?", "alternativas": {"A": "Se for novo", "B": "Se tiver avaliação ruim", "C": "Se for da loja oficial e bem avaliado", "D": "Se for gratuito"}, "correta": "C"},
        {"pergunta": "O que é autenticação multifator?", "alternativas": {"A": "Senha e CPF", "B": "Senha + outro método (ex: SMS)", "C": "Login duplicado", "D": "Cadastro múltiplo"}, "correta": "B"}
    ]
}


if not st.session_state.cadastro_ok:
    st.subheader("📋 Cadastro do Participante")
    with st.form("formulario_cadastro"):
        nome = st.text_input("Seu nome")
        idade = st.number_input("Sua idade", min_value=5, max_value=120, step=1)
        nivel = st.selectbox("Seu nível de conhecimento", ["Iniciante", "Intermediário", "Avançado"])
        consentimento = st.checkbox("Autorizo o uso dos meus dados para fins educacionais conforme a Lei Geral e Proteção de Dados (LGPD)")
        enviar = st.form_submit_button("Começar Quiz")

        if enviar and nome.strip() != "" and consentimento:
            st.session_state.nome = nome
            st.session_state.nivel = nivel
            st.session_state.etapa = 0
            st.session_state.pontuacao = 0
            st.session_state.cadastro_ok = True
            st.success("Cadastro realizado com sucesso!")
        elif not consentimento:
            st.warning("Você precisa aceitar a LGPD para continuar.")
        elif nome.strip() == "":
            st.warning("Informe seu nome.")


if st.session_state.cadastro_ok:
    nivel = st.session_state.nivel
    perguntas = perguntas_por_nivel[nivel]
    etapa = st.session_state.etapa

    if etapa < len(perguntas):
        pergunta = perguntas[etapa]
        st.subheader(f"Pergunta {etapa + 1} de {len(perguntas)}")
        st.write(pergunta["pergunta"])
        resposta = st.radio("Escolha:", list(pergunta["alternativas"].keys()), format_func=lambda x: f"{x}) {pergunta['alternativas'][x]}")
        if st.button("Responder"):
            if resposta == pergunta["correta"]:
                st.success("✅ Resposta correta!")
                st.session_state.pontuacao += 1
            else:
                st.error(f"❌ Errado! A resposta correta era: {pergunta['correta']}) {pergunta['alternativas'][pergunta['correta']]}")
            st.session_state.etapa += 1
            st.rerun()
    else:
        st.success(f"🎉 {st.session_state.nome}, você finalizou o quiz!")
        st.write(f"Você acertou {st.session_state.pontuacao} de {len(perguntas)} perguntas.")

        if st.button("Refazer o quiz"):
            st.session_state.cadastro_ok = False
            st.session_state.etapa = 0
            st.session_state.pontuacao = 0
            st.rerun()
