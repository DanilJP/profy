import streamlit as st

st.title("🧩 Teste de Perfil Comportamental Completo")
st.write("Responda às perguntas abaixo para descobrir seu perfil comportamental. Seja honesto para obter um resultado mais preciso!")

st.header("Parte 1: Preferências de Trabalho")
q1 = st.radio("Você prefere trabalhar em equipe ou sozinho?", ["Equipe", "Sozinho"])
q2 = st.radio("Você prefere planejar tudo antes de agir ou improvisar no momento?", ["Planejar", "Improvisar"])
q3 = st.radio("Você gosta de assumir liderança em projetos?", ["Sim", "Não"])

st.header("Parte 2: Comunicação e Relações")
q4 = st.radio("Você é mais extrovertido ou introvertido?", ["Extrovertido", "Introvertido"])
q5 = st.radio("Você costuma expressar seus sentimentos abertamente?", ["Sim", "Não"])
q6 = st.radio("Você prefere conversas profundas ou bate-papo casual?", ["Conversas profundas", "Bate-papo casual"])

st.header("Parte 3: Reação ao Estresse e Decisão")
q7 = st.radio("Como você reage em situações de pressão?", ["Mantenho a calma", "Fico ansioso"])
q8 = st.radio("Você é mais racional ou emocional ao tomar decisões?", ["Racional", "Emocional"])
q9 = st.radio("Você prefere seguir regras ou quebrar padrões para inovar?", ["Seguir regras", "Quebrar padrões"])

st.header("Parte 4: Motivação e Valores")
q10 = st.radio("O que mais te motiva?", ["Reconhecimento", "Autonomia", "Segurança", "Desafio"])
q11 = st.radio("Você gosta de rotina ou prefere mudanças constantes?", ["Rotina", "Mudanças"])
q12 = st.radio("Você costuma ajudar os outros mesmo que isso tome seu tempo?", ["Sim", "Não"])

# Função para calcular o perfil
def calcular_perfil(respostas):
    pontuacao = {
        "Comunicativo": 0,
        "Independente": 0,
        "Líder": 0,
        "Planejador": 0,
        "Improvisador": 0,
        "Racional": 0,
        "Emocional": 0,
        "Calmo": 0,
        "Ansioso": 0,
        "Motivado_por_Reconhecimento": 0,
        "Motivado_por_Autonomia": 0,
        "Motivado_por_Seguranca": 0,
        "Motivado_por_Desafio": 0,
        "Ajudante": 0,
        "Mudancista": 0,
        "Rotineiro": 0
    }

    # Parte 1
    if respostas['q1'] == "Equipe":
        pontuacao["Comunicativo"] += 2
    else:
        pontuacao["Independente"] += 2

    if respostas['q2'] == "Planejar":
        pontuacao["Planejador"] += 2
    else:
        pontuacao["Improvisador"] += 2

    if respostas['q3'] == "Sim":
        pontuacao["Líder"] += 3

    # Parte 2
    if respostas['q4'] == "Extrovertido":
        pontuacao["Comunicativo"] += 2
    else:
        pontuacao["Independente"] += 2

    if respostas['q5'] == "Sim":
        pontuacao["Comunicativo"] += 1
    else:
        pontuacao["Independente"] += 1

    if respostas['q6'] == "Conversas profundas":
        pontuacao["Independente"] += 1
    else:
        pontuacao["Comunicativo"] += 1

    # Parte 3
    if respostas['q7'] == "Mantenho a calma":
        pontuacao["Calmo"] += 2
    else:
        pontuacao["Ansioso"] += 2

    if respostas['q8'] == "Racional":
        pontuacao["Racional"] += 2
    else:
        pontuacao["Emocional"] += 2

    if respostas['q9'] == "Seguir regras":
        pontuacao["Planejador"] += 1
    else:
        pontuacao["Improvisador"] += 1

    # Parte 4
    if respostas['q10'] == "Reconhecimento":
        pontuacao["Motivado_por_Reconhecimento"] += 3
    elif respostas['q10'] == "Autonomia":
        pontuacao["Motivado_por_Autonomia"] += 3
    elif respostas['q10'] == "Segurança":
        pontuacao["Motivado_por_Seguranca"] += 3
    else:
        pontuacao["Motivado_por_Desafio"] += 3

    if respostas['q11'] == "Rotina":
        pontuacao["Rotineiro"] += 2
    else:
        pontuacao["Mudancista"] += 2

    if respostas['q12'] == "Sim":
        pontuacao["Ajudante"] += 3

    return pontuacao

