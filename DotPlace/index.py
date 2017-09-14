from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from list import list_blueprint
from new import new_blueprint
app.register_blueprint(list_blueprint)
app.register_blueprint(new_blueprint)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Image, User, Trip, Position, Article

engine = create_engine('sqlite:///dotplace.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def MainPage():
	return render_template('index.html')

@app.route('/user/json')
def UserJson():
	users = session.query(User).all()
	return jsonify(Users=[u.serialize for u in users])

@app.route('/trip/<int:trip_id>')
def TripView(trip_id):
	trip = session.query(Trip).filter_by(id=trip_id).one()
	pos = session.query(Position).filter_by(trip_id=trip_id).all()
	return render_template('trip.html', trip=trip, positions=pos)

@app.route('/trip/exists/<int:trip_id>')
def TripExists(trip_id):
	trip = session.query(Trip).filter_by(id=trip_id)
	if trip.count() > 0 :
		return str(1)
	else :
		return str(0)
	
@app.route('/position/exists/<int:position_id>')
def PositionExists(position_id):
	position = session.query(Position).filter_by(id=position_id)
	if position.count() > 0 :
		return str(1)
	else :
		return str(0)
	
@app.route('/image/exists/<int:image_id>')
def ImageExists(image_id):
	image = session.query(Image).filter_by(id=image_id)
	if image.count() > 0 :
		return str(1)
	else :
		return str(0)


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8080)