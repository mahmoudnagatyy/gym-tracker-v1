from pydantic import BaseModel
from typing import List, Optional

class SetBase(BaseModel):
    exercise_name: str
    set_num: int
    weight_kg: float
    reps: int
    volume: float

class SetCreate(SetBase):
    pass

class SetModel(SetBase):
    id: int
    session_id: int

    class Config:
        orm_mode = True
        from_attributes = True

class SessionBase(BaseModel):
    date: str
    time: str
    session_type: str
    bodyweight: Optional[float] = None
    total_volume: float
    total_sets: int
    duration: int

class SessionCreate(SessionBase):
    sets: List[SetCreate]

class SessionModel(SessionBase):
    id: int
    sets: List[SetModel]

    class Config:
        orm_mode = True
        from_attributes = True
