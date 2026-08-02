# 🚗 Previsão de Fraude em Seguros de Automóveis

<p align="left">
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/IBM%20Watson-006699?style=for-the-badge&logo=ibm&logoColor=white" />
</p>

---

## 📌 Visão Geral

Projeto prático desenvolvido como parte do curso **Data Fundamentals (IBM)**, focado na etapa de **limpeza e exploração de dados** — a base de qualquer projeto de ciência de dados.

A análise foi realizada originalmente no **IBM Watson Studio (Data Refinery)** e reproduzida neste repositório em **Python/pandas** para fins de portfólio.

---

## 🎯 Objetivo

Identificar padrões em reivindicações de seguros de automóveis que possam indicar **fraude**, a partir de um processo estruturado de limpeza, engenharia de variáveis e visualização de dados.

---

## 📊 Dataset

| Item | Detalhe |
|---|---|
| **Arquivo** | `AutoInsClaims_csv_shaped_shaped.csv` |
| **Colunas originais** | 38 |
| **Colunas após limpeza** | 19 |
| **Variável-alvo** | `FLAG_FOR_FRAUD_INV` |
| **Fonte** | IBM Watson Studio — Data Fundamentals |

O dataset contém dados de reivindicações de seguros já aprovadas e pagas, incluindo informações sobre o valor da reivindicação, causa do incidente, status do sinistro e o veredito de investigadores de fraude.

---

## 🛠 Tecnologias Utilizadas

| Ferramenta | Uso |
|---|---|
| **IBM Watson Studio** | Limpeza, perfilamento e visualização de dados (Data Refinery) |

---

## 🔎 Etapas da Análise

### 1. Limpeza de Dados

| Ação | Colunas | Motivo |
|---|---|---|
| 🗑️ Removidas | `HOUSEHOLD_ID`, `DRIVER_ID`, `POLICY_ID`, `CLAIM_ID`, `PRIMARY_DRIVER_ID` | Identificadores únicos — sem poder preditivo |
| 🔒 Removidas | `FIRST_NAME`, `LAST_NAME` | Dados pessoais — não ajudam a prever fraude |
| 🗑️ Removida | `DESCRIPTION` | Coluna vazia |
| 🛠️ Tipo corrigido | `LOSS_EVENT_TIME` | String → Data |
| ✅ Mantidas | Demais colunas relevantes | Variáveis com potencial preditivo |

**Resultado:** dataset reduzido de **38 → 19 colunas**.

### 2. Engenharia de Variável

Criação de variável derivada para testar hipótese de negócio:

```python
df["EXCESSIVE_CLAIM_AMOUNT"] = (df["CLAIM_AMOUNT"] > 10_000).astype(int)
```

> **Hipótese:** reivindicações acima de US$ 10.000 têm maior chance de ser fraude.

### 3. Visualização e Teste de Hipótese

Gráfico de dispersão cruzando `EXCESSIVE_CLAIM_AMOUNT` × `CLAIM_AMOUNT`, colorido pela variável-alvo `FLAG_FOR_FRAUD_INV`.

---

## 📈 Principais Resultados

| Faixa de valor | Taxa de fraude |
|---|---|
| Abaixo de US$ 10.000 | **5,3%** |
| Acima de US$ 10.000 | **95,2%** |

A hipótese se confirma na maioria dos casos — o valor da reivindicação é um **sinal forte**, porém não absoluto. Existem fraudes com valores baixos e reivindicações altas legítimas.

---

## 📷 Capturas de Tela

### Gráfico de dispersão — Valor da Reivindicação vs. Fraude

![Scatter plot - Claim vs Fraud](images/scatter_claim_vs_fraud.png)

---

## 🚀 Como Executar

### Pré-requisitos
- Conta no [IBM Watson Studio](https://www.ibm.com/cloud/watson-studio) (gratuita)

### Passo a passo

1. Faça login no **IBM Watson Studio**
2. Crie um novo projeto
3. Importe o dataset `data/AutoInsClaims_csv_shaped_shaped.csv`
4. Abra o **Data Refinery** e aplique as transformações descritas acima
5. Exporte o dataset limpo e gere as visualizações

---

## 📂 Estrutura do Projeto

```
auto-insurance-fraud-project/
│
├── data/
│   └── AutoInsClaims_csv_shaped_shaped.csv   # Dataset após limpeza
├── images/
│   └── scatter_claim_vs_fraud.png            # Gráfico gerado
├── requirements.txt                           # Dependências
└── README.md
```

---

## 📝 Conclusões

- O valor da reivindicação (`CLAIM_AMOUNT`) é o principal preditor de fraude neste dataset
- A etapa de limpeza foi essencial: **19 das 38 colunas** foram removidas por serem identificadores, dados pessoais ou colunas vazias
- O dataset limpo está pronto para a próxima etapa: **modelagem supervisionada** com algoritmos de classificação

---

## 👨‍💻 Autor

**Felipe Simon**
- 📍 São Bernardo do Campo, SP
- 🎓 Ciência de Dados — FATEC
- 💼 [LinkedIn](https://www.linkedin.com/in/felipe-simon-83ba10352)
- 📧 simonhot.com@gmail.com

---

<p align="left">
  <img src="https://img.shields.io/badge/Curso-Data%20Fundamentals%20IBM-006699?style=flat-square&logo=ibm" />
</p>
