from typing import Callable

class TrainingObserver:
    """Observador simples para eventos de treinamento."""

    def __init__(self) -> None:
        self._callbacks: list[Callable[[dict], None]] = []

    def register(self, callback: Callable[[dict], None]) -> None:
        """Registra callback para eventos."""
        self._callbacks.append(callback)

    def notify(self, event: dict) -> None:
        """Notifica todos os callbacks."""
        for callback in self._callbacks:
            callback(event)


# Uso
observer = TrainingObserver()

# Registrar callbacks
observer.register(lambda e: print(f"Época {e['epoch']}: loss={e['loss']:.4f}"))
observer.register(lambda e: mlflow.log_metric("loss", e["loss"], step=e["epoch"]))

# Durante treinamento
for epoch in range(10):
    loss = train_one_epoch()
    observer.notify({"epoch": epoch, "loss": loss})