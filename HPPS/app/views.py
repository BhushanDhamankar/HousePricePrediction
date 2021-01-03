import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def result(request):

    data=pd.read_csv(r"C:\Project\Datasets\USA_Housing.csv")
    data = data.drop(['Address'], axis=1)
    X = data.drop('Price', axis=1)
    Y = data['Price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.05)
    model = LinearRegression()
    model.fit(X_train, Y_train)

    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])

    predictions = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1,-1))
    predictions = round(predictions[0])

    ans = "The Predicted Price is $ "+str(predictions)

    return render(request, "predict.html",{'price': ans})