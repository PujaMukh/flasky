import pytest
from app import create_app
from app import db
from flask import Flask
from flask.signals import request_finished
from app.models.bike import Bike

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all() #creates entirely new databse everytime test is run
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app): #mock client for running request and getting configurations back
    return app.test_client()

@pytest.fixture
def two_bikes(app):
    bike1 = Bike(name="Speedy", price=1)
    bike2 = Bike(name="MotorBike", price=6)

    db.session.add(bike1)
    db.session.add(bike2)
    db.session.commit()


