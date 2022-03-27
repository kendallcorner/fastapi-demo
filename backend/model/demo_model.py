from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Demo(BaseModel):
    info: str
    created_timestamp: datetime
    modified_timestamp: Optional[datetime]
