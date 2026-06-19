from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies" 

    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_title = Column(String)
    pacing_efficiency = Column(Integer)
    originality = Column(Integer)
    family_friendly = Column(Integer)
    plot_quality_rating = Column(Integer)
    plot_quality_reasons_for_liking = Column(String)   # stored as raw string
    plot_quality_reasons_for_disliking = Column(String)
    dialogues = Column(Integer)
    end_feeling_emotional_adjective = Column(String)
    end_feeling_ending_rating = Column(Integer)
    end_feeling_structural_adjective = Column(String)
    immersive = Column(Integer)
    impactful = Column(Integer)
    overall_feeling = Column(Integer)
    visuals = Column(Integer)
    visual_effects = Column(Integer)
    sound_audio_balance_issue = Column(Boolean)
    sound_bgm_quality = Column(Integer)
    sound_song_tracks_quality = Column(Integer)
    performance_of_actors = Column(Integer)
    connected = Column(Integer)
    references_contained = Column(Integer)
    cognitive_requirement = Column(Integer)
    technical_knowledge_required = Column(Integer)
    photosensitivity_warnings = Column(Integer)
    animal_harm = Column(Integer)
    trailer_or_spoiler = Column(Integer)
    comments = relationship("Comment", back_populates="movie")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    comment = Column(String)

    movie = relationship("Movie", back_populates="comments")

