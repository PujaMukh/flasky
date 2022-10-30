from flask import Blueprint, jsonify
class Bike:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price 

bikes = [ 
    Bike(1, "bike1", 200),
    Bike(2, "bike2", 300),
    Bike(3, "bike3", 400)

]
bike_bp= Blueprint("bike_bp", __name__, url_prefix = "/bike")

@bike_bp.route("", methods =["GET"])
def get_all_bikes():
    response = []
    for bike in bikes:
        bike_dict = {
            "id": bike.id,
            "name" : bike.name,
            "price" : bike.price
        }
        response.append(bike_dict)
    return jsonify(response), 200
