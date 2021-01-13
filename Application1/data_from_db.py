import pymysql

from dbutils.pooled_db import PooledDB

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import json

db_config_ardit = {
    'host' : '108.167.140.122',
    'port' : 3306,
    'user' : 'ardit700_student',
    'passwd' : 'ardit700_student',
    'db' : 'ardit700_pm1database',
    'charset' : 'utf8mb4',
    'maxconnections' : 0,    
    'mincached' : 4,    
    'maxcached' : 0,
    'maxusage' : 5,
    'blocking' : True
}


db_config = {
    'host' : '',
    'port' : 3306,
    'user' : 'root',
    'passwd' : '',
    'db' : 'dbtest',
    'charset' : 'utf8mb4',
    'maxconnections' : 0,    
    'mincached' : 4,    
    'maxcached' : 0,
    'maxusage' : 5,
    'blocking' : True
}


def conn_in_pool():

    spool = PooledDB(pymysql, **db_config_ardit)

    conn = spool.connection()
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM Dictionary;'
        sql1 = 'SHOW CREATE TABLE Dictionary;'
        cursor.execute(sql1)
        f = cursor.fetchall()
        print(f)






class Dictionary_Database:

    Base = declarative_base()
    engine = ''


    class Dictionary(Base):
        __tablename__ = 'dictionary'
        wid = Column(Integer(), primary_key=True)
        word = Column(String(100))
        definition = Column(String(5000))


    def __init__(self, user, password, addr, db_name):

        dbURL = f'mysql+pymysql://{user}:{password}@{addr}:3306/{db_name}?charset=utf8mb4'
        self.engine = create_engine(dbURL, encoding='utf-8')
        self.Base.metadata.create_all(self.engine)

    
    def get_session(self):
        SessionClass = sessionmaker(bind=self.engine)
        session = SessionClass()

        return session


    def query_by_word(self, word):

        session = self.get_session()

        defin = session.query(self.Dictionary.definition).filter(self.Dictionary.word == word).first()

        session.commit()
        return defin

        


    def intialize_dictionary(self, filePath):
        
        data = json.load(open(filePath, 'r'))

        session = self.get_session()

        for word, defini in data.items():
            definition = list2String(defini)
            item = self.Dictionary(word=word, definition=definition)
            session.add(item)

        session.commit()


def list2String(l: list):
        s = ""
        for string in l:
            s = s + string + " "
        return s


if __name__ == '__main__':

    db = Dictionary_Database("admin", 'password', 'ip_address', 'db_name')

    # db.intialize_dictionary('Application1/data.json')

    word = db.query_by_word('aaaaaa')
    print(word)