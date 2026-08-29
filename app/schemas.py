from pydantic import BaseModel


class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str = "medium"
    created_by: str


class TicketUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: str | None = None
    status: str | None = None


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str
    created_by: str

    class Config:
        from_attributes = True
