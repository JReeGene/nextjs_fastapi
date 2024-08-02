from pathlib import Path
import os
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
class Settings:
    PROJECT_TITLE: str = 'Fullstack NextJS/FastAPI Site'
    PROJECT_VERSION: str = '0.0.1'

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER:str = os.getenv('POSTGRES_SERVER', 'localhost')
    POSTGRES_PORT:str = os.getenv('POSTGRES_PORT', 5432) #DEFAULT
    POSTGRES_DB:str = os.getenv('POSTGRES_DB', 'nextjs_fastapi_db')
    DATABASE_URL: str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

settings = Settings()