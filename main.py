from fastapi import FastAPI
from database import session
from models import Movie
from schemas import MovieSchema, MovieTitle, FamilyFriendly, Captivating, Underrated, Visual, Sound

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Welcome to this movie API. Try /api/v1 to start your queries"}

@app.get("/api/v1/movies/title/{movie}", response_model=list[MovieSchema])
async def get_movies(movie: str):
    movies = session.query(Movie).filter(Movie.movie_title == movie).all()
    return movies

@app.get("/api/v1/movies/id/{id}", response_model=MovieSchema)
async def get_movies(id: int):
    movies = session.query(Movie).filter(Movie.id == id).first()
    return movies

@app.get("/api/v1/movies", response_model=list[MovieTitle])
async def get_movies():
    movies = session.query(Movie).all()
    return movies

@app.get("/api/v1/movies/family_friendly", response_model=list[FamilyFriendly])
async def get_family_friendly():
    movies = session.query(Movie).filter(Movie.family_friendly >= 4).all()
    return movies

@app.get("/api/v1/movies/captivating", response_model=list[Captivating])
async def get_captivating():
    movies = session.query(Movie).filter(
        Movie.pacing_efficiency >= 4, 
        Movie.immersive >= 4, 
        Movie.impactful >= 3).all()
    return movies

@app.get("/api/v1/movies/underrated", response_model=list[Underrated])
async def get_underrated():
    movies = session.query(Movie).filter(
        Movie.originality >= 4, 
        Movie.plot_quality_rating >= 4, 
        Movie.overall_feeling >= 4, 
        Movie.id > 499).all()
    return movies

@app.get("/api/v1/movies/visual", response_model=list[Visual])
async def get_captivating():
    movies = session.query(Movie).filter(
        Movie.visuals == 5, 
        Movie.visual_effects == 5).all()
    return movies

@app.get("/api/v1/movies/sound", response_model=list[Sound])
async def get_captivating():
    movies = session.query(Movie).filter(
        Movie.sound_audio_balance_issue == False, 
        Movie.sound_bgm_quality == 5,
        Movie.sound_song_tracks_quality == 5).all()
    return movies