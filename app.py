"""
LAWBot - Streamlit UI
Legal AI Assistant Interface
"""

import streamlit as st
from lawbot_engine import get_nyaysetu
from deep_translator import GoogleTranslator

# Speech libraries
import speech_recognition as sr
from gtts import gTTS
import tempfile


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="LAWBot - A Multilingual Legal Rights Chatbot for Rural India",
    page_icon="⚖️",
    layout="wide"
)

# ---------------- LAW THEME ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0f3460 100%);
    color:#e0e0e0;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#0f1419 0%,#1a1f26 100%);
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3{
    color:#f59e0b !important;
}

h1{
    color:#f59e0b !important;
    text-align:center;
}

.stButton>button{
    background:#1f2937;
    color:white;
    border:1px solid #f59e0b;
    border-radius:10px;
}

.stChatInput input{
    background:#1f2937 !important;
    color:white !important;
    border:2px solid #f59e0b !important;
    border-radius:25px !important;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SESSION STATE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- LOAD MODEL ----------------
if "nyaysetu" not in st.session_state:
    with st.spinner("Loading LAWBot AI Legal Assistant..."):
        st.session_state.nyaysetu = get_nyaysetu()


# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.markdown("## ⚖ LAWBot")

    st.markdown("### Multilingual Legal Rights Chatbot for Rural India")

    st.markdown("""
LAWBot helps rural citizens understand **Indian laws, rights and legal procedures**.
""")

    st.markdown("### Example Questions")

    st.markdown("""
• Fundamental Rights in India  
• IPC Section 420  
• How to file FIR  
• Property registration  
• Consumer complaint  
""")

    if st.button("🗑 Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

    st.markdown("---")

    st.markdown("### 🚨 Emergency Legal Help")

    st.markdown("""
📞 Police Emergency: **100**

👩 Women Helpline: **1091**

👶 Child Helpline: **1098**

⚖ Legal Aid (Free): **1516**

🚑 Ambulance: **108**
""")


# ---------------- TITLE ----------------
st.markdown(
"<h1>⚖ LAWBot - Multilingual Legal Rights Chatbot for Rural India</h1>",
unsafe_allow_html=True
)

st.markdown(
"<p style='text-align:center;color:#f59e0b'>AI Legal Rights Assistant for Rural India</p>",
unsafe_allow_html=True
)


# ---------------- LANGUAGE ----------------
language = st.selectbox(
    "🌐 Select Language",
    ["English","Hindi","Telugu","Tamil","Kannada","Malayalam","Marathi","Bengali","Gujarati","Punjabi"]
)

lang_map = {
    "English":"en",
    "Hindi":"hi",
    "Telugu":"te",
    "Tamil":"ta",
    "Kannada":"kn",
    "Malayalam":"ml",
    "Marathi":"mr",
    "Bengali":"bn",
    "Gujarati":"gu",
    "Punjabi":"pa"
}


# ---------------- QUICK QUESTIONS ----------------
st.subheader("⚡ Quick Legal Questions")

quick_questions = [
    "How to file FIR in India?",
    "What are fundamental rights in India?",
    "Property registration process in India",
    "How to file consumer complaint?",
    "Women rights against domestic violence"
]

cols = st.columns(len(quick_questions))
quick_selected=None

for i,q in enumerate(quick_questions):
    if cols[i].button(q):
        quick_selected=q


# ---------------- VOICE INPUT ----------------
voice_input=None

st.subheader("🎤 Voice Assistant")

if st.button("🎙 Speak Question"):

    recognizer=sr.Recognizer()

    try:
        with sr.Microphone() as source:
            st.info("Listening...")
            audio=recognizer.listen(source)

        voice_input=recognizer.recognize_google(audio)
        st.success(f"You said: {voice_input}")

    except:
        st.error("Speech recognition failed")


# ---------------- CHAT DISPLAY ----------------
for sender,msg in st.session_state.chat_history:

    if sender=="User":
        with st.chat_message("user"):
            st.write(msg)

    else:
        with st.chat_message("assistant"):
            st.write(msg)


# ---------------- CHAT INPUT ----------------
placeholders={
"English":"Ask your legal question...",
"Hindi":"यहाँ अपना प्रश्न पूछें...",
"Telugu":"మీ ప్రశ్న అడగండి...",
"Tamil":"உங்கள் கேள்வியை கேளுங்கள்...",
"Kannada":"ನಿಮ್ಮ ಪ್ರಶ್ನೆ ಕೇಳಿ...",
"Malayalam":"നിങ്ങളുടെ ചോദ്യം ചോദിക്കുക...",
"Marathi":"तुमचा प्रश्न विचारा...",
"Bengali":"আপনার প্রশ্ন লিখুন...",
"Gujarati":"તમારો પ્રશ્ન પૂછો...",
"Punjabi":"ਆਪਣਾ ਸਵਾਲ ਪੁੱਛੋ..."
}

text_input=st.chat_input(placeholders[language])


# ---------------- SELECT INPUT ----------------
user_input=None

if quick_selected:
    user_input=quick_selected
elif voice_input:
    user_input=voice_input
elif text_input:
    user_input=text_input


# ---------------- PROCESS QUERY ----------------
if user_input:

    original_input=user_input
    translated_input=user_input

    if language!="English":
        try:
            translated_input=GoogleTranslator(source='auto',target='en').translate(user_input)
        except:
            translated_input=user_input

    st.session_state.chat_history.append(("User",original_input))

    with st.spinner("LAWBot is thinking..."):

        try:
            answer=st.session_state.nyaysetu.ask(translated_input,[])

            if language!="English":
                try:
                    answer=GoogleTranslator(source='en',target=lang_map[language]).translate(answer)
                except:
                    pass

            st.session_state.chat_history.append(("LAWBot",answer))

        except Exception as e:
            st.error(str(e))
            st.session_state.chat_history.pop()

    st.rerun()


# ---------------- SPEAK ANSWER BUTTON ----------------
if st.session_state.chat_history and st.session_state.chat_history[-1][0]=="LAWBot":

    answer_text=st.session_state.chat_history[-1][1]

    if st.button("🔊 Listen Answer"):

        try:
            tts=gTTS(text=answer_text,lang=lang_map[language])

            with tempfile.NamedTemporaryFile(delete=False,suffix=".mp3") as fp:
                tts.save(fp.name)

                audio=open(fp.name,"rb")
                st.audio(audio.read(),format="audio/mp3")

        except:
            st.error("Audio playback failed")


# ---------------- FOOTER ----------------
st.markdown("---")

st.caption(
"LAWBot — Multilingual Legal Rights Chatbot for Rural India | Built using Streamlit + LangChain + RAG + AI"
)