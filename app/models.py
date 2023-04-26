import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name



class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                  Column('employee_id', Integer, ForeignKey('employee.id'))
)


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name

class MenuItem(Model):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    link = Column(String(150), nullable=False)
    menu_category_id = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    menu_category = relationship("MenuCategory")

class MenuCategory(Model):
    __tablename__ = 'menu_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('news_category.id'), nullable=False)
    newsCat = relationship("NewsCategory")

class NewsCategory(Model):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String

class Channel(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=False)

from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship

class Program(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    air_time = Column(Time, nullable=False)
    channel_id = Column(Integer, ForeignKey('channel.id'))
    channel = relationship('Channel')



class Episode(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    air_date = Column(Date, nullable=False)
    program_id = Column(Integer, ForeignKey('program.id'))
    program = relationship('Program')

    from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String

class Genre(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    from flask_appbuilder import Model
from sqlalchemy import Column, Integer, ForeignKey

class ProgramGenre(Model):
    id = Column(Integer, primary_key=True)
    program_id = Column(Integer, ForeignKey('program.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))

  

class Subscription(Model):
    id = Column(Integer, primary_key=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    channel_id = Column(Integer, ForeignKey('channel.id'))
    channel = relationship('Channel')

 

class Payment(Model):
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')


class Review(Model):
    id = Column(Integer, primary_key=True)
    rating = Column(Float, nullable=False)
    comments = Column(String(255), nullable=False)
    program_id = Column(Integer, ForeignKey('program.id'))
    program = relationship('Program')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')

    

class Favorite(Model):
    id = Column(Integer, primary_key=True)
    program_id = Column(Integer, ForeignKey('program.id'))
    program = relationship('Program')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')