# Importar las librerias necesarias
import streamlit as st
import pandas as pd
import numpy as np
#import tensorflow as tf
#from tensorflow import keras
from streamlit.elements.arrow import Data
from streamlit.elements.legacy_altair import generate_chart

from tensorflow.keras.models import load_model

#from tensorflow import keras
#from tensorflow.keras.models import load_model
#import tensorflow as tf
#from keras.models import load_model


model = ''
#Cargar los datos
if model == '':
    model = load_model("ANN.h5")
    
# Titulo
st.title('JAVIER SE LA COME')
# Titulo del sidebar
st.sidebar.header('User Input Parameters')

st.subheader('User input parameters')
st.subheader('Artificial Neural Network')
    
# Funcion para poner los parametros del sidebar
def user_input_parameters(): 
        
    # Variables
    options = ['No','Yes']



    gender_opc = ['Male', 'Female', 'Other']
    gender = st.sidebar.selectbox('Seleccione su género', gender_opc)

    age = st.sidebar.text_input('Ingrese su edad')

    heart_disease = st.sidebar.radio('¿Sufre de problemas al corazón?', options)

    hypertension = st.sidebar.radio('¿Sufre de hipertensión?', options)

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
#Falta arreglar esto ;v
if st.button('RUN'):
    query_df = np.asarray(query_df).astype(np.intc)
    predict = model.predict(query_df)
    if predict == 1:
        st.warning('Propenso a derrame')
    else:
        st.success('No propenso a derrame')

#if __name__ == '__main__':
    #main()

    
