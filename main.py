from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import hashlib
import sqlite3
from fastapi import Request

app = FastAPI()

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 for templating
templates = Jinja2Templates(directory="templates")

# Connect to SQLite database
conn = sqlite3.connect('urls.db', check_same_thread=False)
cursor = conn.cursor()

# Create the table to store URLs if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    long_url TEXT,
    short_code TEXT
)
''')


class URLRequest(BaseModel):
    long_url: str


# Homepage route: Serve a basic HTML form
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Shorten URL route
@app.post("/shorten")
async def shorten_url(url_request: URLRequest):
    long_url = url_request.long_url

    # Check if the URL already exists in the database
    cursor.execute("SELECT short_code FROM urls WHERE long_url = ?", (long_url,))
    result = cursor.fetchone()
    if result:
        # If the URL exists, return the existing short URL
        return {"short_url": f"http://localhost:8000/{result[0]}"}

    # Generate a unique short code for the URL using a hash function
    short_code = hashlib.md5(long_url.encode()).hexdigest()[:6]

    # Insert the URL and short code into the database
    cursor.execute("INSERT INTO urls (long_url, short_code) VALUES (?, ?)", (long_url, short_code))
    conn.commit()

    # Construct the short URL
    short_url = f"http://localhost:8000/{short_code}"

    return {"short_url": short_url}


# Redirect to the long URL using the short code
@app.get("/{short_code}")
async def redirect_to_long_url(short_code: str):
    # Look up the long URL associated with the short code
    cursor.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    result = cursor.fetchone()

    if result:
        # Redirect to the long URL
        return RedirectResponse(url=result[0])
    else:
        raise HTTPException(status_code=404, detail="Shortened URL not found")
