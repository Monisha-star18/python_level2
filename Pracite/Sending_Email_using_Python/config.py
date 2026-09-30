import os
from dotenv import load_dotenv

load_dotenv()

def get_password () -> str | None :
    return os.getenv("APP_PASSWORD",default=None)

