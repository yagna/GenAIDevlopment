from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional, List

# ---------------------------
# Book Schemas
# ---------------------------
class BookBase(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    available: Optional[bool] = None


class BookResponse(BookBase):
    id: int
    available: bool

    class Config:
        orm_mode = True  # allows reading ORM objects directly


# ---------------------------
# Member Schemas
# ---------------------------
class MemberBase(BaseModel):
    name: str
    email: EmailStr


class MemberCreate(MemberBase):
    pass


class MemberResponse(MemberBase):
    id: int
    join_date: datetime

    class Config:
        orm_mode = True


# ---------------------------
# BorrowRecord Schemas
# ---------------------------
class BorrowRecordBase(BaseModel):
    book_id: int
    member_id: int


class BorrowRecordCreate(BorrowRecordBase):
    pass


class BorrowRecordResponse(BorrowRecordBase):
    id: int
    borrow_date: datetime
    return_date: Optional[datetime] = None

    class Config:
        orm_mode = True
