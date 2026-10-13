import streamlit as st
from google import genai
import os

# Configuration de la page
st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🤖",
    layout="centered"
)

# Initialiser le client Gemini une seule fois
@st.cache_resource
def get_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    return genai.Client(api_key=api_key)

client = get_client()

# Instructions de l'assistant
SYSTEM_PROMPT = """
Tu es un assistant IA spécialisé dans la formation professionnelle
et l'aide aux utilisateurs.

Réponds en français par défaut, avec un ton professionnel,
pédagogique et bienveillant.

Explique les notions clairement, utilise des exemples pratiques
et n'invente pas de procédures internes ou d'informations incertaines.
Si tu ne connais pas une réponse, indique-le clairement.
"""

# Interface
st.title("🤖 AI Learning Assistant")
st.caption("Votre assistant IA pour apprendre et progresser.")

# Historique conservé pendant la session Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Bouton pour démarrer une nouvelle conversation
if st.button("Nouvelle conversation"):
    st.session_state.messages = []
    st.rerun()

# Afficher les anciens messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Champ de saisie
question = st.chat_input("Posez votre question...")

if question:
    # Afficher et enregistrer la question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Construire l'historique pour Gemini
    historique = []

    for message in st.session_state.messages[:-1]:
        role = "user" if message["role"] == "user" else "model"
        historique.append({
            "role": role,
            "parts": [{"text": message["content"]}]
        })

    historique.append({
        "role": "user",
        "parts": [{"text": question}]
    })

    try:
        with st.chat_message("assistant"):
            with st.spinner("L'assistant réfléchit..."):
                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=historique,
                    config={"system_instruction": SYSTEM_PROMPT}
                )

                answer = response.text

                if not answer:
                    answer = "Je n'ai pas pu générer de réponse textuelle."

                st.markdown(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        st.error(
            f"Erreur : {type(e).__name__} — {str(e)}"
        )
