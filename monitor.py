import random

def check_services():
    services = ["Email", "Database", "API"]

    status = {
        service: random.choice(["running", "stopped"])
        for service in services
    }

    return status
