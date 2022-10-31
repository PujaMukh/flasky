from app import db

class Bike(db.Model): #Bike class inheriting from db model
    id = db.Column(db.Integer, primary_key = True, autoincrement = True) #1st datatype (db.Integer)
    name = db.Column(db.String) #sqlalchemy will go and figure out the best datatype like string or text if we put string
    price = db.Column(db.Integer)

