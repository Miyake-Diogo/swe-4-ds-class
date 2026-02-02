# tests/unit/test_validation.py
"""
Testes para módulo de validação.

Criados usando TDD - testes escritos ANTES da implementação.
"""

import pytest

from src.validation import (
    validate_age,
    validate_education,
    validate_input,
    validate_limit_bal,
)


class TestValidateLimitBal:
    """Testes para validate_limit_bal."""

    def test_valid_positive_limit(self):
        """Limite positivo deve ser válido."""
        assert validate_limit_bal(50000) is True

    def test_valid_small_limit(self):
        """Limite pequeno mas positivo deve ser válido."""
        assert validate_limit_bal(1) is True

    def test_invalid_zero_limit(self):
        """Limite zero deve ser inválido."""
        assert validate_limit_bal(0) is False

    def test_invalid_negative_limit(self):
        """Limite negativo deve ser inválido."""
        assert validate_limit_bal(-1000) is False


class TestValidateAge:
    """Testes para validate_age."""

    def test_valid_adult_age(self):
        """Idade de adulto deve ser válida."""
        assert validate_age(30) is True

    def test_valid_minimum_age(self):
        """Idade mínima (18) deve ser válida."""
        assert validate_age(18) is True

    def test_valid_maximum_age(self):
        """Idade máxima (120) deve ser válida."""
        assert validate_age(120) is True

    def test_invalid_minor_age(self):
        """Idade de menor deve ser inválida."""
        assert validate_age(17) is False

    def test_invalid_too_old(self):
        """Idade acima de 120 deve ser inválida."""
        assert validate_age(121) is False


class TestValidateEducation:
    """Testes para validate_education."""

    @pytest.mark.parametrize("code", [1, 2, 3, 4])
    def test_valid_education_codes(self, code):
        """Códigos 1-4 devem ser válidos."""
        assert validate_education(code) is True

    @pytest.mark.parametrize("code", [0, 5, -1, 100])
    def test_invalid_education_codes(self, code):
        """Códigos fora de 1-4 devem ser inválidos."""
        assert validate_education(code) is False


class TestValidateInput:
    """Testes para validate_input."""

    def test_valid_complete_input(self):
        """Input completo e válido não deve ter erros."""
        data = {"LIMIT_BAL": 50000, "AGE": 30, "EDUCATION": 2}
        errors = validate_input(data)
        assert errors == {}

    def test_invalid_limit_bal(self):
        """Input com limite inválido deve retornar erro."""
        data = {"LIMIT_BAL": -1000}
        errors = validate_input(data)
        assert "LIMIT_BAL" in errors

    def test_multiple_errors(self):
        """Input com múltiplos erros deve retornar todos."""
        data = {"LIMIT_BAL": -1000, "AGE": 15, "EDUCATION": 0}
        errors = validate_input(data)
        assert len(errors) == 3

    def test_empty_input(self):
        """Input vazio não deve ter erros."""
        data = {}
        errors = validate_input(data)
        assert errors == {}
