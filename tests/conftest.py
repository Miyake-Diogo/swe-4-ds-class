# tests/conftest.py
"""
Fixtures compartilhadas para todos os testes.

Fixtures definidas aqui ficam disponíveis automaticamente
em todos os arquivos de teste.
"""
import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def sample_credit_data():
    """
    Fixture que fornece um DataFrame de exemplo para testes.
    
    Returns:
        pd.DataFrame: Dataset pequeno simulando dados de crédito.
    """
    return pd.DataFrame({
        "ID": [1, 2, 3, 4, 5],
        "LIMIT_BAL": [50000, 100000, 30000, 80000, 60000],
        "SEX": [1, 2, 1, 2, 1],
        "EDUCATION": [2, 1, 3, 2, 1],
        "MARRIAGE": [1, 2, 1, 1, 2],
        "AGE": [25, 35, 28, 42, 31],
        "PAY_0": [0, -1, 2, 0, 1],
        "PAY_2": [0, -1, 2, 0, 0],
        "PAY_3": [0, -1, 0, 0, 0],
        "PAY_4": [0, 0, 0, 0, 0],
        "PAY_5": [0, 0, 0, 0, 0],
        "PAY_6": [0, 0, 0, 0, 0],
        "BILL_AMT1": [10000, 50000, 5000, 30000, 20000],
        "BILL_AMT2": [9000, 48000, 4500, 28000, 19000],
        "BILL_AMT3": [8500, 46000, 4000, 26000, 18000],
        "BILL_AMT4": [8000, 44000, 3500, 24000, 17000],
        "BILL_AMT5": [7500, 42000, 3000, 22000, 16000],
        "BILL_AMT6": [7000, 40000, 2500, 20000, 15000],
        "PAY_AMT1": [1000, 5000, 500, 3000, 2000],
        "PAY_AMT2": [1000, 5000, 500, 3000, 2000],
        "PAY_AMT3": [1000, 5000, 500, 3000, 2000],
        "PAY_AMT4": [1000, 5000, 500, 3000, 2000],
        "PAY_AMT5": [1000, 5000, 500, 3000, 2000],
        "PAY_AMT6": [1000, 5000, 500, 3000, 2000],
        "default payment next month": [0, 0, 1, 0, 1],
    })


@pytest.fixture
def sample_features():
    """
    Fixture com apenas features numéricas para teste de normalização.
    """
    return np.array([
        [50000, 25, 10000],
        [100000, 35, 50000],
        [30000, 28, 5000],
    ])


@pytest.fixture
def empty_dataframe():
    """
    Fixture com DataFrame vazio para testar edge cases.
    """
    return pd.DataFrame()
