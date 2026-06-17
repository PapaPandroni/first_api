from fastapi import FastAPI
from database import session
from models import Movie
from schemas import MovieSchema, MovieTitle, FamilyFriendly

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Welcome to this movie API. Try /api/v1 to start your queries"}

@app.get("/api/v1/movies", response_model=list[MovieTitle])
async def get_movies():
    movies = session.query(Movie).all()
    return movies

@app.get("/api/v1/family_friendly", response_model=list[FamilyFriendly])
async def get_family_friendly():
    movies = session.query(Movie).filter(Movie.family_friendly >= 4).all()
    return movies
    

