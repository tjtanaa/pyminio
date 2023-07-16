from dotenv import load_dotenv
import os
from pathlib import Path

ENV_PATH = Path(__file__).parent / ".env"

if ENV_PATH.exists():
    load_dotenv(ENV_PATH)
else:
    raise FileNotFoundError("`.env` file is not created. ")
