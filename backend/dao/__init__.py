from typing import Any
import os
from fastapi.exceptions import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from urllib.parse import quote_plus

engine = create_engine(
    f"{os.environ['DATABASE_URL']}",
    connect_args={"sslmode": os.environ.get("DB_SSL_MODE", "prefer")},
    poolclass=QueuePool,
    pool_size=int(os.environ.get("DB_POOL_SIZE", "1")),
    max_overflow=int(os.environ.get("DB_MAX_OVERFLOW", "2")),
)
