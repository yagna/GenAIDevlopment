from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    director: str
    genre: str
    year: int
    rating: float

class MovieResponse(BaseModel):
    id: int
    title: str
    director: str
    genre: str
    year: int
    rating: float
    
    class Config:
        from_attributes = True