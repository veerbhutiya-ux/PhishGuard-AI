# List of suspicious keywords

SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify",
    "password",
    "otp",
    "bank",
    "account",
    "click",
    "immediately",
    "suspended",
    "login",
    "debit card",
    "credit card",
    "cvv",
    "reward",
    "prize",
    "winner"
]



def detect_phishing(email):

    email = email.lower()

    found_keywords = []
    score = 0

    for word in SUSPICIOUS_KEYWORDS:

        if word in email:
            found_keywords.append(word)
            score += 10

    if score > 100:
        score = 100

    if score >= 70:
        risk = "High"

    elif score >= 40:
        risk = "Medium"

    else:
        risk = "Low"

    # AI Explanation

    if risk == "High":

        explanation = (
            "This email has been classified as HIGH RISK because it contains "
            "multiple phishing indicators such as urgent language, requests for "
            "sensitive information, banking-related terms, and suspicious actions "
            "that are commonly used in phishing attacks."
        )

    elif risk == "Medium":

        explanation = (
            "This email contains several suspicious characteristics. "
            "Users should carefully verify the sender before taking any action."
        )

    else:

        explanation = (
            "Very few phishing indicators were detected. "
            "However, users should always remain cautious when opening emails."
        )

    return {
        "score": score,
        "risk": risk,
        "keywords": found_keywords,
        "explanation": explanation
    }