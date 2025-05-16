from typing import Union
import redis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import json
import re
import ast
import os

app = FastAPI()
r = None

# Connect to Redis
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
r = redis.Redis.from_url(redis_url)
backend_url = os.getenv("BACKEND_URL")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/cached_api")
def get_cached_data():
    cache_key = "cnn-viz-2"
    cached_data = r.get(cache_key)
    if cached_data:
        dict_data = ast.literal_eval(cached_data.decode())
        return json.dumps(dict_data)
    response = requests.get(backend_url).json()
    # response = "cached_data"
    r.set(cache_key, f'{response}')
    return {"data": response, "source": "original_api"}


if __name__ == "__main__":
    import uvicorn
    # r = redis.Redis(host="localhost", port=6379)
    uvicorn.run(app, host="0.0.0.0", port=8000) 