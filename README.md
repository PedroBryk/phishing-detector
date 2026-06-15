```markdown
# Detector de Email de Phishing

## Sobre o Projeto

Este projeto treina e compara quatro modelos de inteligência artificial para classificar e-mails como legítimos ou phishing, utilizando um dataset de 82.486 e-mails reais obtido do Kaggle.

## Dataset

Fonte: Kaggle - Phishing Email Dataset
Link: https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset

O arquivo utilizado é o phishing_email.csv, contendo 82.486 e-mails com duas colunas: text_combined (texto do e-mail) e label (0 = legítimo, 1 = phishing). O dataset é bem balanceado com 52% de phishing e 48% de e-mails legítimos.

## Modelos Utilizados

Random Forest (ML Clássico) - 98.77% de acurácia. Escolhido por sua robustez e bom desempenho em dados textuais com TF-IDF. Referência: Akinyelu (2014) - Classification of Phishing Email Using Random Forest Machine Learning Technique. https://doi.org/10.1155/2014/425731

LSTM (DL Clássico) - 98.37% de acurácia. Escolhido por sua capacidade de capturar a ordem e o contexto das palavras em sequências de texto. Referência: Al-Selwi et al. - LSTM based Phishing Detection for Big Email Data. https://www.researchgate.net/publication/339892999

CNN (DL Treinado do Zero) - 98.32% de acurácia. Escolhido por sua eficiência na detecção de padrões locais no texto e velocidade de treinamento. Referência: Gurumurthy & Chitra (2024) - Email Phishing Detection Model using CNN Model. https://doi.org/10.61453/joit.v2024no43

DistilBERT (DL Pré-treinado) - 97.95% de acurácia. Escolhido por ser um modelo pré-treinado em bilhões de textos, 40% menor e 60% mais rápido que o BERT original, mantendo 97% da performance. Referência: Uddin & Sarker (2024) - An Explainable Transformer-based Model for Phishing Email Detection. https://arxiv.org/abs/2402.13871

## Estrutura do Projeto

```
phishing-detector/
├── data/                    # Dataset (não versionado)
├── notebooks/
│   ├── 01_exploracao.ipynb  # Exploração e limpeza dos dados
│   ├── 02_random_forest.ipynb
│   ├── 03_lstm.ipynb
│   ├── 04_cnn.ipynb
│   └── 05_bert.ipynb
├── models/                  # Modelos treinados (não versionados)
├── src/
├── reports/
├── app.py                   # Interface Streamlit
├── requirements.txt
└── README.md
```

## Como Executar

1. Clonar o repositório
```
git clone https://github.com/PedroBryk/phishing-detector.git
cd phishing-detector
```

2. Criar e ativar o ambiente virtual
```
python -m venv venv
venv\Scripts\activate
```

3. Instalar as dependências
```
pip install -r requirements.txt
pip install torch
```

4. Baixar o dataset

Acesse https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset, baixe o arquivo phishing_email.csv e coloque na pasta data/.

5. Rodar os notebooks em ordem

Abra o Jupyter e execute os notebooks de 01 a 05 na pasta notebooks/ para treinar os modelos.

6. Rodar a interface
```
streamlit run app.py
```

## Equipe

Pedro, Alana, Matheus e Kaka
```
