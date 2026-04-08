# 📊 Projeto-AD

Pipeline de Dados para extração, transformação e análise de dados, com foco em organização, padronização e preparação para análise exploratória e visualização.

---

## 🚀 Sobre o Projeto

O **Projeto-AD** tem como objetivo construir um pipeline de dados completo, passando pelas etapas de:

- Extração de dados brutos (CSV)
- Tratamento e padronização
- Validação de estrutura (schema)
- Armazenamento em camadas (raw → interim → processed)
- Preparação para análise e visualização

O projeto segue boas práticas de engenharia de dados, visando organização, reprodutibilidade e escalabilidade.
Os dados foram extraídos do repositório de dados abertos da ANP (Agência Nacional do Petróleo, Gás Natural e Biocombustíveis do Brasil)
---

## 🧱 Arquitetura do Projeto

O pipeline segue uma arquitetura em camadas:

data/
│
├── raw/         # Dados brutos (sem tratamento)
├── interim/     # Dados parcialmente tratados
└── processed/   # Dados prontos para análise

Fluxo:

RAW → NORMALIZAÇÃO → VALIDAÇÃO → PROCESSADO

---

## ⚙️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Pathlib / OS
- Estrutura modular (scripts organizados por responsabilidade)

---

## 🔄 Pipeline de Dados

### 1. Extração
Leitura de múltiplos arquivos CSV, tratando possíveis problemas de:
- Encoding
- Número inconsistente de colunas

### 2. Normalização
Padronização dos dados:
- Nomes de colunas
- Tipos de dados
- Formatação geral

### 3. Validação
- Verificação de consistência entre arquivos
- Comparação de estruturas (colunas)
- Definição de schema padrão

### 4. Armazenamento
- Salvamento em camadas intermediárias e finais
- Organização para facilitar análise posterior

---

## 📁 Estrutura do Projeto

project/
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── src/
│   ├── ingestion/
│   ├── io/
│   └── processing/
│
├── config/
│   └── settings.py
│
├── main.py
└── README.md

---

## ▶️ Como Executar

1. Clone o repositório:

git clone https://github.com/Luiz-Prudente/Projeto-AD.git
cd Projeto-AD

2. Crie um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Instale as dependências:

pip install -r requirements.txt

4. Execute o pipeline:

python main.py

---

## 📊 Próximos Passos

- Análise exploratória dos dados (EDA)
- Criação de dashboards (Power BI / Python)
- Possível migração para banco de dados
- Otimização com formatos como Parquet
- Automação do pipeline

---

## 🎯 Objetivo Acadêmico

Este projeto foi desenvolvido como parte dos estudos em **Ciência de Dados**, com foco em:

- Engenharia de Dados
- Construção de pipelines ETL
- Boas práticas de organização de projetos

---

## 👨‍💻 Autor

**João Victor Luiz Prudente de Sousa**

- Estudante de Ciência de Dados
- Foco em Engenharia de Dados e análise

---

## 📌 Observações

Este projeto está em constante evolução conforme novos conceitos e práticas são estudados e aplicados.
