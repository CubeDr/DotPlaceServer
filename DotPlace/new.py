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
	count = int(request.form['count'])

	trip = Trip(title=title, owner=owner)
	session.add(trip)
	session.flush()

        for i in range(count):
                pContent = request.form['position'+str(i)].split()
                pTime = datetimeparser.parseDatetime(request.form['position'+str(i)+'_time'])
                p = Position(lat=pContent[0], lng=pContent[1], type=pContent[2], duration=pContent[3], trip_id=trip.id, time=pTime)
                session.add(p)
                session.flush()

        session.commit()

	print ('inserted trip ' + str(trip.id))

	return str(trip.id), str(301)

@new_blueprint.route('/article/new', methods=['POST'])
def NewArticle():
        content = urllib.parse.unquote_plus(request.form['content'])
        trip_id = request.form['tripId']
        position_index = request.form['dotIndex']
        time = datetimeparser.parseDatetime(urllib.parse.unquote_plus(request.form['time']))

        positions = Position.query.filter_by(trip_id=trip_id).order_by(time).all()
        position = positions[position_index]

        article = Article(content=content, dot_id=position.id, time=time)
        session.add(article)
        session.commit()
        
        return str(article.id), str(301)