def interpretar_perfil(pontuacao):
    resultados = []

    if pontuacao["Comunicativo"] > pontuacao["Independente"]:
        resultados.append("Você tem um perfil **Comunicativo**: gosta de interação social, colaboração e é extrovertido.")
    else:
        resultados.append("Você tem um perfil **Independente**: prefere trabalhar sozinho, é introspectivo e reflexivo.")

    if pontuacao["Líder"] >= 3:
        resultados.append("Você demonstra características de **Líder**: gosta de tomar iniciativa e assumir responsabilidades.")

    if pontuacao["Planejador"] > pontuacao["Improvisador"]:
        resultados.append("Você é um **Planejador**: gosta de organização, estrutura e seguir regras.")
    else:
        resultados.append("Você é um **Improvisador**: prefere flexibilidade e inovação, quebra padrões.")

    if pontuacao["Calmo"] > pontuacao["Ansioso"]:
        resultados.append("Você lida bem com o estresse e é uma pessoa calma.")
    else:
        resultados.append("Você tende a sentir ansiedade em situações de pressão.")

    if pontuacao["Racional"] > pontuacao["Emocional"]:
        resultados.append("Você toma decisões mais com base na razão e lógica.")
    else:
        resultados.append("Você é uma pessoa mais guiada pelas emoções.")

    if pontuacao["Motivado_por_Reconhecimento"] > 0:
        resultados.append("Você é motivado pelo reconhecimento e aprecia ser valorizado pelo seu trabalho.")
    if pontuacao["Motivado_por_Autonomia"] > 0:
        resultados.append("Você valoriza muito a autonomia e liberdade para fazer seu trabalho.")
    if pontuacao["Motivado_por_Seguranca"] > 0:
        resultados.append("Você busca segurança e estabilidade em sua vida e carreira.")
    if pontuacao["Motivado_por_Desafio"] > 0:
        resultados.append("Você gosta de desafios e de sair da zona de conforto.")

    if pontuacao["Rotineiro"] > pontuacao["Mudancista"]:
        resultados.append("Você prefere a rotina e ambientes estáveis.")
    else:
        resultados.append("Você gosta de mudanças e novidades constantes.")

    if pontuacao["Ajudante"] > 0:
        resultados.append("Você é uma pessoa altruísta que gosta de ajudar os outros.")

    return resultados

# Botão para calcular o resultado
if st.button("Ver resultado"):
    respostas = {
        'q1': q1,
        'q2': q2,
        'q3': q3,
        'q4': q4,
        'q5': q5,
        'q6': q6,
        'q7': q7,
        'q8': q8,
        'q9': q9,
        'q10': q10,
        'q11': q11,
        'q12': q12
    }

    pontuacao = calcular_perfil(respostas)
    resultados = interpretar_perfil(pontuacao)

    st.subheader("📋 Seu Perfil Comportamental:")
    for r in resultados:
        st.markdown(f"- {r}")

    # Visualização simples com barras
    import matplotlib.pyplot as plt

    categorias = ["Comunicativo", "Independente", "Líder", "Planejador", "Improvisador",
                  "Calmo", "Ansioso", "Racional", "Emocional",
                  "Reconhecimento", "Autonomia", "Segurança", "Desafio",
                  "Rotineiro", "Mudancista", "Ajudante"]

    valores = [
        pontuacao["Comunicativo"], pontuacao["Independente"], pontuacao["Líder"],
        pontuacao["Planejador"], pontuacao["Improvisador"],
        pontuacao["Calmo"], pontuacao["Ansioso"], pontuacao["Racional"], pontuacao["Emocional"],
        pontuacao["Motivado_por_Reconhecimento"], pontuacao["Motivado_por_Autonomia"],
        pontuacao["Motivado_por_Seguranca"], pontuacao["Motivado_por_Desafio"],
        pontuacao["Rotineiro"], pontuacao["Mudancista"], pontuacao["Ajudante"]
    ]

    fig, ax = plt.subplots(figsize=(10,6))
    ax.barh(categorias, valores, color='skyblue')
    ax.set_xlabel("Pontuação")
    ax.set_title("Distribuição do seu Perfil Comportamental")
    st.pyplot(fig)
