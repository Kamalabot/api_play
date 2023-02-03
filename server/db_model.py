#This file will hold the tables that are required
from .dbengine import Base
from sqlalchemy import Column, String, Sequence, Integer
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

class Merch(Base):
    __tablename__ = 'google_merchandise'

    categories = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    timedate = Column(TIMESTAMP(timezone=True),
                      nullable=False)
    #item_sequence = Sequence('item_seq_id')
    item_id = Column(Integer,primary_key=True,
                     nullable=False)
