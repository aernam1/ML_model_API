# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 20:50:52 2025

@author: Abhinav
"""
from pydantic import BaseModel
import pickle
import json
import numpy as np
import joblib
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
app = FastAPI()

class model_input(BaseModel):
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
diabetes_model=joblib.load('diabetes_model.joblib')

@app.get("/", response_class=HTMLResponse)
def get_form(request : Request):
    return templates.TemplateResponse("template-form.html", {"request": request, "result": None})


@app.post("/", response_class=HTMLResponse)
def post_form(
    request: Request,
    Pregnancies: int = Form(...),
    Glucose: int = Form(...),
    BloodPressure: int = Form(...),
    SkinThickness: int = Form(...),
    Insulin: int = Form(...),
    BMI: float = Form(...),
    DiabetesPedigreeFunction: float = Form(...),
    Age: int = Form(...)
):
    input_list = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    prediction = diabetes_model.predict([input_list])
    
    result = "The person is diabetic" if prediction[0] == 1 else "The person is not diabetic"
    
    return templates.TemplateResponse("template-form.html", {"request": request, "result": result})



# @app.post('/diabetes_prediction', response_class=HTMLResponse)
# def diabetes_pred(input_parameters : model_input):
#     input_data = input_parameters.json()
#     input_dictionary = json.loads(input_data)
    
#     preg = input_dictionary['Pregnancies']
#     glu = input_dictionary['Glucose']
#     bp = input_dictionary['BloodPressure']
#     st = input_dictionary['SkinThickness']
#     insu = input_dictionary['Insulin']
#     bmi = input_dictionary['BMI']
#     dpf = input_dictionary['DiabetesPedigreeFunction']
#     age = input_dictionary['Age']
    
#     input_list = [preg, glu, bp, st, insu, bmi, dpf, age]
#     prediction = diabetes_model.predict([input_list])
    
#     if prediction[0]==0:
#         result  = "The person is not diabetic"
#     else: result =  "The person is diabetic"
    
#     return templates.TemplateResponse("template-form.html", {"result": result})

    
    
    
    
    
    
    
    
