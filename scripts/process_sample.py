# scripts/process_sample.py
"""
Script para demonstrar processamento de dados em container.
Usa volume para ler dados e salvar resultados.
"""
from pathlib import Path
import sys

# Adicionar src ao path
sys.path.insert(0, "/app")

from src.data_loader import get_feature_names
from src.validation import validate_limit_bal, validate_age
import pandas as pd


def main():
    print("=" * 50)
    print("Processamento de Dados em Container Docker")
    print("=" * 50)
    
    # Verificar diretório de dados
    data_dir = Path("/app/data/raw")
    output_dir = Path("/app/data/processed")
    
    if not data_dir.exists():
        print(f"\n[ERRO] Diretório não encontrado: {data_dir}")
        print("Monte o volume com: -v /seu/path/data:/app/data")
        return 1
    
    # Listar arquivos
    print(f"\nArquivos em {data_dir}:")
    for f in data_dir.iterdir():
        print(f"  - {f.name}")
    
    # Criar dados de exemplo se não existir CSV
    csv_files = list(data_dir.glob("*.csv"))
    if not csv_files:
        print("\n[INFO] Nenhum CSV encontrado. Criando dados de exemplo...")
        sample_data = pd.DataFrame({
            "ID": range(1, 11),
            "LIMIT_BAL": [50000, 100000, 30000, 80000, 60000, 
                        150000, 20000, 90000, 70000, 40000],
            "AGE": [25, 35, 28, 42, 31, 55, 22, 38, 45, 29],
            "default payment next month": [0, 0, 1, 0, 1, 0, 1, 0, 0, 1]
        })
        sample_file = data_dir / "sample_credit.csv"
        sample_data.to_csv(sample_file, index=False)
        print(f"  Criado: {sample_file}")
        csv_files = [sample_file]
    
    # Processar primeiro CSV encontrado
    csv_file = csv_files[0]
    print(f"\nProcessando: {csv_file.name}")
    
    df = pd.read_csv(csv_file)
    print(f"  Linhas: {len(df)}")
    print(f"  Colunas: {list(df.columns)}")
    
    # Validar dados
    print("\nValidação:")
    if "LIMIT_BAL" in df.columns:
        valid_limits = df["LIMIT_BAL"].apply(validate_limit_bal).sum()
        print(f"  Limites válidos: {valid_limits}/{len(df)}")
    
    if "AGE" in df.columns:
        valid_ages = df["AGE"].apply(validate_age).sum()
        print(f"  Idades válidas: {valid_ages}/{len(df)}")
    
    # Salvar resultado
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "processed_sample.csv"
    df.to_csv(output_file, index=False)
    print(f"\nResultado salvo em: {output_file}")
    
    print("\n" + "=" * 50)
    print("Processamento concluído com sucesso!")
    print("=" * 50)
    return 0


if __name__ == "__main__":
    sys.exit(main())