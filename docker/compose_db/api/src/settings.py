import os
from dotenv import load_dotenv
load_dotenv()

class DB_CONFIG:
    DB=os.getenv("POSTGRES_DB")
    HOST=os.getenv("POSTGRES_HOST")
    USER=os.getenv("POSTGRES_USER")
    PASSWORD=os.getenv("POSTGRES_PASSWORD")
    PORT=os.getenv("POSTGRES_PORT")