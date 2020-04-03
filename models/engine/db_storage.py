#!/usr/bin/python3
"""
    Define class DBStorage
"""
#  ██████╗ ██████╗ ███████╗████████╗ ██████╗ ██████╗  █████╗  ██████╗ ███████╗
#  ██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔══██╗██╔════╝ ██╔════╝
#  ██║  ██║██████╔╝███████╗   ██║   ██║   ██║██████╔╝███████║██║  ███╗█████╗
#  ██║  ██║██╔══██╗╚════██║   ██║   ██║   ██║██╔══██╗██╔══██║██║   ██║██╔══╝
#  ██████╔╝██████╔╝███████║   ██║   ╚██████╔╝██║  ██║██║  ██║╚██████╔╝███████╗
#  ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝


from os import getenv
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """
        Class for Database Storage MySQL
    """

    __engine = None
    __session = None

    def __init__(self):
        """
            Instance for Database Storage
        """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Query on the current database session all object
            Or the specified if cls is not none
        """
        db_dict = {}

        if cls is not None:
            input_db = self.__session.query(models.classes[cls]).all()
            for obj in input_db:
                # under the hood, sqlalchemy converts entry as input
                # to objects allowing access to object attributes
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
        else:
            for key, value in models.classes.items():
                for obj in self.__session.query(value).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    db_dict[key] = obj
        return db_dict

    def new(self, obj):
        """
            Add the object at the current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
            Commit's all changes of the current database session
        """
        self.__session.commit()

    def reload(self):
        """
            Creates the current database session
        """
        # Makes all the tables in the database which are
        # defined by Base's subclasses
        Base.metadata.create_all(self.__engine)
        # create a configured factory class
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        # create a global session for all to use
        Session = scoped_session(session_maker)
        self.__session = Session()

    def delete(self, obj=None):
        """
             Delete from the current database session
        """

        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """
            Close and clears all items and ends any transaction in progress
        """
        self.__session.close()
