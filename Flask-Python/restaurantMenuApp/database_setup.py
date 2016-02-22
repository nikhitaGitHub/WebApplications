#CONFIGURATION BEGINNING
import sys
from sqlalchemy import Column, ForeignKey, Integer, String # help with mapping 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine # connect to database database
Base = declarative_base() #Create instance of declarative base

#CLASS TO REPRESENT TABLE IN THE DB
class Restaurant(Base): #Extending/inheriting from Base class
    #TABLE
    __tablename__ = 'restaurant' # table name for the database
    #MAPPER - map python objects to columns in DB
    #columnname = column ( column attributes , column attributes)
    name = Column(String(80), nullable = False) #nullable = false means column needs to have a value to create the row
    id = Column(Integer, primary_key=True) # uniquely identify each row 

    #Return object data in easily serializeable format
    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }

class MenuItem(Base):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course
        }

"""class Employee(Base):
	__tablename__ = 'employee'
	name = Column(String(250), nullable=False)
	id = Column(Integer, primary_key = True)

class Address(Base):
	__tablename__ = 'address'
	street = Column(String(80), nullable=False)
	zip = Column(String(5), nullable=False)
	id = Column(Integer, primary_key=True)
	employee_id = Column(Integer, ForeignKey('employee.id'))
	employee = relationship('Employee')
"""
#### CONFIGURATION END####
engine = create_engine('sqlite:///restaurantmenu.db')
### Create class code back into database table
Base.metadata.create_all(engine)