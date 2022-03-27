from fastapi import APIRouter, status
from typing import Iterable, List
from backend.dao.demo_dao import demo_dao_instance

from backend.model.demo_model import Demo


router = APIRouter()
tags = ["Demo"]
SECONDS_IN_1_MIN = 60


@router.get("", response_model=List[Demo], tags=tags)
def get_all_demos() -> List[Demo]:
    resp = demo_dao_instance.find_all()
    return list(resp)


@router.post(
    "/{demo_info}",
    response_model=Demo,
    status_code=status.HTTP_201_CREATED,
    tags=tags,
)
def create_demo(demo_info: str) -> Demo:
    resp = demo_dao_instance.insert(demo_info)
    return resp
