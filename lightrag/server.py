#!/usr/bin/env python3
"""
LightRAG Server for RevitAI
Placeholder - replace with actual server from artifacts
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI(title="LightRAG Server for RevitAI")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "lightrag-revitai"}

@app.get("/")
async def root():
    return {"message": "LightRAG server is running. Replace this with actual implementation."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
