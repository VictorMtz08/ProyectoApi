#Se define el modelado de los datos

#from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

class Predict_Input(BaseModel):
    year: int

class Predict_Output(BaseModel):
    year: int
    pred: float


class Delete_Input(BaseModel):
    id: int

class Delete_Onput(BaseModel):
    pred: int