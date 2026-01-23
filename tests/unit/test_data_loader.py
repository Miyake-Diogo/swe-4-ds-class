# tests/unit/test_data_loader.py
"""
Testes unitários para o módulo data_loader.

Estes testes verificam o comportamento das funções de
carregamento e preprocessamento de dados de crédito.
"""
import pytest
import pandas as pd
from src.data_loader import get_feature_names


class TestGetFeatureNames:
    """Testes para a função get_feature_names."""
    
    def test_returns_list(self, sample_credit_data):
        """
        Verifica que o retorno é uma lista.
        
        Args:
            sample_credit_data: Fixture do conftest.py
        """
        # ACT
        result = get_feature_names(sample_credit_data)
        
        # ASSERT
        assert isinstance(result, list)
    
    def test_excludes_id_column(self, sample_credit_data):
        """Verifica que coluna ID é excluída."""
        result = get_feature_names(sample_credit_data)
        assert "ID" not in result
    
    def test_excludes_target_column(self, sample_credit_data):
        """Verifica que coluna target é excluída."""
        result = get_feature_names(sample_credit_data)
        assert "default payment next month" not in result
    
    def test_returns_correct_count(self, sample_credit_data):
        """
        Verifica quantidade de features.
        
        23 colunas totais - ID - target = 21 features
        """
        result = get_feature_names(sample_credit_data)
        # Total de colunas (25) - ID - target = 23
        # Nosso fixture tem 25 colunas
        assert len(result) == 23
    
    def test_with_empty_dataframe(self, empty_dataframe):
        """Verifica comportamento com DataFrame vazio."""
        result = get_feature_names(empty_dataframe)
        assert result == []