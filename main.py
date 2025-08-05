from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/hello")
def hello():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return {
        "message": f"Hallo Sharif! 👋 Deze begroeting komt realtime uit Raymond's eigen FastAPI-backend, op {now} verzonden 🚀"
    }
