# (SUBSTITUIR conteúdo do arquivo)
# src/__init__.py
"""
SWE4DS Credit API - Módulo de análise de crédito.

Este pacote fornece ferramentas para validação e análise
de dados de crédito, desenvolvido como parte do curso
Engenharia de Machine Learning.

Uso básico:
    from src import validate_limit_bal, validate_age
    
    is_valid = validate_limit_bal(50000)
"""

__version__ = "0.1.0"
__author__ = "SWE4DS Team"

# Imports públicos
from .validation import (
    validate_age,
    validate_education,
    validate_input,
    validate_limit_bal,
)

__all__ = [
    "__version__",
    "__author__",
    "validate_limit_bal",
    "validate_age",
    "validate_education",
    "validate_input",
]