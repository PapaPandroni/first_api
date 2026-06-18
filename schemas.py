import ast
from pydantic import BaseModel, field_validator

class MovieSchema(BaseModel):
    id: int
    movie_title : str
    pacing_efficiency : int
    originality :int
    family_friendly : int
    plot_quality_rating : int
    plot_quality_reasons_for_liking : str
    plot_quality_reasons_for_disliking : str
    dialogues : int
    end_feeling_emotional_adjective : str
    end_feeling_ending_rating : int
    end_feeling_structural_adjective : str
    immersive : int
    impactful : int
    overall_feeling : int
    visuals : int
    visual_effects : int
    sound_audio_balance_issue : bool
    sound_bgm_quality : int
    sound_song_tracks_quality : int
    performance_of_actors : int
    connected : int
    references_contained : int
    cognitive_requirement : int
    technical_knowledge_required : int
    photosensitivity_warnings : int
    animal_harm : int
    trailer_or_spoiler : int

    class Config:
        from_attributes = True

class MovieTitle(BaseModel):
    id: int
    movie_title: str
    class Config:
        from_attributes = True

class FamilyFriendly(BaseModel):
    id: int
    movie_title: str
    family_friendly: int
    overall_feeling: int
    plot_quality_rating: int
    plot_quality_reasons_for_liking: list[str]

    @field_validator("plot_quality_reasons_for_liking", mode="before")
    @classmethod
    def parse_list(cls, v):
        if isinstance(v, str):
            return ast.literal_eval(v)
        return v

    class Config:
        from_attributes = True

class Captivating(BaseModel):
    id: int
    movie_title: str
    pacing_efficiency: int
    immersive: int
    impactful: int
    
    class Config:
        from_attributes = True

class Underrated(BaseModel):
    id: int
    movie_title: str
    originality: int
    plot_quality_rating: int
    overall_feeling: int
    plot_quality_reasons_for_liking: list[str]

    @field_validator("plot_quality_reasons_for_liking", mode="before")
    @classmethod
    def parse_list(cls, v):
        if isinstance(v, str):
            return ast.literal_eval(v)
        return v
    
    class Config:
        from_attributes = True

class Visual(BaseModel):
    id: int
    movie_title: str
    visuals: int
    visual_effects: int

    class Config:
        from_attributes = True

class Sound(BaseModel):
    id: int
    movie_title: str
    sound_audio_balance_issue: bool
    sound_bgm_quality: int
    sound_song_tracks_quality: int

    class Config:
        from_attributes = True

class FeelGood(BaseModel):
    id: int
    movie_title: str
    overall_feeling: int
    end_feeling_ending_rating: int
    end_feeling_structural_adjective: str
    connected: int

    class Config:
        from_attributes = True

class Background(BaseModel):
    id: int
    movie_title: str
    cognitive_requirement: int
    pacing_efficiency: int
    technical_knowledge_required: int
    references_contained: int
    originality: int

    class Config:
        from_attributes = True

class TrailerMovie(BaseModel):
    id: int
    movie_title: str
    trailer_or_spoiler: int

    class Config:
        from_attributes = True

class Challenging(BaseModel):
    id: int
    movie_title: str
    technical_knowledge_required: int
    cognitive_requirement: int
    references_contained: int
    originality: int

    class Config:
        from_attributes = True