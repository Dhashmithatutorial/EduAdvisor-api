from dotenv import load_dotenv
import os

load_dotenv()

# Configuration with safe defaults so the app can run in serverless
# or local environments without a .env file. For production, set
# environment variables in your hosting provider (Vercel, GitHub Actions, etc.).
DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:///./database.db"
SECRET_KEY = os.getenv("SECRET_KEY") or "change-me-in-production"
ALGORITHM = os.getenv("ALGORITHM") or "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
)