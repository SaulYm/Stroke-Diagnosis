# Importar las librerias necesarias
import streamlit as st
import pandas as pd
from streamlit.elements.arrow import Data
from streamlit.elements.legacy_altair import generate_chart

#from tensorflow import keras
from tensorflow.keras.models import load_model
#import tensorflow as tf
#from keras.models import load_model


model = ''
#Cargar los datos
if model == '':
    model = load_model('ANN.h5')
    
# Titulo
st.title('JAVIER SE LA COME')
# Titulo del sidebar
st.sidebar.header('User Input Parameters')

st.subheader('User input parameters')
st.subheader('Artificial Neural Network')
    
# Funcion para poner los parametros del sidebar
def user_input_parameters(): 
        
    # Variables
    gender_dic = {'Male':0, 'Female':1, 'Other':2}
    gender = st.sidebar.selectbox('Seleccione su género', gender_dic)
    gender_num = gender_dic.get(gender)

    age = st.sidebar.text_input('Ingrese su edad')

    option_dic = {'No':0, 'Yes':1}

    heart_disease = st.sidebar.radio('¿Sufre de problemas al corazón?', option_dic)
    heart_disease_num = option_dic.get(heart_disease)

    hypertension = st.sidebar.radio('¿Sufre de hipertensión?', option_dic)
    hypertension_num = option_dic.get(hypertension)

    ever_married = st.sidebar.radio('¿Alguna vez se casó?', option_dic)
    ever_married_num = option_dic.get(ever_married)

    work_type_dic = {'children':0,'Govt_job':1,'Never_worked':2,'Private':3,'Self-employed':4}
    work_type = st.sidebar.selectbox('Seleccione su tipo de trabajo', work_type_dic)
    work_type_num = work_type_dic.get(work_type)

    residence_type_dic = {'Rural':0,'Urban':1}
    residence_type = st.sidebar.radio('¿En qué tipo de residencia vive?', residence_type_dic)
    residence_type_num = residence_type_dic.get(residence_type)
                
    avg_glucose_level = st.sidebar.text_input('Ingrese su nivel de glucosa')

    bmi = st.sidebar.text_input('Índice de masa corporal')

    smoking_status_dic = {"formerly smoked":0, "never smoked":1, "smokes":2, "Unknown":3}
    smoking_status = st.sidebar.selectbox('Tipo de fumador', smoking_status_dic)
    smoking_status_num = smoking_status_dic.get(smoking_status)

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

if st.button('RUN'):
    predict = model.predict(query_df)
    if predict == 1:
        st.warning('Propenso a derrame')
    else:
        st.success('No propenso a derrame')


#if __name__ == '__main__':
    #main()

    




