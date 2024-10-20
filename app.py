from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import os

app = FastAPI()

# Serve static files (for CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="templates")

# Load messages from CSV
def load_messages():
    if os.path.exists("messages.csv"):
        df = pd.read_csv("messages.csv")
        return df['message'].tolist()
    else:
        return ["Chúc mừng Ngày Phụ nữ Việt Nam!"]

# Home route
@app.get("/")
async def read_root(request: Request):
    messages = load_messages()  # Load messages from CSV
    return templates.TemplateResponse("index.html", {"request": request, "messages": messages})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
