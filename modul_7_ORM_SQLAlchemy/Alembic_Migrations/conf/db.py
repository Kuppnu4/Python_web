import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URI: postgresql://username:password@domain.port/database

file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
# set the path to config.ini file
config = configparser.ConfigParser()
config.read(file_config)

'''
pull the config data from file config.ini
'''

user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
domain = config.get('DEV_DB', 'DOMAIN')
port = config.get('DEV_DB', 'PORT')
db = config.get('DEV_DB', 'DB_NAME')

URI = f'postgresql://{user}:{password}@{domain}:{port}/{db}'

engine = create_engine(URI, echo=True, pool_size=5, max_overflow=0)
DBSession = sessionmaker(bind=engine)
session = DBSession()
'''
we have created the block connecting to DB
'''
