from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from util.db_property_util import get_db_url

engine = create_engine(get_db_url())
Session = sessionmaker(bind=engine)

def get_session():
    return Session()
