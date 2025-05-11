import os
from fastapi import FastAPI
from dotenv import load_dotenv
from src.api.configuration import configure_db, configure_routes

load_dotenv()

def create_app():
  app = FastAPI()

  #inicializar db
  configure_db(app)
  configure_routes(app)

  return app 

app = create_app()

