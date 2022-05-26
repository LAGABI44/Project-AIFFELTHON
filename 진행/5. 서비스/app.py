from email import message
from this import d
from flask import Flask,render_template,url_for,request
import pandas as pd
import numpy as np
import tensorflow as tf
import sklearn
import pickle # 객체 입출력을 위한 라이브러리
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier # 랜덤포레스트 분류 알고리즘
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    df=pd.read_csv("data(over_dis_vs_nor).csv",encoding="cp949")
    df.drop(['Dis'], axis=1)
    #Features and Labels
    y = df['DIS']
    x = df.drop(['DIS'], axis=1)
    x = pd.DataFrame(x)


    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)

    rf = RandomForestClassifier(random_state=1234,
                                n_estimators = 15,
                                max_depth = 25,
                                min_samples_split = 2,
                                min_samples_leaf = 2)
    rf.fit(x, y)
    rf.score(x, y)


    if request.method=='POST':
        message = request.form['message']
        message = int(message)
        print(message)
        data = [message]
        vect = scaler.transform(data).toarray()
        pred = rf.predict(vect)
    return render_template('result.html',prediction = pred)

if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)