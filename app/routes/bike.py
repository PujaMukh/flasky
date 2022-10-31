from flask import Blueprint, jsonify, request,abort, make_response
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
def get_one_bike_or_abort(bike_id):
    try:
        bike_id = int(bike_id)
    except ValueError:
        response_str= f"Invalid bike_id"
        abort(jsonify({"message":response_str}),400)
    matching_bike = Bike.query.get(bike_id)

    if matching_bike is None:
        response_str = f"Bike id {bike_id} not found in database"
        abort(make_response(jsonify({"message":response_str}),400))
    return matching_bike


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

@bike_bp.route("/<bike_id>", methods =["GET"])
def get_one_bike(bike_id):
    chosen_bike = get_one_bike_or_abort(bike_id)
    bike_dict = {
            "id": chosen_bike.id,
            "name" : chosen_bike.name,
            "price" : chosen_bike.price
        }
    return jsonify(chosen_bike.to_dict()), 200


@bike_bp.route("/<bike_id>", methods =["PUT"])
def update_bike_with_new_vals(bike_id):
    chosen_bike = get_one_bike_or_abort(bike_id)
    request_body = request.get_json()
    if "name" not in request_body or \
        "price" not in request_body:
            return jsonify({"message": "Request must include name, price"}), 400

    chosen_bike.name = request_body["name"]
    chosen_bike.name = request_body["price"]

    db.session.commit()

    return jsonify({"message": f"successfully replaced bike with id {bike_id}"}), 200


@bike_bp.route("/<bike_id>", methods =["DELETE"])
def delete_one_bike(bike_id):
    chosen_bike = get_one_bike_or_abort(bike_id)
    db.session.delete(chosen_bike)
    db.session.commit()

    return jsonify({"message": f"successfully deleted bike with id {bike_id}"}), 200