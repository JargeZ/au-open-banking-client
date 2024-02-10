from pydantic import BaseModel


class ClientConfig(BaseModel):
    base_url: str
    timeout: int = 10
