"""Testes para analyzer - garantem comportamento durante refatoração."""

import pytest
from src.analyzer import analyze


class TestAnalyze:
    """Testes de caracterização para analyze."""

    def test_valid_young_low_limit_good_history(self):
        data = {"age": 20, "limit": 500, "history": "good"}
        result = analyze(data)
        
        assert result["status"] == "approved"
        assert result["score"] == pytest.approx(0.55)

    def test_valid_middle_age_high_limit_bad_history(self):
        data = {"age": 40, "limit": 15000, "history": "bad"}
        result = analyze(data)
        
        assert result["status"] == "approved"
        assert result["score"] == pytest.approx(0.70)  # 30 + 35 + 5

    def test_missing_age(self):
        result = analyze({"limit": 1000, "history": "good"})
        assert result == {"error": "no age"}

    def test_invalid_age(self):
        result = analyze({"age": 15, "limit": 1000, "history": "good"})
        assert result == {"error": "invalid age"}

    def test_none_data(self):
        result = analyze(None)
        assert result == {"error": "no data"}

    def test_custom_threshold(self):
        data = {"age": 20, "limit": 500, "history": "good"}
        
        result_low = analyze(data, 0.3)
        result_high = analyze(data, 0.9)
        
        assert result_low["status"] == "approved"
        assert result_high["status"] == "rejected"