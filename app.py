from flask import Flask,request
app = Flask(__name__)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC # "Support Vector Classifier"
def reg(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    nx = [inps]
    pred = linear_regressor.predict(nx)
    return pred

def classify(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    Y=Y.round()
    clf = SVC(kernel='linear') 
    clf.fit(X,Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred
@app.route('/', methods=['GET', 'POST'])
def index():
    Income = int(request.form.get('Income'))
    Housingcost = int(request.form.get('Housing_cost'))
    Transportationcost = int(request.form.get('Transportation_cost'))
    HealthcareExpense = int(request.form.get('Healthcare_Expense'))
    FoodandDining = int(request.form.get('Food_and_Dining'))
    PersonalExpenses = int(request.form.get('Personal_Expenses'))
    Financialaid = int(request.form.get('Financial_aid'))
    CreditHistory = int(request.form.get('Credit_History'))
    Savings = float(request.form.get('Savings'))
    AcademicPerformance = int(request.form.get('Academic_Performance'))
    p = reg('expense.csv',["Income","Housing cost","Transportation cost","Healthcare Expense","Food and Dining","Personal Expenses","Financial aid","Credit History","Savings","Academic Performance"],"outcome",[Income,Housingcost,Transportationcost,HealthcareExpense,FoodandDining,PersonalExpenses,Financialaid,CreditHistory,Savings,AcademicPerformance])
    print("Bot : The Income is: ",float(p[0]))
    p = classify('expense.csv',["Income","Housing cost","Transportation cost","Healthcare Expense","Food and Dining","Personal Expenses","Financial aid","Credit History","Savings","Academic Performance"],"class",[Income,Housingcost,Transportationcost,HealthcareExpense,FoodandDining,PersonalExpenses,Financialaid,CreditHistory,Savings,AcademicPerformance])
    if int(p[0]) == 0:
        print("Student does not have enough savings")
        pr = "Student does not have enough savings"
    elif int(p[0]) == 1:
        print("Student has enough savings")
        pr = "Student has enough savings"
    return pr

if __name__ == '__main__':
    app.run(debug=True)