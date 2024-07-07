from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)

# Load your machine learning model (assuming it's a pickle file)
# with open('public/final.pickle', 'rb') as file:
#     model = pickle.load(file)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    location = data['location']
    area = float(data['area'])
    bathrooms = int(data['bathrooms'])
    bhk = int(data['bhk'])

    # Perform your prediction logic here
    # For example, if your model expects an array [area, bathrooms, bhk, location]
    estimated_price=predict_price(location, area, bath, bhk)
    
    # Make prediction (modify this part according to your model's requirements)
    

    return jsonify({'success': True, 'price': estimated_price})




def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = data_columns.index(location.lower())
    except ValueError:
        raise Exception(f"Invalid location: {location}")

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    try:
        prediction = model.predict([x])[0]
    except Exception as e:
        raise Exception(f"Error predicting price: {str(e)}")

    return round(prediction, 2)

if __name__ == '__main__':
    app.run(debug=True)





