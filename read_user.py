# Read Data


from database import SessionLocal
from models import User

session = SessionLocal()

try:
    users = session.query(User).all()

    if not users:
        print("No users found")

    for user in users:
        print(
            f"ID: {user.id},"
            f"Name: {user.name},"
            f"Email: {user.email}"
        )

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    session.close()