# Detector de Email de Phishing

Projeto acadêmico de detecção de e-mails de phishing utilizando técnicas de Machine Learning e Deep Learning.

## Sobre o Projeto

Este projeto treina e compara quatro modelos de inteligência artificial para classificar e-mails como legítimos ou phishing, utilizando um dataset de 82.486 e-mails reais obtido do Kaggle.

## Dataset

Fonte: Kaggle - Phishing Email Dataset. Link: https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset. O arquivo utilizado é o phishing_email.csv, contendo 82.486 e-mails com duas colunas: text_combined (texto do e-mail) e label (0 = legítimo, 1 = phishing). O dataset é bem balanceado com 52% de phishing e 48% de e-mails legítimos.

## Modelos Utilizados

Random Forest (ML Clássico) - 98.77% de acurácia. Escolhido por sua robustez e bom desempenho em dados textuais com TF-IDF. Referência: Akinyelu (2014) - Classification of Phishing Email Using Random Forest Machine Learning Technique. https://doi.org/10.1155/2014/425731

LSTM (DL Clássico) - 98.37% de acurácia. Escolhido por sua capacidade de capturar a ordem e o contexto das palavras em sequências de texto. Referência: Al-Selwi et al. - LSTM based Phishing Detection for Big Email Data. https://www.researchgate.net/publication/339892999

CNN (DL Treinado do Zero) - 98.32% de acurácia. Escolhido por sua eficiência na detecção de padrões locais no texto e velocidade de treinamento. Referência: Gurumurthy & Chitra (2024) - Email Phishing Detection Model using CNN Model. https://doi.org/10.61453/joit.v2024no43

DistilBERT (DL Pré-treinado) - 97.95% de acurácia. Escolhido por ser um modelo pré-treinado em bilhões de textos, 40% menor e 60% mais rápido que o BERT original, mantendo 97% da performance. Referência: Uddin & Sarker (2024) - An Explainable Transformer-based Model for Phishing Email Detection. https://arxiv.org/abs/2402.13871

## Como Executar

Clone o repositório com `git clone https://github.com/PedroBryk/phishing-detector.git` e entre na pasta com `cd phishing-detector`. Crie e ative o ambiente virtual com `python -m venv venv` e `venv\Scripts\activate`. Instale as dependências com `pip install -r requirements.txt` e `pip install torch`. Baixe o dataset em https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset, coloque o arquivo phishing_email.csv na pasta data/ e execute os notebooks de 01 a 05 em ordem no Jupyter para treinar os modelos. Por fim, rode a interface com `streamlit run app.py`.

## Equipe

Pedro, Alana, Matheus e Kaka
