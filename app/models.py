# app/models.py
from app import db

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    square_footage = db.Column(db.Float)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    year_built = db.Column(db.Integer)
    zip_code = db.Column(db.String(10))
    estimated_price = db.Column(db.Float)
    
    def to_dict(self):
        return {
            "id": self.id,
            "square_footage": self.square_footage,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "year_built": self.year_built,
            "zip_code": self.zip_code,
            "estimated_price": self.estimated_price
        }

