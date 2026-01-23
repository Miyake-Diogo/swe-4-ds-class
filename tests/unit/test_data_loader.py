# tests/unit/test_data_loader.py
"""
Testes unitários para o módulo data_loader.

Estes testes verificam o comportamento das funções de
carregamento e preprocessamento de dados de crédito.
"""
import pytest
import pandas as pd
from src.data_loader import get_feature_names, preprocess_data, load_credit_data
from pathlib import Path
from unittest.mock import MagicMock

class TestFeatureNames:
    """ Testes para a função get_feature_names"""

    def test_returns_list(self, sample_credit_data):
        """
        Verifica que o retorno é uma lista.
        Args: 
            sample_credit_data: Fixture do conftest.py
        """
        # Act 
        result = get_feature_names(sample_credit_data)

        # Assert
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

## Preprocess Data


## Mock

class TestLoadCreditData:
    """Testes para a função load_credit_data."""
    @pytest.mark.slow
    def test_loads_from_cache_when_exists(self, mocker, sample_credit_data):
        """
        Verifica que usa cache quando disponível.
        """
        # ARRANGE
        # Mock read_parquet para retornar nosso fixture
        mock_read_parquet = mocker.patch(
            "src.data_loader.pd.read_parquet",
            return_value=sample_credit_data
        )
        
        # Mock Path.exists para cache existir
        mocker.patch("src.data_loader.Path.exists", return_value=True)
        
        # ACT
        result = load_credit_data(use_cache=True)
        
        # ASSERT
        mock_read_parquet.assert_called_once()
        assert result.equals(sample_credit_data)
    
    def test_loads_from_csv_when_no_cache(
        self,
        mocker,
        sample_credit_data,
        tmp_path
    ):
        """
        Verifica carregamento de CSV quando cache não existe.
        """
        # ARRANGE
        # Criar arquivo CSV temporário
        csv_path = tmp_path / "test_data.csv"
        sample_credit_data.to_csv(csv_path, index=False)
        
        # Mock para cache não existir
        def mock_exists(self):
            return self == csv_path
        
        mocker.patch.object(Path, "exists", mock_exists)
        
        # Mock to_parquet para não tentar salvar
        mocker.patch("pandas.DataFrame.to_parquet")
        
        # ACT
        result = load_credit_data(filepath=csv_path, use_cache=False)
        
        # ASSERT
        assert len(result) == len(sample_credit_data)
    
    def test_raises_filenotfound_for_missing_file(self, mocker):
        """
        Verifica que levanta FileNotFoundError para arquivo inexistente.
        """
        # ARRANGE
        mocker.patch.object(Path, "exists", return_value=False)
        
        # ACT & ASSERT
        with pytest.raises(FileNotFoundError) as exc_info:
            load_credit_data(
                filepath=Path("nao_existe.csv"),
                use_cache=False
            )
        
        assert "nao_existe.csv" in str(exc_info.value)
    
    def test_raises_valueerror_for_empty_csv(self, mocker, tmp_path):
        """
        Verifica que levanta ValueError para CSV vazio.
        """
        # ARRANGE
        # Criar CSV vazio (só header)
        empty_csv = tmp_path / "empty.csv"
        pd.DataFrame(columns=["col1", "col2"]).to_csv(empty_csv, index=False)
        
        # Mock cache não existir
        mocker.patch.object(
            Path,
            "exists",
            lambda self: str(self) == str(empty_csv)
        )
        
        # ACT & ASSERT
        with pytest.raises(ValueError) as exc_info:
            load_credit_data(filepath=empty_csv, use_cache=False)
        
        assert "vazio" in str(exc_info.value)