from fastapi import APIRouter , HTTPException, status
from models import Predict_Input
from models import Predict_Output
from models import Delete_Input
from models import Delete_Onput

# import de bibliotecas necesarias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv("jobs_in_data.csv")
df = df[df['job_category'] == 'Data Engineering']
df = df[['work_year','salary_in_usd']]
df = df.groupby("work_year").mean("salary_in_usd").reset_index()

#Variables para modelo 
x = df[["work_year"]]
y = df["salary_in_usd"]

#Asignacio de variables independientes a 'x' y las variables independientes a 'y'
#x_train, x_test, y_train, y_test = train_test_split( x , y , test_size=0.3 , random_state=1 )

# Crea modelo de regresiuon lineal 
#LM = LinearRegression()

# Ajusta el modelo a los datos de entrenamiento 
#LM.fit(x_train, y_train)

# Hace la prediccion sobre los datos de prueba
#y_pred = LM.predict([[2024]])


#Proceso para API
router = APIRouter()

preds=[]

@router.get('/ml')
def get_preds():
    return preds


@router.post('/ml', status_code=201,response_model = Predict_Output)
def predict(pred_input:Predict_Input):

    #Asignacio de variables independientes a 'x' y las variables independientes a 'y'
    x_train, x_test, y_train, y_test = train_test_split( x , y , test_size=0.3 , random_state=1 )
    # Crea modelo de regresiuon lineal 
    LM = LinearRegression()
    # Ajusta el modelo a los datos de entrenamiento 
    LM.fit(x_train, y_train)
    # Hace la prediccion sobre los datos de prueba
    prediction_f = LM.predict([[pred_input.year]])

    prediction_dict = {"year": pred_input.year,
                       "pred": float(prediction_f[0])}
    
    preds.append(prediction_dict)

    return prediction_dict


@router.delete('/ml')
def del_preds( delete_Input:Delete_Input):
    del preds[delete_Input.id]
    return preds