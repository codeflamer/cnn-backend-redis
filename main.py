from typing import Union
import redis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import json
import re
import ast

app = FastAPI()
r = None
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
    response = requests.get("https://cnn-viz-production.up.railway.app/all_layers").json()
    # response = "cached_data"
    r.setex(cache_key, 360000, f'{response}')
    return {"data": response, "source": "original_api"}


if __name__ == "__main__":
    import uvicorn
    r = redis.Redis(host="localhost", port=6379)
    uvicorn.run(app, host="0.0.0.0", port=8000) 