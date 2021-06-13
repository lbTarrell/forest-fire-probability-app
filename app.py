from flask import Flask,request, url_for, redirect, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("forest_fire.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    params = {"temp": int_features[0], "ox": int_features[1], "humid": int_features[2]}
    response = requests.get(f"https://forest-fire-probability-api.herokuapp.com/", params=params)
    output=str(response.json())

    if output>str(0.5):
        return render_template('forest_fire.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
    else:
        return render_template('forest_fire.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")

if __name__ == '__main__':
    app.run(debug=True)