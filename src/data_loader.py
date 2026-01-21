"""
Módulo de carregamento e preprocessamento de dados.

Este módulo é responsável por carregar o dataset de inadimplência
de cartão de crédito e preparar os dados para treinamento/inferência.
"""
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, Optional
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# URL do dataset UCI Credit Card Default
DATASET_URL = (
    "https://raw.githubusercontent.com/dados-ml/"
    "credit-default/main/data.csv"
)


def load_credit_data(
    filepath: Optional[Path] = None,
    use_cache: bool = True
) -> pd.DataFrame:
    """
    Carrega o dataset de inadimplência de cartão de crédito.
    
    Args:
        filepath: Caminho para arquivo local. Se None, baixa da UCI.
        use_cache: Se True, salva/carrega de cache local.
    
    Returns:
        DataFrame com os dados brutos.
        
    Raises:
        FileNotFoundError: Se filepath especificado não existir.
        ValueError: Se dados estiverem corrompidos.
    """
    cache_path = Path("data/credit_data.parquet")
    
    # Tentar carregar do cache
    if use_cache and cache_path.exists():
        print(f"Carregando dados do cache: {cache_path}")
        return pd.read_parquet(cache_path)
    
    # Carregar de arquivo local ou URL
    if filepath is not None:
        if not filepath.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
        print(f"Carregando dados de: {filepath}")
        df = pd.read_excel(filepath, header=1)
    else:
        print(f"Baixando dados de: {DATASET_URL}")
        df = pd.read_excel(DATASET_URL, header=1)
    
    # Validar dados
    if df.empty:
        raise ValueError("Dataset vazio!")
    
    # Salvar cache
    if use_cache:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(cache_path)
        print(f"Cache salvo em: {cache_path}")
    
    return df


def preprocess_data(
    df: pd.DataFrame,
    target_column: str = "default payment next month",
    test_size: float = 0.2,
    random_state: int = 42
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, StandardScaler]:
    """
    Preprocessa os dados para treinamento.
    
    Args:
        df: DataFrame com dados brutos.
        target_column: Nome da coluna alvo.
        test_size: Proporção do conjunto de teste.
        random_state: Seed para reprodutibilidade.
    
    Returns:
        Tupla com (X_train, X_test, y_train, y_test, scaler).
    """
    # Remover coluna ID
    df = df.drop(columns=["ID"], errors="ignore")
    
    # Separar features e target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Split treino/teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=test_size, 
        random_state=random_state,
        stratify=y
    )
    
    # Normalizar features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train.values, y_test.values, scaler


def get_feature_names() -> list:
    """
    Retorna os nomes das features do dataset.
    
    Returns:
        Lista com nomes das features.
    """
    return [
        "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE",
        "PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6",
        "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6",
        "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"
    ]


if __name__ == "__main__":
    # Teste rápido do módulo
    print("Testando data_loader...")
    
    # Nota: Descomentar para testar (requer internet)
    # df = load_credit_data()
    # print(f"Shape: {df.shape}")
    # print(f"Colunas: {df.columns.tolist()}")
    
    print("Módulo carregado com sucesso!")
    print(f"Features disponíveis: {len(get_feature_names())}")