from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///viana_kalista.db')

Session = sessionmaker(bind=engine)
session = Session()
