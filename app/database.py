# Purpose: 建立資料庫連線，並提供 DB session

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# 載入 .env 變數
load_dotenv()

# **取得資料庫連線字串**
DATABASE_URL = os.getenv("DATABASE_URL")

# **建立資料庫連線**
engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# **建立 DB session**
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
