
from sqlalchemy import create_engine, column, Integer, String, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Dog

Base = declarative_base()

def create_table(base, engine):
    base.metadata.create_all(engine)

engine = create_engine("sqlite:///dogs.db")
create_table(Base, engine)  
Session = sessionmaker(bind=engine)
session = Session()



def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    all_dogs = session.query(Dog).all()
    return all_dogs
    pass

def find_by_name(session, name):
    matches = session.query(Dog).filter_by(name=name).first()
    return matches
    pass

def find_by_id(session, id):
    return session.query(Dog).get(id)
    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()
    pass

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    pass