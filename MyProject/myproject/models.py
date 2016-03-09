from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Thing(Base):
    """ The SQLAlchemy declarative model class for a Person object. """
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    result = Column(Text, unique=False)

# class Equation(Base):
#     """ The SQLAlchemy declarative model class for a Person object. """
#     __tablename__ = 'equations'
#     id = Column(Integer, primary_key=True)
#     firstIngredient = Column(Text, unique=False)
#     secondIngredient = Column(Text, unique=False)
#     resultIngredient = Column(Text, unique=False)




