# Update Data

from database import SessionLocal
from models import User

session = SessionLocal()

try:

    user_id = int(input("Enter user id: "))

    user = session.query(User).filter(
        User.id == user_id
    ).first()

    if user:
        new_name = input("Enter new name: ")

        user.name = new_name

        session.commit()
        print("User updated Successfully")
    else:        
        print("User not found")

except Exception as e:
    session.rollback()
    print(f"Error occurred: {e}")
finally:
    session.close()