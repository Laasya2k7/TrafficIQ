from pydantic import BaseModel

class TrafficInput(BaseModel):
    Junction: int
    Year: int
    Month: int
    Day: int
    Hour: int
    Dayofweek: int