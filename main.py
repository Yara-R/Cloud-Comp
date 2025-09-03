from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/auth/me")
async def auth_me(request: Request):
    data = await request.json()
    usuario = data.get("user", "desconhecido")
    return {"user": usuario, "ping": "pong"}
