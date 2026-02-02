# src/validation.py
"""
Módulo de validação para dados de crédito.

Funções de validação para garantir qualidade dos dados
antes de processamento e predição.
"""

from typing import Any

# Type alias para valores numéricos
type NumericValue = int | float

# Constantes de validação
LIMIT_BAL_MIN: int = 1
LIMIT_BAL_MAX: int = 1_000_000

AGE_MIN: int = 18
AGE_MAX: int = 100

VALID_EDUCATION: tuple[int, ...] = (1, 2, 3, 4)
VALID_MARRIAGE: tuple[int, ...] = (1, 2, 3)


def validate_limit_bal(limit_bal: float) -> bool:
    """
    Valida o limite de crédito.

    Args:
        limit_bal: Valor do limite de crédito em NT$.

    Returns:
        True se o valor é válido (positivo), False caso contrário.

    Examples:
        >>> validate_limit_bal(50000)
        True
        >>> validate_limit_bal(-1000)
        False
    """
    return limit_bal > 0


def validate_age(age: int) -> bool:
    """
    Valida a idade do cliente.

    Args:
        age: Idade em anos.

    Returns:
        True se a idade está no range válido (18-120), False caso contrário.
    """
    return 18 <= age <= 120


def validate_education(education: int) -> bool:
    """
    Valida o nível educacional.

    Args:
        education: Código do nível educacional (1-4).

    Returns:
        True se o código é válido, False caso contrário.
    """
    valid_codes = {1, 2, 3, 4}  # 1=graduate, 2=university, 3=high school, 4=others
    return education in valid_codes


def validate_input(data: dict[str, Any]) -> dict[str, list[str]]:
    """
    Valida todos os campos de entrada.

    Args:
        data: Dicionário com os dados do cliente.

    Returns:
        Dicionário com lista de erros por campo.
    """
    errors: dict[str, list[str]] = {}

    if "LIMIT_BAL" in data and not validate_limit_bal(data["LIMIT_BAL"]):
        errors.setdefault("LIMIT_BAL", []).append("Limite deve ser positivo")

    if "AGE" in data and not validate_age(data["AGE"]):
        errors.setdefault("AGE", []).append("Idade deve estar entre 18 e 120")

    if "EDUCATION" in data and not validate_education(data["EDUCATION"]):
        errors.setdefault("EDUCATION", []).append("Educação deve ser 1, 2, 3 ou 4")

    return errors


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
