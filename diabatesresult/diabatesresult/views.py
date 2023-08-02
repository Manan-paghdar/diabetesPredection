
from django.shortcuts import render
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def home(request):
    return render(request ,"home.html")
def predict(request):
    return render(request ,"predict.html")
def result (request):
    data = pd.read_csv(r"D:\my downloads\archive (1)\diabetes.csv")

    x = data.drop("Outcome", axis=1)
    y = data["Outcome"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(x_train, y_train)

    val1 = float(request.GET["n1"])
    val2 = float(request.GET["n2"])
    val3 = float(request.GET["n3"])
    val4 = float(request.GET["n4"])
    val5 = float(request.GET["n5"])
    val6 = float(request.GET["n6"])
    val7 = float(request.GET["n7"])
    val8 = float(request.GET["n8"])

    pred=model.predection([val1,val2,val3,val4,val5,val6,val7,val8])

    result1=""
    if pred==[1]:
       result2="positive"
    else:
        result2="negative"

    return render(request ,"predict.html",{"result":result2})
