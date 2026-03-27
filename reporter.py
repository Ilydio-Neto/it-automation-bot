import pandas as pd
from user_manager import load_users

def generate_user_report(output_path):
    users = load_users()
    df = pd.DataFrame(users)
    df.to_csv(output_path, index=False)
