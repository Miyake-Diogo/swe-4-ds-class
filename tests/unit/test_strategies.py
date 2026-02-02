"""Testes básicos das estratégias de modelo."""

from src.models.strategies import DummyStrategy, LogisticRegressionStrategy, RandomForestStrategy


def test_random_forest_strategy_name():
    model = RandomForestStrategy(n_estimators=10)
    assert model.name == "RandomForest"


def test_logistic_strategy_name():
    model = LogisticRegressionStrategy(max_iter=100)
    assert model.name == "LogisticRegression"


def test_dummy_strategy_name():
    model = DummyStrategy(strategy="most_frequent")
    assert model.name == "Dummy"