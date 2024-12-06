from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Director
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def delete_director(session, director_id):
    director = session.query(Director).filter(Director.id == director_id).one_or_none()
    if director:
        session.delete(director) 
        session.commit()  
# END
