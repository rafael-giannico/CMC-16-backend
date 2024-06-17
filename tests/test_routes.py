# tests/test_routes.py
def test_estimate_price(client):
    response = client.post('/estimate', json={
        "square_footage": 2000,
        "bedrooms": 3,
        "bathrooms": 2,
        "year_built": 1990,
        "zip_code": "12345"
    })
    assert response.status_code == 200
    json_data = response.get_json()
    assert "estimated_price" in json_data

def test_add_house(client):
    response = client.post('/houses', json={
        "square_footage": 2000,
        "bedrooms": 3,
        "bathrooms": 2,
        "year_built": 1990,
        "zip_code": "12345",
        "estimated_price": 300000
    })
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["square_footage"] == 2000
    assert json_data["bedrooms"] == 3
    assert json_data["bathrooms"] == 2
    assert json_data["year_built"] == 1990
    assert json_data["zip_code"] == "12345"
    assert json_data["estimated_price"] == 300000
