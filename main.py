# Importar las librerias necesarias
import streamlit as st
import pandas as pd
import numpy as np

from streamlit.elements.arrow import Data
from streamlit.elements.legacy_altair import generate_chart
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
from sklearn import preprocessing



model = ''
#Cargar los datos
if model == '':
    model = load_model("ANN.h5")
    
# Titulo
st.title('Stroke Prediction based on Artificial Neural Network')
# Titulo del sidebar
st.sidebar.header('User Input Parameters')

st.subheader('User input parameters')
    
# Funcion para poner los parametros del sidebar
def user_input_parameters(): 
        
    # Variables
    options = ['No','Yes']

    gender_opc = ['Male', 'Female', 'Other']
    gender = st.sidebar.selectbox('Seleccione su género', gender_opc)

    age = st.sidebar.text_input('Ingrese su edad')
    
    hypertension = st.sidebar.radio('¿Sufre de hipertensión?', options)

    heart_disease = st.sidebar.radio('¿Sufre de problemas al corazón?', options)

    ever_married = st.sidebar.radio('¿Alguna vez se casó?', options)

    work_type_opc = ['children','Govt_job','Never_worked','Private','Self-employed']
    work_type = st.sidebar.selectbox('Seleccione su tipo de trabajo', work_type_opc)

    residence_type_opc = ['Rural','Urban']
    residence_type = st.sidebar.radio('¿En qué tipo de residencia vive?', residence_type_opc)
                
    avg_glucose_level = st.sidebar.text_input('Ingrese su nivel de glucosa')

    bmi = st.sidebar.text_input('Índice de masa corporal')

    smoking_status_opc = ["formerly smoked", "never smoked", "smokes", "Unknown"]
    smoking_status = st.sidebar.selectbox('Tipo de fumador', smoking_status_opc)

    data_query = {
                    'gender': gender,
                    'age': age,
                    'hypertension': hypertension,
                    'heart_disease': heart_disease,
                    'ever_married': ever_married,
                    'work_type': work_type,
                    'Residence_type': residence_type,
                    'avg_glucose_level': avg_glucose_level,
                    'bmi': bmi,
                    'smoking_status': smoking_status}

    features = pd.DataFrame(data_query, index=[0])
    return features
    
query_df = user_input_parameters()

st.write(query_df)

query_df = query_df.replace({"Male":0, "Female":1, "Other":2, "No":0, "Yes":1, "children":0,"Govt_job":1,"Never_worked":2,"Private":3,"Self-employed":4,
                         "Rural":0,"Urban":1,"formerly smoked":0, "never smoked":1, "smokes":2, "Unknown":3})

if st.button('RUN'):

    query_df = preprocessing.normalize(query_df)
    query_df = np.asarray(query_df).astype(np.float16)

    predict = model.predict(query_df)

    if predict >= 0.05:
        st.warning('Propenso a sufrir un ACV')
        st.text('Algunas medidas para prevenir un ACV')
        st.image('https://www.clikisalud.net/wp-content/uploads/2017/10/pasos.png')
        st.image('https://scontent.flim2-1.fna.fbcdn.net/v/t1.6435-9/71035919_1232422356938185_9082812119627333632_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_ohc=ViMR4XuI0xgAX-HzkkR&_nc_ht=scontent.flim2-1.fna&oh=0eba68aa0f6fcf8f4ce0c52ab97b23b2&oe=61D28603')
    else:
        st.success('No propenso a sufrir un ACV')
        st.text('Usted cuida su cerebro :)')
        st.image('https://grillodeyucatan.com/wp-content/uploads/2019/07/0723_CEREBRO2.jpg')


