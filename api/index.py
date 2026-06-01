"""Vercel serverless entrypoint.

Vercel will invoke this file for requests under `/api/...`.
We expose the FastAPI app instance defined in `backend.main` as `app`.
"""
from backend.main import app

app = app
