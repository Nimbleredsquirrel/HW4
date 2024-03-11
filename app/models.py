"""This program create template from database."""

from sqlalchemy import Column, DateTime, Integer, String

from .database import Base


class Trees(Base):  # pylint: disable=R0903
    """Template from database."""

    __tablename__ = "Trees"

    id = Column(Integer, primary_key=True)
    city = Column(String, default="")
    country = Column(String, default="")
    year = Column(Integer, default=2000)
    trees_count = Column(Integer, default=0)
    request_time = Column(DateTime)
