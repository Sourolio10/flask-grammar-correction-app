import os
from sqlalchemy import create_engine
from urllib.parse import quote 
DB_HOST = 'localhost'
DB_PORT = 3306
DB_USERNAME = 'root'
DB_PASSWORD = 'Sourolo@10'
DB_NAME = 'grammar'
#mysql://username:password@localhost/db_name
CONNECTION_STRING = 'mysql://{username}:%s@{host}:{port}/{db_name}'.format(username=DB_USERNAME,host=DB_HOST,port=DB_PORT,db_name=DB_NAME)
print(CONNECTION_STRING)
engine = create_engine(CONNECTION_STRING % quote(DB_PASSWORD))