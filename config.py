import json


def get_secret(key):
    with open("secrets.json", "r", encoding="utf-8") as file:
        secrets = json.load(file)
    return secrets[key]
