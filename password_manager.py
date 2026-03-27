import random
import string
from logger import log_info

def generate_password(length=10):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def reset_password(username):
    new_password = generate_password()
    log_info(f"Password reset for {username}")
    return new_password
