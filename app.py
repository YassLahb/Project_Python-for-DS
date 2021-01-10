from flask import Flask, request, jsonify
import json
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

app = Flask(__name__)

myModel = pickle.load(open('model.sav', 'rb'))

@app.route('/api/submit', methods=['POST'])
def index():
    if request.method == 'POST':
        content = request.json['content']

        #! Clean data
        contentDF = pd.DataFrame(data={'text':content}, index=[0])
        contentDF.Weekend = contentDF.Weekend.astype('int')
        dff = pd.concat([contentDF,pd.get_dummies(contentDF['Month'], prefix='Month')], axis=1).drop(['Month'],axis=1)
        dff = pd.concat([dff,pd.get_dummies(dff['VisitorType'], prefix='VisitorType')], axis=1).drop(['VisitorType'],axis=1)
        sc_X = StandardScaler()
        scaled_data=sc_X.fit_transform(dff)
        
        #!Prediction
        prediction = myModel.predict(scaled_data)

        return json.dumps({'result':prediction[0]}), 200, {'ContentType':'application/json'} 
    
@app.route('/', methods=['GET'])
def homepage():
    return 'Hello world'
    
if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)

