# insert data

from database import SessionLocal
from models import User

session = SessionLocal()

try:
    while True:
        user_name = input("Enter User name: ")
        user_email = input("Enter User email: ")

        user = User(
            name = user_name, 
            email = user_email
        )

        session.add(user)

        session.commit()

        print("User Added Successfully")

        print(f"Id: {user.id}")
        print(f"Username: {user.name}")
        print(f"User email: {user.email}")

        choice = input(
            "\nDo you want to add more user? (Y/N):"
        ).strip().upper()

        if choice != "Y":
            break

except Exception as e:
    session.rollback()
    print("Error", e)

finally:
    session.close()
