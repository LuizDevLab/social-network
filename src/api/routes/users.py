from fastapi import APIRouter
from src.api.dtos.users import UserRegistration, UserLogin
from src.datalayer.models.user import UserModel
from src.api.exceptions.user import login_wrong_exception, email_already_exists

router = APIRouter(
  prefix="/users",
  tags=["users"],
  responses={404: {"description": "Not Found"}}
)


@router.post("/register")
async def register(body: UserRegistration):

  email_exists = await UserModel.filter(email=body.email)
  if email_exists:
    raise email_already_exists()

  user = await UserModel.create(
    name = body.name,
    email = body.email,
    password = body.password
  )
  return {"created": user}


@router.post("/login")
async def login(body: UserLogin):

  user = None
  try:
    user = await UserModel.get(email=body.email)
  except Exception:
    raise login_wrong_exception()
  
  
  if user.password != body.password:
    raise login_wrong_exception()

  return user
