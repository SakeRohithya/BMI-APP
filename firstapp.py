import streamlit as st
import pandas as pd
import numpy as np
#df=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
#st.line_chart(df)
##data=np.random.randn(1000, 2)
##data
##df=pd.DataFrame(data / [50, 50] + [37.76, -122.4],columns=['lat','lon'])
##df
##st.map(df)
##if st.sidebar.checkbox('Show it'):
##    chart_data = pd.DataFrame(
##    np.random.randn(20, 3),
##    columns=['a', 'b', 'c'])
##    chart_data
##    
##df = pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40]})
##
##option = st.sidebar.selectbox('Which number do you like best?',['sweety','Rohithya','Aaa','Bss'])
##st.sidebar('You selected: ', option)
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

