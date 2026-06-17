import pandas as pd
from database import engine

df = pd.read_csv("/Users/peremil/Documents/project/first_api/Cinatomy/cinatomy_movie_profiles.csv")
df.index.name = "id"
df.to_sql("movies", con=engine, if_exists="replace", index=True)
print("Done with ingesting to database")
