from flask import Blueprint, render_template, request
new_blueprint = Blueprint('new_blueprint', __name__)

import database
from database import Image, User, Trip, Position, Article

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///dotplace.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

import datetimeparser
import urllib

@new_blueprint.route('/user/new', methods=['POST'])
def NewUser():
	nickname = request.form['nickname']
	password = request.form['password']
	print ('signup request ' + nickname + ' ' + password)
	user = User(nickname=nickname, password=password)
	session.add(user)
	session.commit()
	
	return str(user.id), str(301)
	
@new_blueprint.route('/trip/new', methods=['POST'])
def NewTrip():
	title = urllib.parse.unquote_plus(request.form['title'])
	owner = request.form['owner']
	
	trip = Trip(title=title, owner=owner)
	session.add(trip)
	session.commit()

	print ('inserted trip ' + str(trip.id))

	return str(trip.id), str(301)

@new_blueprint.route('/position/new', methods=['POST'])
def NewPosition():
	lat = request.form['lat']
	lng = request.form['lng']
	time = datetimeparser.parseDatetime(request.form['time'])
	type = request.form['type']
	duration = request.form['duration']
	trip_id = request.form['trip_id']
	
	pos = Position(lat=lat, lng=lng, time=time, type=type, duration=duration, trip_id=trip_id)
	
	session.add(pos)
	session.commit()
	
	print ('inserted position ' + str(pos.id))
	
	return str(pos.id), str(301)

@new_blueprint.route('/article/new', methods=['POST'])
def NewArticle():
	content = urllib.parse.unquote_plus(request.form['content'])
	position_id = request.form['dotId']
	time = datetimeparser.parseDatetime(urllib.parse.unquote_plus(request.form['time']))
	thumbnail_id = request.form.get('thumbnail_id', 0)
	
	article = Article(content=content, dot_id=position_id, time=time, thumbnail_id=thumbnail_id)
	session.add(article)
	session.commit()
	
	return str(article.id), str(301)
