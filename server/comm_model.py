#This file will contain the various response
#request object models
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic.types import conint

class reqmerch(BaseModel):
    item_id:int
    categories:str

class resmerch(BaseModel):
    categories:str
    price:int
    timedate:datetime
    item_id:int
    
    class Config:
        orm_mode = True

class aggmerch(BaseModel):
    category:str
    count:int
