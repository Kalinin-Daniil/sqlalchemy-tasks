from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie, Director
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def get_movies_with_directors(session):
    movies_with_directors = session.query(Movie).join(Director).order_by(Movie.title).all()
    
    result = [
        f"{movie.title} by {movie.director.name}, released on {movie.release_date}, duration: {movie.duration} min, genre: {movie.genre}, rating: {movie.rating}"
        for movie in movies_with_directors
    ]
    
    return result
# END
