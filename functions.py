#!python3

import datetime
from peewee import *

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


def getHolidayCal():
	today = datetime.date.today()
	thisYear = today.year
	query =  HolidayCalendar.select()
	for holday in query:
		if holday.holidayDate.year == thisYear:
			return ("{} | {}/{}/{}".format(holday.description, holday.holidayDate.month, holday.holidayDate.day, holday.holidayDate.year))

initialize()
getHolidayCal()
db.close()
