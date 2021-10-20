from flask import Flask, request, jsonify
import joblib
import pandas as pd



#Creat a flask app
app = Flask(__name__)




#connect POST api call ---> predict() function
@app.route('/predict',methods=['POST'])
def predict():
    feature_data = request.json
    
    df = pd.DataFrame(feature_data)
    
    df = df.reindex(columns=col_names)
    
    prediction = list(model.predict(df))
    
    
    return jsonify({'prediction':str(prediction)})



#Load pickle files

if __name__ == '__main__':
    
    model = joblib.load('final_model.pkl')
    col_names = joblib.load('column_names.pkl')
    
    app.run(debug=True)