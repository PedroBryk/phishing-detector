import streamlit as st
import joblib
import numpy as np
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Configuração da página
st.set_page_config(
    page_title="Detector de Phishing",
    layout="centered"
)

st.title("Detector de E-mails Phishing")
st.markdown("Cole o conteúdo do e-mail abaixo e selecione o modelo para analisar.")

# Sidebar para seleção do modelo
st.sidebar.title("Configurações")
modelo_escolhido = st.sidebar.selectbox(
    "Escolha o modelo:",
    ["Random Forest", "LSTM", "CNN", "DistilBERT"]
)

# Carrega os modelos em cache para não recarregar toda vez
@st.cache_resource
def carregar_random_forest():
    rf = joblib.load('models/random_forest.pkl')
    tfidf = joblib.load('models/tfidf_vectorizer.pkl')
    return rf, tfidf

@st.cache_resource
def carregar_lstm():
    model = load_model('models/lstm_model.keras')
    tokenizer = joblib.load('models/lstm_tokenizer.pkl')
    return model, tokenizer

@st.cache_resource
def carregar_cnn():
    model = load_model('models/cnn_model.keras')
    tokenizer = joblib.load('models/lstm_tokenizer.pkl')
    return model, tokenizer

@st.cache_resource
def carregar_bert():
    tokenizer = DistilBertTokenizer.from_pretrained('models/distilbert_tokenizer')
    model = DistilBertForSequenceClassification.from_pretrained('models/distilbert_model')
    model.eval()
    return model, tokenizer

# Campo de texto para o e-mail
email_texto = st.text_area(
    "Conteúdo do e-mail:",
    height=250,
    placeholder="Cole aqui o texto do e-mail que deseja analisar..."
)

# Botão de análise
if st.button("Analisar E-mail", use_container_width=True):
    if not email_texto.strip():
        st.warning("Por favor, cole o conteúdo de um e-mail antes de analisar.")
    else:
        with st.spinner("Analisando..."):

            if modelo_escolhido == "Random Forest":
                rf, tfidf = carregar_random_forest()
                X = tfidf.transform([email_texto])
                pred = rf.predict(X)[0]
                prob = rf.predict_proba(X)[0][pred]

            elif modelo_escolhido == "LSTM":
                model, tokenizer = carregar_lstm()
                seq = tokenizer.texts_to_sequences([email_texto])
                X = pad_sequences(seq, maxlen=200, truncating='post', padding='post')
                prob_raw = model.predict(X)[0][0]
                pred = 1 if prob_raw > 0.5 else 0
                prob = prob_raw if pred == 1 else 1 - prob_raw

            elif modelo_escolhido == "CNN":
                model, tokenizer = carregar_cnn()
                seq = tokenizer.texts_to_sequences([email_texto])
                X = pad_sequences(seq, maxlen=200, truncating='post', padding='post')
                prob_raw = model.predict(X)[0][0]
                pred = 1 if prob_raw > 0.5 else 0
                prob = prob_raw if pred == 1 else 1 - prob_raw

            elif modelo_escolhido == "DistilBERT":
                model, tokenizer = carregar_bert()
                inputs = tokenizer(
                    email_texto,
                    return_tensors='pt',
                    max_length=128,
                    truncation=True,
                    padding='max_length'
                )
                with torch.no_grad():
                    outputs = model(**inputs)
                probs = torch.softmax(outputs.logits, dim=1)[0]
                pred = probs.argmax().item()
                prob = probs[pred].item()

        # Exibe o resultado
        st.markdown("---")
        if pred == 1:
            st.error(f"🚨 **PHISHING DETECTADO!**")
        else:
            st.success(f"✅ **E-mail Legítimo**")

        st.metric("Confiança do modelo", f"{prob * 100:.2f}%")
        st.caption(f"Modelo utilizado: {modelo_escolhido}")