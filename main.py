import argparse
from user_manager import create_user
from password_manager import reset_password
from monitor import check_services
from reporter import generate_user_report

def main():
    parser = argparse.ArgumentParser(description="IT Automation Bot")

    parser.add_argument("--create-user", nargs=2, metavar=("username", "email"))
    parser.add_argument("--reset-password", metavar="username")
    parser.add_argument("--monitor", action="store_true")
    parser.add_argument("--report", metavar="output_path")

    args = parser.parse_args()

    if args.create_user:
        username, email = args.create_user
        user = create_user(username, email)
        print(f"User created: {user}")

    elif args.reset_password:
        password = reset_password(args.reset_password)
        print(f"New password: {password}")

    elif args.monitor:
        status = check_services()
        print("Service status:")
        for k, v in status.items():
            print(f"{k}: {v}")

    elif args.report:
        generate_user_report(args.report)
        print(f"Report generated at {args.report}")

    else:
        print("No command provided.")

if __name__ == "__main__":
    main()
