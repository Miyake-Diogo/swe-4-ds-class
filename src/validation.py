# src/validation.py
"""
Módulo de validação para dados de crédito.

Funções de validação para garantir qualidade dos dados
antes de processamento e predição.
"""
from typing import TypeAlias

# Type alias para valores numéricos
NumericValue: TypeAlias = int | float

# Constantes de validação
LIMIT_BAL_MIN: int = 1
LIMIT_BAL_MAX: int = 1_000_000

AGE_MIN: int = 18
AGE_MAX: int = 100

VALID_EDUCATION: tuple[int, ...] = (1, 2, 3, 4)
VALID_MARRIAGE: tuple[int, ...] = (1, 2, 3)


def validate_limit_bal(value: NumericValue) -> bool:
    """
    Valida se o limite de crédito é aceitável.
    
    Limite deve estar entre 1 e 1.000.000.
    
    Args:
        value: Valor do limite de crédito.
        
    Returns:
        True se válido (1 <= value <= 1.000.000), False caso contrário.
    """
    return LIMIT_BAL_MIN <= value <= LIMIT_BAL_MAX


def validate_age(value: NumericValue) -> bool:
    """
    Valida se a idade é aceitável para análise de crédito.
    
    Idade deve estar entre 18 e 100 anos.
    
    Args:
        value: Idade em anos.
        
    Returns:
        True se válido (18 <= value <= 100), False caso contrário.
    """
    return AGE_MIN <= value <= AGE_MAX


def validate_education(value: int) -> bool:
    """
    Valida código de educação.
    
    Códigos válidos:
    - 1: Graduate school
    - 2: University
    - 3: High school
    - 4: Others
    
    Args:
        value: Código de educação.
        
    Returns:
        True se válido, False caso contrário.
    """
    return value in VALID_EDUCATION


def validate_marriage(value: int) -> bool:
    """
    Valida código de estado civil.
    
    Códigos válidos:
    - 1: Married
    - 2: Single
    - 3: Others
    
    Args:
        value: Código de estado civil.
        
    Returns:
        True se válido, False caso contrário.
    """
    return value in VALID_MARRIAGE