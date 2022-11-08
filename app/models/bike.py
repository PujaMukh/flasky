from app import db

class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    cyclist_id = db.Column(db.Integer, db.ForeignKey('cyclist.id'))
    cyclist = db.relationship("Cyclist", back_populates="bikes")

    def to_dict(self):
        bike_dict = {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }
        return bike_dict

    @classmethod
    def from_dict(cls, data_dict):
        #check data_dict has all valid bike attributes
        #helps prevent KeyError
        if "name" in data_dict and "price" in data_dict:
            new_obj = cls(name=data_dict["name"], 
            price=data_dict["price"])
            
            return new_obj
        #if not, can look into raising an error with make_response and abort(); did not have time in class.