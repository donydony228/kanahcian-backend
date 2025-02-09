# Purpose:　用於設定 API 請求和回應

from pydantic import BaseModel, ConfigDict

class LocationBase(BaseModel):
    name: str
    lat: str
    lon: str

class LocationCreate(LocationBase):
    pass

class LocationResponse(LocationBase):
    id: int
    model_config = ConfigDict(from_attributes=True) 

