from pydantic import BaseModel


class Tasks(BaseModel):
    title: str
    completecd: bool = False