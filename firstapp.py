import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
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

weight=np.linspace(10,120)
bmis=[10,20,30,40]
ht=[]
for i in bmis:
    height=((weight/i)**0.5)/0.3048
    ht.append(height)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
for i in range(len(bmis)):
    ax.plot(weight,ht[i],label='BMI:'+str(bmis[i]))
    
ax.scatter(w,h)    
ax.legend()
ax.set_xlabel('Weight(kgs)')
ax.set_ylabel('Height(ft)')    
st.write(fig)



    


st.header('BMI Categories:')
'Underweight = < 18.5'
'Normal weight = 18.5–24.9'
'Overweight = 25–29.9'
'Obesity = BMI of 30 or greater'

