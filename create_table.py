# create_tables.py
from database import engine
from models import Base

Base.metadata.create_all(engine)
print("Tables created (if they didn't already exist)")