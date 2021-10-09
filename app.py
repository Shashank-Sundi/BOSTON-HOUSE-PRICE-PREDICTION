from flask import Flask,render_template, request
from flask_cors import cross_origin
import pickle


app=Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/Prediction',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method=='POST':
            try:
                CRIM = float(request.form['CRIM'])
                ZN = float(request.form['ZN'])
                INDUS = float(request.form['INDUS'])
                CHAS = int(request.form['CHAS'])
                NOX = float(request.form['NOX'])
                RM = float(request.form['RM'])
                AGE = request.form['AGE']
                DIS = float(request.form['DIS'])
                RAD = request.form['RAD']
                TAX = float(request.form['TAX'])
                PTRATIO = float(request.form['PTRATIO'])
                B = float(request.form['B'])
                LSTAT = float(request.form['LSTAT'])

                data = [[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]]
                scaler = pickle.load(open('StandardScaler.pickle','rb'))
                data=scaler.transform(data)

                RandomForest=pickle.load(open('rand_forest.pickle','rb'))
                prediction=RandomForest.predict(data)
                print(f"The estimated price of the House is : {round(prediction[0] * 1000)} dollars")

                return render_template('results.html', prediction=round(1000 * prediction[0]))

            except Exception as e:
                return print(e)
    else:
        return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True,host='127.0.0.1',port=8001)