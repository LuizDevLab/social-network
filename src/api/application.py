import os
from fastapi import FastAPI
from dotenv import load_dotenv
from src.datalayer.db_config import configure_db

load_dotenv()

def create_app():
  app = FastAPI()

  #inicializar db
  configure_db(app)

  return app 

app = create_app()

@app.get('/')
async def home():
  return {'status': 'ok'}