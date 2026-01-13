import re

def check_password_strength(password):
    """
    Avalia a força de uma senha com base em critérios de segurança.
    """
    strength = 0
    feedback = []

    # Critério 1: Comprimento
    if len(password) >= 12:
        strength += 1
    else:
        feedback.append("❌ Muito curta (mínimo 12 caracteres).")

    # Critério 2: Letras Maiúsculas e Minúsculas
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("❌ Misture letras MAIÚSCULAS e minúsculas.")

    # Critério 3: Números
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("❌ Adicione pelo menos um número (0-9).")

    # Critério 4: Símbolos/Caracteres Especiais
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("❌ Use caracteres especiais (ex: @, #, $).")

    # Avaliação Final
    ratings = {
        0: "MUITO FRACA 🚨",
        1: "FRACA ⚠️",
        2: "MODERADA ⚖️",
        3: "FORTE ✅",
        4: "MUITO FORTE 💪"
    }
    
    return ratings.get(strength), feedback