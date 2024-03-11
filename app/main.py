"""This is the fraud detector."""
from datetime import datetime
from typing import Any

from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine
from .model_predict import tree_count

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    """Give database."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    """Hello message."""
    return {"message": "Hello! This is an information application about trees."}


@app.post("/information")
async def post_information(
    buff: schemas.InputFeatures, db: Session = Depends(get_db)
) -> int | Any:
    """Get info."""
    load_dotenv()
    info = tree_count(buff.city, buff.year)
    new_detect = models.Trees(
        city=buff.city,
        country=buff.country,
        year=int(buff.year),
        trees_count=info,
        request_time=datetime.now(),
    )
    db.add(new_detect)
    db.commit()
    return info
