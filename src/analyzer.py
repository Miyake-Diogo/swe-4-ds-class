REQUIRED_FIELDS = ["age", "limit", "history"]
MIN_AGE = 18
MAX_AGE = 120


def _validate_client_data(client_data: dict | None) -> str | None:
    """Valida dados do cliente.
    
    Returns:
        Mensagem de erro ou None se válido.
    """
    if client_data is None:
        return "no data"
    
    # Verifica campos obrigatórios
    for field in REQUIRED_FIELDS:
        if field not in client_data:
            return f"no {field}"
    
    # Valida valores
    if not (MIN_AGE <= client_data["age"] <= MAX_AGE):
        return "invalid age"
    if client_data["limit"] <= 0:
        return "invalid limit"
    
    return None



def analyze(client_data: dict | None, approval_threshold: float = 0.5) -> dict | None:
    # Validação extraída
    error = _validate_client_data(client_data)
    if error:
        return {"error": error}
    
    # calcula score
    score = 0
    
    # pontos por idade
    age = client_data["age"]
    if age >= 18 and age < 25:
        score = score + 10
    elif age >= 25 and age < 35:
        score = score + 20
    elif age >= 35 and age < 50:
        score = score + 30
    elif age >= 50:
        score = score + 25
    
    # pontos por limite
    credit_limit = client_data["limit"]
    if credit_limit < 1000:
        score = score + 5
    elif credit_limit < 5000:
        score = score + 15
    elif credit_limit < 10000:
        score = score + 25
    else:
        score = score + 35
    
    # pontos por histórico
    history = client_data["history"]
    if history == "good":
        score = score + 40
    elif history == "regular":
        score = score + 20
    elif history == "bad":
        score = score + 5
    
    # normaliza score
    normalized_score = score / 100
    
    # decide aprovação
    if normalized_score >= approval_threshold:
        status = "approved"
    else:
        status = "rejected"
    
    return {"status": status, "score": normalized_score}