def analyze(client_data, approval_threshold=0.5):
    # valida presença
    if client_data is None:
        return {"error": "no data"}
    if "age" not in client_data:
        return {"error": "no age"}
    if "limit" not in client_data:
        return {"error": "no limit"}
    if "history" not in client_data:
        return {"error": "no history"}
    
    # valida valores
    if client_data["age"] < 18 or client_data["age"] > 120:
        return {"error": "invalid age"}
    if client_data["limit"] <= 0:
        return {"error": "invalid limit"}
    
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