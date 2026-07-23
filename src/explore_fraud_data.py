"""
Análise exploratória e visualização — Previsão de fraude em seguros de automóveis.

Este script reproduz, em Python/pandas, a lógica aplicada na ferramenta de
Data Refinery do IBM Watson Studio durante o curso Data Fundamentals (IBM):

1. Carrega o dataset já limpo (colunas de ID, dados pessoais e colunas vazias
   foram removidas no Watson Studio — ver README para o passo a passo completo).
2. Recria a variável derivada EXCESSIVE_CLAIM_AMOUNT (reivindicação > US$10 mil).
3. Gera o gráfico de dispersão CLAIM_AMOUNT x EXCESSIVE_CLAIM_AMOUNT,
   colorido por FLAG_FOR_FRAUD_INV (0 = sem fraude, 1 = fraude confirmada),
   o mesmo gráfico usado para validar a hipótese do time de negócio.

Uso:
    python src/explore_fraud_data.py
"""

import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/AutoInsClaims_csv_shaped_shaped.csv"
OUTPUT_PATH = "images/scatter_claim_vs_fraud.png"


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def recreate_excessive_claim_flag(df: pd.DataFrame) -> pd.DataFrame:
    """Recria a coluna derivada criada no Watson Studio (Data Refinery)."""
    df["EXCESSIVE_CLAIM_AMOUNT"] = (df["CLAIM_AMOUNT"] > 10_000).astype(int)
    return df


def plot_claim_vs_fraud(df: pd.DataFrame, output_path: str) -> None:
    colors = df["FLAG_FOR_FRAUD_INV"].map({0: "#4FB6A6", 1: "#D62839"})

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(
        df["EXCESSIVE_CLAIM_AMOUNT"],
        df["CLAIM_AMOUNT"],
        c=colors,
        alpha=0.6,
        s=25,
        edgecolors="none",
    )
    ax.set_xticks([0, 1])
    ax.set_xlabel("EXCESSIVE_CLAIM_AMOUNT (reivindicação > US$10 mil)")
    ax.set_ylabel("CLAIM_AMOUNT (US$)")
    ax.set_title("Reivindicações acima de US$10 mil são mais propensas a fraude?")

    legend_elements = [
        plt.Line2D([0], [0], marker="o", color="w", label="Sem fraude",
                    markerfacecolor="#4FB6A6", markersize=8),
        plt.Line2D([0], [0], marker="o", color="w", label="Fraude confirmada",
                    markerfacecolor="#D62839", markersize=8),
    ]
    ax.legend(handles=legend_elements, loc="upper left")

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    print(f"Gráfico salvo em: {output_path}")


def print_summary(df: pd.DataFrame) -> None:
    total = len(df)
    fraud_rate_below = df[df["EXCESSIVE_CLAIM_AMOUNT"] == 0]["FLAG_FOR_FRAUD_INV"].mean()
    fraud_rate_above = df[df["EXCESSIVE_CLAIM_AMOUNT"] == 1]["FLAG_FOR_FRAUD_INV"].mean()

    print(f"Total de reivindicações: {total}")
    print(f"Taxa de fraude ABAIXO de US$10 mil: {fraud_rate_below:.1%}")
    print(f"Taxa de fraude ACIMA de US$10 mil:  {fraud_rate_above:.1%}")


if __name__ == "__main__":
    df = load_data(DATA_PATH)
    df = recreate_excessive_claim_flag(df)
    print_summary(df)
    plot_claim_vs_fraud(df, OUTPUT_PATH)
