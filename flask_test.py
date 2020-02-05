from flask import Flask 

from sklearn.externals import joblib 

model = joblib.load('nn100.joblib')
print('joblib loaded')

app = Flask(__name__)

@app.route('/', methods =['GET'])


def home():
    # deployed model geos here
     return '<h1> Hello, Welcome to symphinity neural something fancy!</h1>'


if __name__ == "__main__":
     app.run(debug=True, port = 8080)

