import json
from pathlib import Path
from logger import log_info

DATA_PATH = Path("../data/users.json")

def load_users():
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DATA_PATH, "w") as f:
        json.dump(users, f, indent=2)

def create_user(username, email):
    users = load_users()

    new_user = {
        "username": username,
        "email": email,
        "status": "active"
    }

    users.append(new_user)
    save_users(users)

    log_info(f"User created: {username}")

    return new_user
