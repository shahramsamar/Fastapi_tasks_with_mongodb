from pydantic import BaseModel


class Tasks(BaseModel):
    title: str
    completed: bool = False