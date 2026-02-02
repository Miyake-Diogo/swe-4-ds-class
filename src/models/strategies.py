"""
Estratégias de modelos de ML usando Strategy Pattern.

Este módulo implementa diferentes algoritmos de classificação
com uma interface unificada para facilitar experimentação.
"""

from abc import ABC, abstractmethod
from typing import Any

import numpy as np
from numpy.typing import NDArray


class ModelStrategy(ABC):
    """Interface base para estratégias de modelo."""

    @abstractmethod
    def fit(self, X: NDArray, y: NDArray) -> None:
        """Treina o modelo com dados de entrada."""
        pass

    @abstractmethod
    def predict(self, X: NDArray) -> NDArray:
        """Faz predições com o modelo treinado."""
        pass

    @abstractmethod
    def predict_proba(self, X: NDArray) -> NDArray:
        """Retorna probabilidades de predição."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Nome descritivo do modelo."""
        pass


class RandomForestStrategy(ModelStrategy):
    """Estratégia usando Random Forest."""

    def __init__(self, n_estimators: int = 100, **kwargs: Any) -> None:
        from sklearn.ensemble import RandomForestClassifier

        self._model = RandomForestClassifier(
            n_estimators=n_estimators,
            **kwargs,
        )

    def fit(self, X: NDArray, y: NDArray) -> None:
        self._model.fit(X, y)

    def predict(self, X: NDArray) -> NDArray:
        return self._model.predict(X)

    def predict_proba(self, X: NDArray) -> NDArray:
        return self._model.predict_proba(X)

    @property
    def name(self) -> str:
        return "RandomForest"


class LogisticRegressionStrategy(ModelStrategy):
    """Estratégia usando Regressão Logística."""

    def __init__(self, **kwargs: Any) -> None:
        from sklearn.linear_model import LogisticRegression

        self._model = LogisticRegression(**kwargs)

    def fit(self, X: NDArray, y: NDArray) -> None:
        self._model.fit(X, y)

    def predict(self, X: NDArray) -> NDArray:
        return self._model.predict(X)

    def predict_proba(self, X: NDArray) -> NDArray:
        return self._model.predict_proba(X)

    @property
    def name(self) -> str:
        return "LogisticRegression"


class DummyStrategy(ModelStrategy):
    """Estratégia dummy para testes e baseline."""

    def __init__(self, strategy: str = "most_frequent") -> None:
        from sklearn.dummy import DummyClassifier

        self._model = DummyClassifier(strategy=strategy)

    def fit(self, X: NDArray, y: NDArray) -> None:
        self._model.fit(X, y)

    def predict(self, X: NDArray) -> NDArray:
        return self._model.predict(X)

    def predict_proba(self, X: NDArray) -> NDArray:
        return self._model.predict_proba(X)

    @property
    def name(self) -> str:
        return "Dummy"
    
class ModelFactory:
    """Factory para criar estratégias de modelo."""

    _strategies: dict[str, type[ModelStrategy]] = {
        "random_forest": RandomForestStrategy,
        "logistic_regression": LogisticRegressionStrategy,
        "dummy": DummyStrategy,
    }

    @classmethod
    def create(cls, name: str, **kwargs: Any) -> ModelStrategy:
        """Cria uma estratégia de modelo pelo nome.

        Args:
            name: Nome do modelo (random_forest, logistic_regression, dummy)
            **kwargs: Parâmetros para o modelo

        Returns:
            Instância da estratégia de modelo

        Raises:
            ValueError: Se o nome não for reconhecido
        """
        if name not in cls._strategies:
            available = ", ".join(cls._strategies.keys())
            raise ValueError(
                f"Modelo '{name}' não encontrado. "
                f"Disponíveis: {available}"
            )
        return cls._strategies[name](**kwargs)

    @classmethod
    def register(cls, name: str, strategy: type[ModelStrategy]) -> None:
        """Registra uma nova estratégia.

        Args:
            name: Nome para o modelo
            strategy: Classe da estratégia
        """
        cls._strategies[name] = strategy

    @classmethod
    def available(cls) -> list[str]:
        """Retorna nomes de modelos disponíveis."""
        return list(cls._strategies.keys())
    
