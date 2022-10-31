from flask import Blueprint, jsonify, request
# class Bike:
#     def __init__(self, id, name, price):
#         self.id = id
#         self.name = name
#         self.price = price 

# bikes = [ 
#     Bike(1, "bike1", 200),
#     Bike(2, "bike2", 300),
#     Bike(3, "bike3", 400)

# ]

from app import db
from app.models.bike import Bike

bike_bp= Blueprint("bike_bp", __name__, url_prefix = "/bike")
@bike_bp.route("", methods=["POST"])
def add_bike():
    request_body = request.get_json()

    new_bike = Bike(
        name = request_body["name"],
        price = request_body["price"]

    )

    # add it to database
    db.session.add(new_bike)
    db.session.commit() # DO NOT FORGET TO COMMIT 

    return {"id": new_bike.id}, 201

@bike_bp.route("", methods =["GET"])
def get_all_bikes():

    #getting all bikes list instead of hardcoding like above
    bikes = Bike.query.all() #added this for models

    response = []
    for bike in bikes:
        bike_dict = {
            "id": bike.id,
            "name" : bike.name,
            "price" : bike.price
        }
        response.append(bike_dict)
    return jsonify(response), 200


