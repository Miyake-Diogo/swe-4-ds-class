# tests/unit/test_validation.py
"""
Testes para módulo de validação.

Criados usando TDD - testes escritos ANTES da implementação.
"""
import pytest


class TestValidateLimitBal:
    """Testes para validação de limite de crédito."""
    
    def test_rejects_negative_limit(self):
        """Limite negativo deve ser rejeitado."""
        from src.validation import validate_limit_bal
        
        assert validate_limit_bal(-1000) is False
    
    def test_rejects_zero_limit(self):
        """Limite zero deve ser rejeitado."""
        from src.validation import validate_limit_bal
        
        assert validate_limit_bal(0) is False
    
    def test_accepts_valid_limit(self):
        """Limite válido (positivo) deve ser aceito."""
        from src.validation import validate_limit_bal
        
        assert validate_limit_bal(50000) is True
    
    def test_rejects_excessive_limit(self):
        """Limite muito alto (> 1 milhão) deve ser rejeitado."""
        from src.validation import validate_limit_bal
        
        assert validate_limit_bal(2_000_000) is False
    
    @pytest.mark.parametrize("value,expected", [
        (1, True),           # Mínimo válido
        (500_000, True),     # Médio
        (1_000_000, True),   # Máximo válido
        (1_000_001, False),  # Acima do máximo
    ])
    def test_boundary_cases(self, value, expected):
        """Testa valores nos limites."""
        from src.validation import validate_limit_bal
        
        assert validate_limit_bal(value) is expected