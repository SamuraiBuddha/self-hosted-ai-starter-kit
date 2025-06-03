from fastapi import FastAPI

app = FastAPI(title="MCP Revit Server Mock")

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "mcp-revit-mock"}

@app.post("/mcp")
async def mcp_endpoint(request: dict):
    return {"jsonrpc": "2.0", "result": {"message": "Mock response"}, "id": request.get("id")}
