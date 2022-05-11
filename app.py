import numpy as np
import pickle
import streamlit as st


#loading the saved model
load_model= pickle.load(open("C:/Users/Nitin_Kondaval/Downloads/New folder/final_model.sav",'rb'))

                             
#creating a function for prediction
def insurance_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    
    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = load_model.predict(input_data_reshaped)
    print(prediction)
    
    if(prediction[0] == 0):
        return'The claim is fraud'
    else:
        return'The claim is genuine'
        
        
def main():
    #giving the title
    
    st.title("INSURANCE PREDICTION OF HOSPITAL DATA")
    
    #getting the input data from user
    
    
    Area_Service=st.text_input("Area_Service")
    Hospital_County=st.text_input("Hospital_County")
    Age=st.text_input("Age group")
    Gender=st.text_input("Gender")
    Cultural_group=st.text_input("Cultural_group")
    ethnicity=st.text_input("ethnicity")
    Days_spend_hsptl=st.text_input("Days spent in hospital")
    Admission_type=st.text_input("Type of admission")
    Home_or_self_care=st.text_input("Home_or_self_care")
    ccs_diagnosis_code=st.text_input("Diagnosis code")
    ccs_procedure_code=st.text_input("ccs_procedure_code")
    apr_drg_description=st.text_input("apr_drg_description")
    Mortality_risk=st.text_input("Mortality risk")
    Surg_Description=st.text_input("Surgical Description")
    Weight_baby=st.text_input("Weight_baby")
    Abortion=st.text_input("Abortion")
    Emergency_dept=st.text_input("Emergency department")
    Tot_charg=st.text_input("Total charge")
    Payment_Typology=st.text_input("Type of payment")
    
    #code for prediction
    insurance_claim=''
    
    if st.button("Predict"):
        insurance_claim=insurance_prediction([Area_Service,Hospital_County, Age, Gender, Cultural_group,ethnicity,Days_spend_hsptl, Admission_type, Home_or_self_care,ccs_diagnosis_code, ccs_procedure_code, apr_drg_description,Mortality_risk, Surg_Description, Weight_baby, Abortion,Emergency_dept, Tot_charg, Payment_Typology])
        
    st.success(insurance_claim)

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    