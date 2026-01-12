import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.ext.declarative import declarative_base
from src.config.config import Config

engine = sa.create_engine(Config.DATABASE_URI)
Session = orm.sessionmaker(bind=engine)
session = Session()

Base = declarative_base()