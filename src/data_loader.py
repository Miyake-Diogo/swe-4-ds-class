# src/data_loader.py
"""
Módulo para carregamento e preprocessamento de dados de crédito.
"""
from pathlib import Path
from typing import Tuple, List
import pandas as pd


def load_credit_data(
    filepath: Path | None = None,
    use_cache: bool = True
) -> pd.DataFrame:
    """
    Carrega dados de crédito de arquivo CSV ou cache.
    
    Args:
        filepath: Caminho para arquivo CSV. Se None, usa padrão.
        use_cache: Se True, tenta carregar de cache parquet.
        
    Returns:
        DataFrame com dados de crédito.
        
    Raises:
        FileNotFoundError: Se arquivo não existe.
        ValueError: Se dados estão vazios.
    """
    if filepath is None:
        filepath = Path("data/raw/UCI_Credit_Card.csv")
    
    cache_path = Path("data/processed/credit_cache.parquet")
    
    if use_cache and cache_path.exists():
        return pd.read_parquet(cache_path)
    
    if not filepath.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    
    df = pd.read_csv(filepath)
    
    if df.empty:
        raise ValueError("Dataset está vazio")
    
    if use_cache:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(cache_path)
    
    return df


def preprocess_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Preprocessa dados separando features e target.
    
    Args:
        df: DataFrame com dados brutos.
        
    Returns:
        Tupla (features DataFrame, target Series).
        
    Raises:
        KeyError: Se coluna target não existe.
    """
    target_col = "default payment next month"
    
    if target_col not in df.columns:
        raise KeyError(f"Coluna target '{target_col}' não encontrada")
    
    # Remover ID e target das features
    feature_cols = [c for c in df.columns if c not in ["ID", target_col]]
    
    X = df[feature_cols]
    y = df[target_col]
    
    return X, y

def get_feature_names(df: pd.DataFrame) -> List[str]:
    """
    Retorna lista de nomes de features (exclui ID e target).
    
    Args:
        df: DataFrame com dados.
        
    Returns:
        Lista de nomes de colunas.
    """
    exclude = ["ID", "default payment next month"]
    return [c for c in df.columns if c not in exclude]