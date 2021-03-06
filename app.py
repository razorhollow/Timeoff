#!python3
from flask import Flask, request, render_template

import datetime

from peewee import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

	return render_template('index.html')

@app.route('/holiday')
def holiday():
	today = datetime.date.today()
	thisYear = today.year
	query =  HolidayCalendar.select()
	return render_template('holiday.html',
							query=query,
							thisYear=thisYear)

@app.route('/vacation')
def vacation():
	return render_template('vacation.html')

@app.before_request
def before_request():
	db.connect()

@app.after_request
def after_request(response):
	db.close()
	return response

db = SqliteDatabase('TimeOff.db')

class BaseModel(Model):
	class Meta:
		database = db

class Employee(BaseModel):
    employeeNumber = IntegerField(primary_key=True, unique=True)
    lastName = CharField(max_length=20)
    firstName = CharField(max_length=20)
    hireDate = DateField(null=False)
    password = CharField(max_length=20)

class Vacation(BaseModel):
    employeeNumber = IntegerField()
    vacationDate = DateField(null=False)
    hoursUsed = IntegerField(default=8)

class HolidayCalendar(BaseModel):
    holidayDate = DateField(primary_key=True, unique=True)
    description = TextField()

def initialize():
    db.connect()
    db.create_tables([Employee, Vacation, HolidayCalendar], safe=True)

isAdmin = [33, 65]
app.run()	