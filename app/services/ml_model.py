import joblib

# Carregue o modelo treinado
model = joblib.load('path_to_saved_model.pkl')

def predict_price(features):
    prediction = model.predict([features])
    return prediction[0]
