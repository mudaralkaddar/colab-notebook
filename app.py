import pickle
import streamlit as slt
#PAGE_CONFIG = {"page_title":"StColab.io","page_icon":":smiley:","layout":"centered"}
#slt.beta_set_page_config(**PAGE_CONFIG)
logistic_regression = pickle.load(open('/app/colab-notebook/Completed_llogistic_regression_model.joblib', 'rb'))
#tree = pickle.load(open('/app/colab-notebook/Completed_Bayesian_model.joblib', 'rb'))
#GNB = pickle.load(open('/app/colab-notebook/Completed_tree_model.joblib', 'rb'))
def main():
  slt.title('compare between three models in case of accept or refuse give a loan')

  #input vabs
  Gender = slt.text_input("Gender")
  Married = slt.text_input("Married")
  Dependents = slt.text_input("Dependents")
  Education = slt.text_input("Education")
  Self_Employed = slt.text_input("Self_Employed")
  ApplicantIncome = slt.text_input("ApplicantIncome")
  CoapplicantIncome = slt.text_input("CoapplicantIncome")
  LoanAmount = slt.text_input("LoanAmount")
  Loan_Amount_Term = slt.text_input("Loan_Amount_Term")
  Credit_History = slt.text_input("Credit_History")
  result=["can get a loan","can not get a loan"]
  if slt.button('logistic_regression'):
    y_pred = logistic_regression.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History]])
    output = y_pred[0]
    if output ==1:
      slt.success("the person with the former data  : {}".format(result[0]))
    else:
      slt.success("the person with the former data  : {}".format(result[1]))
  if slt.button('GNB'):
    y_pred = logistic_regression.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History]])
    output = y_pred[0]
    if output ==1:
      slt.success("the person with the former data  : {}".format(result[0]))
    else:
      slt.success("the person with the former data  : {}".format(result[1])) 
  if slt.button('tree'):
    y_pred = logistic_regression.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History]]) 
    output = y_pred[0]
    if output ==1:
      slt.success("the person with the former data  : {}".format(result[0]))
    else:
      slt.success("the person with the former data  : {}".format(result[1]))
if __name__ == '__main__':
	main()
