import joblib
import streamlit as st
import numpy as np

#model_name = 'RF_Loan_model.joblib'
model_name = 'https://github.com/randi-source/Complete-MLOps-BootCamp/blob/184e9699469c6072c5f8cdcb1a041288c89cd0fc/Build-ML-App-Streamlit/RF_Loan_model.joblib'
model = joblib.load(model_name)

def prediction(Gender, Married, Dependents, Education, 
               Self_Employed, Applicant_Indome, 
               Coapplicant_Income, Loan_Amount, Loan_Amount_Term,
               Credit_History, Property_Area):
    
    if Gender == "Male":
        Gender = 1
    else:
        Gender = 0

    if Married == "Yes":
        Married = 1
    else:
        Married = 0
    
    if Education == "Graduate":
        Education = 0
    else:
        Education = 1
    
    if Self_Employed == "Yes":
        Self_Employed = 1
    else:
        Self_Employed = 0
    
    if Credit_History == "Outstanding Loan":
        Credit_History = 1
    else:
        Credit_History = 0

    if Property_Area == "Rural":
        Property_Area = 0
    elif Property_Area == "Semi Urban":
        Property_Area = 1
    else:
        Property_Area = 2
    
    #Numeric Feature
    Total_Indome = np.log(Applicant_Indome+Coapplicant_Income)

    prediction = model.predict([[Gender, Married, Dependents, Education, 
                                 Self_Employed, Loan_Amount, Loan_Amount_Term,
                                 Credit_History, Property_Area, Total_Indome]])
    print(prediction)

    if prediction == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return pred


def main():
    # Front end
    st.title("Welcome to Loan Application")
    st.header("Please enter your details to proceed with your Application")
    
    Gender = st.selectbox("Gender",("Male","Female"))
    Married = st.selectbox("Married",("Yes","No"))
    Dependents = st.number_input("Number of Dependents")
    Education = st.selectbox("Education",("Graduate","Not Graduate"))
    Self_Employed = st.selectbox("Self Employed",("Yes","No"))
    Applicant_Indome = st.number_input("Applicant Income")
    Coapplicant_Income = st.number_input("Coapplicant Income")
    Loan_Amount = st.number_input("Loan Amount")
    Loan_Amount_Term = st.number_input("Loan Amount Term")
    Credit_History = st.selectbox("Credit History", ("Outstanding Loan","No Outstanding Loan"))
    Property_Area = st.selectbox("Property Area",("Rural", "Urban", "Semi Urban"))

    if st.button("Predict"):
        result = prediction(Gender, Married, Dependents, Education, 
                            Self_Employed, Applicant_Indome, 
                            Coapplicant_Income, Loan_Amount, Loan_Amount_Term,
                            Credit_History, Property_Area)
        
        if result == "Approved":
            st.success("Your loan application is Approved")
        else: 
            st.error("Your loan application is rejected")

if __name__=="__main__":
    main()
    