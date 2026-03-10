from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# การตั้งค่า CORS เพื่ออนุญาตให้หน้าเว็บ (Frontend) ของเราดึงข้อมูลจาก API นี้ได้
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# สร้างโครงสร้างข้อมูลสำหรับรับ URL
class URLRequest(BaseModel):
    url: str

# หน้าแรกสำหรับเช็คว่าเซิร์ฟเวอร์ทำงานปกติไหม
@app.get("/")
def read_root():
    return {"message": "เซิร์ฟเวอร์ IG Scraper ทำงานปกติ!"}

# เส้นทางสำหรับรับ URL จากหน้าเว็บ (เดี๋ยวเราจะเอาโค้ด Apify มาใส่ตรงนี้ทีหลัง)
@app.post("/scrape")
def scrape_instagram(request: URLRequest):
    return {
        "status": "success",
        "received_url": request.url,
        "message": "ระบบได้รับ URL แล้ว (รอเชื่อมต่อกับ Apify ในสเต็ปถัดไป)"
    }
