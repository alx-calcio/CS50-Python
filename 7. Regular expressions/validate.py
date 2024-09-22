"""
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
"""

import re

email = input("What's your email? ").strip()

if re.search(
    r"^\w+@\w+\.edu$", email, flags=re.IGNORECASE
):  # premier paramètre pour les exigences, deuxième pour la variable et le troisième pour une configuration spéciale
    print("Valid")
else:
    print("Invalid")
