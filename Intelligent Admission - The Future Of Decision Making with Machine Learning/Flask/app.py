import numpy as numpy
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
#Import necessary libraries
from tensorflow.keras.models import load_model

#model = pickle.load(open('university.pkl', 'rb'))
#load model trrained model
# Load your trained model
model = load_model('model.h5')


@app.route('/')
def home():
    return render_template('Demo2222.html')

@app.route('//y_predict', methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    #min max scaling
    min1=[290., 92.0, 1.0, 1.0, 1.0, 6.8, 0.0]
    max1=[340.0, 120.0, 5.0, 5.0, 5.0, 9.92, 1.0]
    k= [float(x) for x in request.form.values()]
    p = []
    for i in range(7):
        l=(k[i]-min1[i])/(max1[i]-min1[i])
        p.append(1)
        prediction = model.predict([p])
        print(prediction)
        output=prediction[0]
        if(output==False):
            return render_template('noChance.html', prediction_text='You Dont have a chance of getting admission')
        else:
            return render_template('chance.html', prediction_text='You have a chance of getting admission')
if __name__=="__main__":
    app.run(debug=False)