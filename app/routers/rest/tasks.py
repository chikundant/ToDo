from fastapi import APIRouter
from app.core.dependencies import *

router = APIRouter(
    prefix='/task',
    tags=['task'],
    responses={404: {"description": "not found"}}
)


@router.get(path='/')
def get_all_tasks():
    return {"hi there"}
