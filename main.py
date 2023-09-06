import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('Models/diabetes_model.sav' ,'rb'))

heart_disease_model = pickle.load(open("Models/heart_model.sav",'rb'))

parkinsons_model = pickle.load(open("Models/parkinsons_model.sav", 'rb'))

kidney_model = pickle.load(open("Models/kidney_model.sav", 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System  [Team 20]',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction','Kidney Prediction'],
                          icons=['activity','heart','person','activity'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          st.error('The person is diabetic')
        else:
          st.success('The person is not diabetic')





# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        select_option = st.radio("Select Gender: ", ('Male', 'Female'))
        if select_option == "Male":
            sex = 1
        elif select_option == "Female":
            sex = 0
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          st.error('The person is having heart disease')
        else:
          st.success('The person does not have any heart disease')
        
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          st.error("The person has Parkinson's disease")
        else:
          st.success("The person does not have Parkinson's disease")

#kidney disease prediction




if (selected == "Kidney Prediction"):
    
    # page title
    st.title("kidney Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        bp = st.text_input('BP')
        
    with col3:
        al = st.text_input('al')
        
    with col4:
        su = st.text_input('su')
        
    with col5:

        select_option = st.selectbox("RBC: ",['Normal', 'Abnormal'])
        if select_option == "Normal":
            rbc = 1
        elif select_option == "Abnormal":
            rbc = 0
        
    with col1:

        select_option = st.selectbox("PC: ",['Normal', 'Abnormal'])
        if select_option == "Normal":
            pc = 1
        elif select_option == "Abnormal":
            pc = 0

        # pc = st.text_input('pc')
        
    with col2:
        # pcc = st.text_input('ppc')
        select_option = st.selectbox("PCC: ",['Not present', 'Present'])
        if select_option == "Present":
            pcc = 1
        elif select_option == "Not present":
            pcc = 0
        
    with col3:
        # ba = st.text_input('ba')
        select_option = st.selectbox("BA: ",['Not present', 'Present'])
        if select_option == "Present":
            ba = 1
        elif select_option == "Not present":
            ba = 0
        
    with col4:
        bgr = st.text_input('bgr')
        
    with col5:
        bu = st.text_input('bu')
        
    with col1:
        sc = st.text_input('sc')
        
    with col2:
        pot = st.text_input('pot')
        
    with col3:
        wc = st.text_input('wc')
        
    with col4:
        # htn = st.text_input('htn')
        select_option = st.selectbox("HTN: ",['Yes', 'No'])
        if select_option == "Yes":
            htn = 1
        elif select_option == "No":
            htn = 0
        
    with col5:
        # dm = st.text_input('dm')
        select_option = st.selectbox("DM: ",['Yes', 'No'])
        if select_option == "Yes":
            dm = 1
        elif select_option == "No":
            dm = 0
        
    with col1:
        # cad = st.text_input('cad')
        select_option = st.selectbox("CAD: ",['Yes', 'No'])
        if select_option == "Yes":
            cad = 1
        elif select_option == "No":
            cad = 0
        
    with col2:
        # pe = st.text_input('pe')
        select_option = st.selectbox("PE: ",['Yes', 'No'])
        if select_option == "Yes":
            pe = 1
        elif select_option == "No":
            pe = 0
        
    with col3:
        # ane = st.text_input('ane')
        select_option = st.selectbox("ANE: ",['Yes', 'No'])
        if select_option == "Yes":
            ane = 1
        elif select_option == "No":
            ane = 0

    
    # code for Prediction
    kidney_diagnosis  = ''
    
    # creating a button for Prediction    
    if st.button("Kidney Test"):
        kidney_prediction = kidney_model.predict([[age,bp,al,su,rbc,pc,pcc,ba,bgr,bu,sc,pot,wc,htn,dm,cad,pe,ane]])                          
        
        if (kidney_prediction[0] == 1):
          st.error("The person has Kidney disease")
        else:
          st.success("The person does not have kidney disease")
        