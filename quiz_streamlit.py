
import streamlit as st

st.set_page_config(page_title="Quiz de Segurança Digital", layout="centered")
st.title("🛡️ Quiz de Segurança Digital")

perguntas = [
    ("O que é uma senha segura?",
     {"A": "Uma senha com letras, números e símbolos diferentes",
      "B": "Uma senha fácil de lembrar, como 1234",
      "C": "Uma senha igual para todas as contas",
      "D": "Uma senha com nome da minha família"}, "A"),
    ("Por que não devemos clicar em links de e-mails ou mensagens de desconhecidos?",
     {"A": "Porque o celular vai travar",
      "B": "Porque pode ser perigoso e roubar seus dados",
      "C": "Porque vai gastar muita internet",
      "D": "Porque o computador pode ficar lento"}, "B"),
    ("O que fazer se uma mensagem pedir seus dados bancários?",
     {"A": "Compartilhar com amigos",
      "B": "Ignorar e apagar a mensagem",
      "C": "Postar nas redes sociais",
      "D": "Responder com os dados"}, "B"),
    ("Qual é a função de um antivírus?",
     {"A": "Proteger contra vírus e ameaças",
      "B": "Apagar arquivos antigos",
      "C": "Ajudar a encontrar senhas esquecidas",
      "D": "Deixar vídeos mais rápidos"}, "A")
]

pontuacao = 0
for i, (pergunta, alternativas, correta) in enumerate(perguntas):
    st.subheader(f"{i+1}. {pergunta}")
    resposta = st.radio("Escolha uma opção:", list(alternativas.values()), key=i)
    if resposta == alternativas[correta]:
        pontuacao += 1

if st.button("Finalizar Quiz"):
    st.success(f"✅ Você acertou {pontuacao} de {len(perguntas)} perguntas!")
