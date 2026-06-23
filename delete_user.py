# Delete Data

from sqlalchemy.orm import sessionmaker
from database import SessionLocal, engine
from models import User

session = SessionLocal()

try:
    user_id = int(input("Enter user id: "))

    user = session.query(User).filter(
        User.id == user_id
    ).first()

    if user:
        session.delete(user)
        session.commit()
        print("User deleted")
    else:
        print("User not found")
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    session.close()