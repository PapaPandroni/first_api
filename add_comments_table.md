# run this in the database

CREATE TABLE (
    id INTEGER PRIMARY KEY AUTOINCRAMENT,
    movie_id INTEGER,
    comment TEXT,
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);