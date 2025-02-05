from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

# 載入 .env 變數
load_dotenv()

# **從環境變數取得 Neon 資料庫連線字串**
DATABASE_URL = os.getenv("DATABASE_URL")

# **建立資料庫連線**
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# **定義資料表**
class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    lat = Column(String)
    lon = Column(String)

# **建立資料表（如果不存在）**
Base.metadata.create_all(bind=engine)

# **FastAPI 應用程式**
app = FastAPI()

# **設定 CORS，允許前端請求**
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 你可以改成你的 GitHub Pages 網址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# **資料庫 session 依賴**
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# **測試 API**
@app.get("/")
def read_root():
    return {"message": "FastAPI 伺服器運行中"}

# **取得所有地點（從資料庫）**
@app.get("/api/locations")
def get_locations(db: Session = Depends(get_db)):
    locations = db.query(Location).all()
    return {"status": "success", "data": locations}

# **新增地點**
@app.post("/api/add_location")
def add_location(name: str, lat: str, lon: str, db: Session = Depends(get_db)):
    new_location = Location(name=name, lat=lat, lon=lon)
    db.add(new_location)
    db.commit()
    return {"message": "地點已新增"}


# uvicorn main:app --host 0.0.0.0 --port 8000