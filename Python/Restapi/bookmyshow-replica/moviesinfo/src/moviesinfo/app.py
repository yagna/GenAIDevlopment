from fastapi import FastAPI, HTTPException
from sqlalchemy import text, select
from sqlalchemy.ext.asyncio import AsyncSession
from .db import AsyncSessionLocal, create_tables
from .models import Movie
from .schemas import MovieCreate, MovieResponse
from typing import List

app = FastAPI(title="Movies Info Service", version="1.0.0")

@app.on_event("startup")
async def startup_event():
    import asyncio
    await asyncio.sleep(2)  # Wait for database to be ready
    await create_tables()

@app.get("/")
async def health_check():
    try:
        async with AsyncSessionLocal() as session:
            result = await session.execute(text("SELECT 1"))
            await session.commit()
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}

@app.get("/movies", response_model=List[MovieResponse])
async def get_movies():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Movie))
        movies = result.scalars().all()
        return movies

@app.get("/movies/{movie_id}", response_model=MovieResponse)
async def get_movie(movie_id: int):
    async with AsyncSessionLocal() as session:
        movie = await session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return movie

@app.post("/movies", response_model=MovieResponse, status_code=201)
async def create_movie(movie: MovieCreate):
    async with AsyncSessionLocal() as session:
        db_movie = Movie(**movie.dict())
        session.add(db_movie)
        await session.commit()
        await session.refresh(db_movie)
        return db_movie

@app.put("/movies/{movie_id}", response_model=MovieResponse)
async def update_movie(movie_id: int, movie: MovieCreate):
    async with AsyncSessionLocal() as session:
        db_movie = await session.get(Movie, movie_id)
        if not db_movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        
        for field, value in movie.dict().items():
            setattr(db_movie, field, value)
        
        await session.commit()
        await session.refresh(db_movie)
        return db_movie

@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int):
    async with AsyncSessionLocal() as session:
        movie = await session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        
        await session.delete(movie)
        await session.commit()
        return {"message": "Movie deleted successfully"}