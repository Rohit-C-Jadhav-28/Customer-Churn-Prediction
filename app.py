from flask import Flask, render_template, request
import pickle

model_path = r'C:\Users\rcjad\Desktop\Desktop Files\NLP\CodeSoft ML Internship\Customer Churn\Models\RandomForestClassifier.pkl'

Model = pickle.load(open(model_path, 'rb'))

# Helper Function...
def nat(Nationality):
    if Nationality[:3].lower() == "fra":
        Nationality = 0
    elif Nationality[:3].lower() == 'ger':
        Nationality = 1
    elif Nationality[:3].lower() == 'spa':
        Nationality = 2
    else:
        Nationality = 3
    return Nationality

def gender_numb(Gender):
    if Gender[0].lower() == 'm':
        Gender = 1
    elif Gender[0].lower() == 'f':
        Gender = 0
    else:
        Gender = 2

    return Gender

def Yes_NO(value):
    if value[0].lower() == 'y':
        value = 1
    else:
        value = 0
    return value

def data_extract():
    # surname = request.form['Text-name']
    Nationality = request.form['Text-Nationality']
    Gender = request.form['Text-Gender']
    Age = request.form['Text-Age']
    Balance = request.form['Text-Balance']
    Product = request.form['Text-Products']
    Card = request.form['Text-Card']
    CreditScore = request.form['Text-CreditScore']
    years = request.form['Text-years']
    Salary = request.form['Text-Salary']
    Active_Member = request.form['Text-Member']

    Nationality = nat(Nationality=Nationality)
    Gender = gender_numb(Gender=Gender)
    Card = Yes_NO(value=Card)
    Active_Member = Yes_NO(value=Active_Member)

    return [CreditScore,Nationality,Gender,Age,years,Balance,Product, Card,Active_Member, Salary]

def pred():
    data = data_extract()
    prediction = str(Model.predict([data])[0])
    return prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pred', methods=['POST'])
def prediction_final():
    if request.method == 'POST':
        Prediction = pred()
        return render_template('index.html', Message = f"Prediction Says : {Prediction}")

    else:
        print('error...')
        return None

if __name__ == "__main__":
    app.run(port=2000, debug=True)
    
