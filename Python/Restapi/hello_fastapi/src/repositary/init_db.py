from database import Base, engine
from models import Book, Member, BorrowRecord

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Done!")
