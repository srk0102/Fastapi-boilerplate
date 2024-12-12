import os
from dotenv import load_dotenv

load_dotenv()


ENVIRONMENT=os.environ.get('ENVIRONMENT')
PORT=int(os.environ.get('PORT'))

PYTHONDONTWRITEBYTECODE=os.environ.get('PYTHONDONTWRITEBYTECODE')

IP_INFO_API_KEY=os.environ.get('IP_INFO_API_KEY')

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")
