import streamlit as st
import pandas as pd
import numpy as np
st.title('BMI CALCULATOR')
w=st.number_input("Weight(kgs)")
h=st.number_input('Height(feet)')
if w<0:
    raise Exception('Weight should be positive')
if h<0:
    raise Exception('Height should be positive')
try:
    Bmi=w/(h*0.3048)**2
except:
    Bmi=0
'Your BMI: ',str(Bmi),'(kg/m2)'

def show(x):
    'You fall in ',x,' category'
if Bmi<18.5:
    x='Underweigth'
elif Bmi<=24.9:
    x='Normal weight'
elif Bmi<=29.9:
    x='Overweight'
else:
    x='Obesity'

show(x)

st.header('BMI Categories:')
'Underweight = < 18.5'
'Normal weight = 18.5–24.9'
'Overweight = 25–29.9'
'Obesity = BMI of 30 or greater'

