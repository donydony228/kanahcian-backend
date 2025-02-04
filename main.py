from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 設定 CORS，允許前端請求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 可改成你的 GitHub Pages 網址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 測試端點
@app.get("/")
def read_root():
    return {"message": "FastAPI 伺服器運行中"}

# 模擬地點 API
@app.get("/api/locations")
def get_locations():
    locations = [
        {"name": "臺灣基督教長老教會 加拿教會", "lat": 22.999724630233, "lon": 121.13047583808864},
        {"name": "加拿天主堂", "lat": 23.001269123782023, "lon": 121.12791348995336},
        {"name": "加樂教會", "lat": 23.009829368501553, "lon": 121.13182280986576},
        {"name": "江新武長老家", "lat": 23.009498, "lon": 121.131187},
        {"name": "加拿國小", "lat": 23.00116136899162, "lon": 121.13087331027815}
    ]
    return {"status": "success", "data": locations}

# uvicorn main:app --host 0.0.0.0 --port 8000