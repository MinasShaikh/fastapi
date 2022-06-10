from fastapi import APIRouter
from repository import test



router=APIRouter(
    prefix="/minas",
    tags=['test']
)

@router.get('/')
def all():
    return test.get_all()
