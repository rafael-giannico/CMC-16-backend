from flask import Blueprint, request, jsonify
from app.models import db, House
from app.services.ml_model import predict_price

bp = Blueprint('main', __name__)

@bp.route('/houses', methods=['GET'])
def get_houses():
    houses = House.query.all()
    return jsonify([house.to_dict() for house in houses])

@bp.route('/houses', methods=['POST'])
def add_house():
    data = request.get_json()
    new_house = House(
        square_footage=data['square_footage'],
        bedrooms=data['bedrooms'],
        bathrooms=data['bathrooms'],
        year_built=data['year_built'],
        zip_code=data['zip_code'],
        estimated_price=data['estimated_price']
    )
    db.session.add(new_house)
    db.session.commit()
    return jsonify(new_house.to_dict()), 201

@bp.route('/estimate', methods=['POST'])
def estimate_price():
    data = request.get_json()
    square_footage = data.get('square_footage')
    bedrooms = data.get('bedrooms')
    bathrooms = data.get('bathrooms')
    year_built = data.get('year_built')
    zip_code = data.get('zip_code')
    
    estimated_price = predict_price([square_footage, bedrooms, bathrooms, year_built, zip_code])
    
    new_house = House(
        square_footage=square_footage,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        year_built=year_built,
        zip_code=zip_code,
        estimated_price=estimated_price
    )
    db.session.add(new_house)
    db.session.commit()
    
    return jsonify({"estimated_price": estimated_price})
