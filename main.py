from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

@app.get("/")
def read_root():
    # ใช้ JSONResponse เพื่อบังคับเข้ารหัสภาษาไทย (UTF-8) ให้ถูกต้อง
    return JSONResponse(content={"message": "เซิร์ฟเวอร์ IG Scraper ทำงานปกติ!"})

@app.post("/scrape")
def scrape_instagram(request: URLRequest):
    return JSONResponse(content={
        "status": "success",
        "received_url": request.url,
        "message": "ระบบได้รับ URL แล้ว (รอเชื่อมต่อกับ Apify)"
    })
