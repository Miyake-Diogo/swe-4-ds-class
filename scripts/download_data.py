# scripts/download_data.py
"""
Script para download do dataset de credit default.
"""
import urllib.request
import os
from pathlib import Path


def download_credit_dataset():
    """
    Baixa o dataset UCI Credit Card Default e salva localmente.
    
    Para fins didáticos, vamos criar um dataset de exemplo.
    Em produção, você baixaria de uma fonte real.
    """
    output_dir = Path("data/raw")
    output_file = output_dir / "credit_sample.csv"
    
    # Criar diretório se não existir
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Para a aula, vamos criar um dataset de exemplo
    # Em produção, você baixaria o dataset real
    print("Criando dataset de exemplo...")
    
    import random
    
    # Gerar dados de exemplo
    header = "ID,LIMIT_BAL,SEX,EDUCATION,MARRIAGE,AGE,PAY_0,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6,default\n"
    
    rows = []
    for i in range(1, 2001):  # 1000 registros de exemplo
        row = [
            i,                              # ID
            random.randint(10000, 500000),  # LIMIT_BAL
            random.randint(1, 2),           # SEX
            random.randint(1, 4),           # EDUCATION
            random.randint(1, 3),           # MARRIAGE
            random.randint(21, 70),         # AGE
            random.randint(-2, 8),          # PAY_0
            random.randint(-2, 8),          # PAY_2
            random.randint(-2, 8),          # PAY_3
            random.randint(-2, 8),          # PAY_4
            random.randint(-2, 8),          # PAY_5
            random.randint(-2, 8),          # PAY_6
            random.randint(0, 100000),      # BILL_AMT1
            random.randint(0, 100000),      # BILL_AMT2
            random.randint(0, 100000),      # BILL_AMT3
            random.randint(0, 100000),      # BILL_AMT4
            random.randint(0, 100000),      # BILL_AMT5
            random.randint(0, 100000),      # BILL_AMT6
            random.randint(0, 50000),       # PAY_AMT1
            random.randint(0, 50000),       # PAY_AMT2
            random.randint(0, 50000),       # PAY_AMT3
            random.randint(0, 50000),       # PAY_AMT4
            random.randint(0, 50000),       # PAY_AMT5
            random.randint(0, 50000),       # PAY_AMT6
            random.randint(0, 1),           # default
        ]
        rows.append(",".join(map(str, row)) + "\n")
    
    # Escrever arquivo
    with open(output_file, "w") as f:
        f.write(header)
        f.writelines(rows)
    
    print(f"Dataset salvo em: {output_file}")
    print(f"Tamanho: {output_file.stat().st_size / 1024:.2f} KB")
    print(f"Registros: {len(rows)}")
    
    return output_file


if __name__ == "__main__":
    download_credit_dataset()