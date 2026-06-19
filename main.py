from fastapi import FastAPI
from typing import Optional
from database import session
from models import Movie, Comment
from fastapi import HTTPException
from schemas import MovieSchema, MovieTitle, FamilyFriendly, Captivating, Underrated, Visual, Sound, FeelGood, Background, TrailerMovie, Challenging

app = FastAPI()

url = "http://127.0.0.1:8000/docs"

@app.get("/")
async def home():
    return {"message": f"Welcome to this movie API. Try {url} to read the documentation"}

@app.get("/api/v1/movies/search", response_model=list[MovieSchema])
async def search_movies(
    pacing_efficiency: Optional[int] = None,
    originality: Optional[int] = None,
    family_friendly: Optional[int] = None,
    plot_quality_rating: Optional[int] = None,
    dialogues: Optional[int] = None,
    end_feeling_ending_rating: Optional[int] = None,
    immersive: Optional[int] = None,
    impactful: Optional[int] = None,
    overall_feeling: Optional[int] = None,
    visuals: Optional[int] = None,
    visual_effects: Optional[int] = None,
    sound_audio_balance_issue: Optional[bool] = None,
    sound_bgm_quality: Optional[int] = None,
    sound_song_tracks_quality: Optional[int] = None,
    performance_of_actors: Optional[int] = None,
    connected: Optional[int] = None,
    references_contained: Optional[int] = None,
    cognitive_requirement: Optional[int] = None,
    technical_knowledge_required: Optional[int] = None,
    photosensitivity_warnings: Optional[int] = None,
    animal_harm: Optional[int] = None,
    trailer_or_spoiler: Optional[int] = None,
):
    query = session.query(Movie)

    if pacing_efficiency is not None:
        query = query.filter(Movie.pacing_efficiency >= pacing_efficiency)
    if originality is not None:
        query = query.filter(Movie.originality >= originality)
    if family_friendly is not None:
        query = query.filter(Movie.family_friendly >= family_friendly)
    if plot_quality_rating is not None:
        query = query.filter(Movie.plot_quality_rating >= plot_quality_rating)
    if dialogues is not None:
        query = query.filter(Movie.dialogues >= dialogues)
    if end_feeling_ending_rating is not None:
        query = query.filter(Movie.end_feeling_ending_rating >= end_feeling_ending_rating)
    if immersive is not None:
        query = query.filter(Movie.immersive >= immersive)
    if impactful is not None:
        query = query.filter(Movie.impactful >= impactful)
    if overall_feeling is not None:
        query = query.filter(Movie.overall_feeling >= overall_feeling)
    if visuals is not None:
        query = query.filter(Movie.visuals >= visuals)
    if visual_effects is not None:
        query = query.filter(Movie.visual_effects >= visual_effects)
    if sound_audio_balance_issue is not None:
        query = query.filter(Movie.sound_audio_balance_issue == sound_audio_balance_issue)
    if sound_bgm_quality is not None:
        query = query.filter(Movie.sound_bgm_quality >= sound_bgm_quality)
    if sound_song_tracks_quality is not None:
        query = query.filter(Movie.sound_song_tracks_quality >= sound_song_tracks_quality)
    if performance_of_actors is not None:
        query = query.filter(Movie.performance_of_actors >= performance_of_actors)
    if connected is not None:
        query = query.filter(Movie.connected >= connected)
    if references_contained is not None:
        query = query.filter(Movie.references_contained >= references_contained)
    if cognitive_requirement is not None:
        query = query.filter(Movie.cognitive_requirement >= cognitive_requirement)
    if technical_knowledge_required is not None:
        query = query.filter(Movie.technical_knowledge_required >= technical_knowledge_required)
    if photosensitivity_warnings is not None:
        query = query.filter(Movie.photosensitivity_warnings <= photosensitivity_warnings)
    if animal_harm is not None:
        query = query.filter(Movie.animal_harm <= animal_harm)
    if trailer_or_spoiler is not None:
        query = query.filter(Movie.trailer_or_spoiler <= trailer_or_spoiler)

    return query.all()

@app.get("/api/v1/movies/title/{movie}", response_model=list[MovieSchema])
async def get_movie_by_title(movie: str):
    movies = session.query(Movie).filter(Movie.movie_title == movie).all()
    if not movies:
        raise HTTPException(status_code=404, detail="No movie found with that title")
    return movies

@app.get("/api/v1/movies/id/{id}", response_model=MovieSchema)
async def get_movie_by_id(id: int):
    movie = session.query(Movie).filter(Movie.id == id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail="No movie found with that id. Try 0-999")
    return movie

@app.get("/api/v1/movies", response_model=list[MovieTitle])
async def get_all_movies():
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
async def get_visual():
    movies = session.query(Movie).filter(
        Movie.visuals == 5, 
        Movie.visual_effects == 5).all()
    return movies

@app.get("/api/v1/movies/sound", response_model=list[Sound])
async def get_sound():
    movies = session.query(Movie).filter(
        Movie.sound_audio_balance_issue == False, 
        Movie.sound_bgm_quality == 5,
        Movie.sound_song_tracks_quality == 5).all()
    return movies

@app.get("/api/v1/movies/feelgood", response_model=list[FeelGood])
async def get_feelgood():
    movies = session.query(Movie).filter(
        Movie.overall_feeling >= 4,
        Movie.end_feeling_ending_rating >= 4,
        Movie.end_feeling_structural_adjective.in_(["satisfying", "earned"]),
        Movie.connected >= 4).all()
    return movies

@app.get("/api/v1/movies/background", response_model=list[Background])
async def get_background():
    movies = session.query(Movie).filter(
        Movie.cognitive_requirement <= 2,
        Movie.pacing_efficiency >= 4,
        Movie.originality <= 2,
        Movie.references_contained <= 2,
        Movie.technical_knowledge_required <= 2).all()
    return movies

@app.get("/api/v1/movies/trailermovie", response_model=list[TrailerMovie])
async def get_trailermovie():
    movies = session.query(Movie).filter(
        Movie.trailer_or_spoiler == 5).all()
    return movies

@app.get("/api/v1/movies/challenging", response_model=list[Challenging])
async def get_challenging():
    movies = session.query(Movie).filter(
        Movie.cognitive_requirement >= 4,
        Movie.technical_knowledge_required >= 4,
        Movie.references_contained >= 4,
        Movie.originality >= 4).all()
    return movies

@app.post("/api/v1/movies/{id}/comments")
async def add_comment(id: int, comment: str):
    new_comment = Comment(movie_id = id, comment = comment)
    session.add(new_comment)
    session.commit()
    return new_comment