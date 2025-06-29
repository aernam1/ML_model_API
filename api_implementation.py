# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 19:03:35 2025

@author: Abhinav
"""

import requests
import json

url = 'http://127.0.0.1:8000/diabetes_prediction'

input_data_for_model =    { 
      'Pregnancies' : 8,
      'Glucose' : 183,
      'BloodPressure' : 64,
      'SkinThickness' : 0,
      'Insulin' : 0,
      'BMI' : 23.3,
      'DiabetesPedigreeFunction' : 0.672,
      'Age' : 32
      }
     
input_json = json.dumps(input_data_for_model)
response = requests.post(url, data=input_json)
     
print(response.text)

