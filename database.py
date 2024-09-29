from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'mysql+pymysql://root:Sundar@localhost/GraphQL'

db_engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=db_engine)

base=declarative_base()



