# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 18:29:23 2023

@author: Lenovo
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


diabetes_model = pickle.load(open("D:Data science practice\multiple disease prediction\diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("D:Data science practice\multiple disease prediction\heart_disease_model.sav",'rb'))
parkinsons_model = pickle.load(open("D:Data science practice\multiple disease prediction\parkinsons_model.sav",'rb'))


#side bar for navigate
with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'], 
                         
                         icons = ['activity','heart','person'],
                          
                          default_index = 0)


#diabetes prediction page                          
if (selected == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using ML')
    
   
    
    #getting the user data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
        
    with col2:
         Glucose = st.text_input('Glucose Level')    
         
    with col3:
         BloodPressure = st.text_input('Blood Pressure value')   


    with col1:
        SkinThickness = st.text_input('skin thickness value')        

    with col2:
        Insulin = st.text_input('Insulin level')                 
        
    with col3:
        BMI = st.text_input('BMI Level') 
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')        

    with col2:
         Age = st.text_input('Age of the Person')      
    
    #code for prediction 
    diab_diagnosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,  Glucose, BloodPressure, SkinThickness, Insulin, BMI,DiabetesPedigreeFunction, Age ]])
    
        
        if (diab_prediction[0]==1):           
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is not Diabetic'
            
    st.success(diab_diagnosis )                
         
     

           
    
if (selected == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction using ML')

if (selected == 'Parkinsons Prediction'):
    #page title
    st.title('Parkinsons Prediction using ML')    

                          