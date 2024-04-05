import os
from sqlalchemy import create_engine
from urllib.parse import quote

# Load environment variables
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

CONNECTION_STRING = f'mysql://{DB_USERNAME}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}' % quote(DB_PASSWORD)
print(CONNECTION_STRING)
engine = create_engine(CONNECTION_STRING)
