# tests/unit/test_example.py
def test_sample_data_has_correct_columns(sample_credit_data):
    """
    Teste que usa a fixture sample_credit_data.
    
    A fixture é injetada automaticamente pelo nome do parâmetro.
    """
    expected_columns = ["ID", "LIMIT_BAL", "SEX", "EDUCATION"]
    for col in expected_columns:
        assert col in sample_credit_data.columns


def test_sample_data_has_five_rows(sample_credit_data):
    """Outro teste usando a mesma fixture."""
    assert len(sample_credit_data) == 5

    