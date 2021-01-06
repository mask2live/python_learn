import pymysql

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


"""
    a database of books

    BookStore(Base)                              -- a table which contain infos about books
    get_session                                  -- an connection to database
    view_items                                   -- check all books in database
    
    [Can be optimized] 
    insert_item(self, title, author, year, isbn) -- insert a new book into database
    search_by(self, title, author, year, isbn)   -- query item by specified info
    delete_by_id(self, bid)                      -- delete an item by id
    update(self, bid, title, author, year, isbn) -- update an item by specified info

"""
class Book_Database:

    Base = declarative_base()
    engine = ''


    class BookStore(Base):
        __tablename__ = 'bookstore'
        bid = Column(Integer(), primary_key=True)
        title = Column(String(100), nullable=False)
        author = Column(String(100), nullable=False)
        year = Column(Integer())
        isbn = Column(Integer())

        def __str__(self):
            return f"{self.bid}: {self.title} {self.author} {self.year} {self.isbn}"


    def __init__(self, user, password, addr, db_name):

        dbURL = f'mysql+pymysql://{user}:{password}@{addr}:3306/{db_name}?charset=utf8mb4'
        self.engine = create_engine(dbURL, encoding='utf-8')
        self.Base.metadata.create_all(self.engine)

    
    def get_session(self):
        SessionClass = sessionmaker(bind=self.engine)
        session = SessionClass()

        return session


    def insert_item(self, title, author, year, isbn):

        session = self.get_session()

        item = self.BookStore(title=title, author=author, year=year, isbn=isbn)

        session.add(item)

        session.commit()


    def view_items(self):

        session = self.get_session()

        items = session.query(self.BookStore)

        session.commit()

        data = []
        for i in items:
            print(i)
            data.append(i.__str__())
        
        return data


    def search_by(self, title, author, year, isbn):
        
        session = self.get_session()

        result = session.query(self.BookStore).filter(self.BookStore.title==title, self.BookStore.author == author, self.BookStore.year == year, self.BookStore.isbn == isbn).all()

        session.commit()

        return result

    
    def delete_by_id(self, bid):
        
        session = self.get_session()

        session.query(self.BookStore).filter(self.BookStore.bid == bid).delete()

        session.commit()
    

    def update(self, bid, title, author, year, isbn):

        session = self.get_session()

        session.query(self.BookStore)\
            .filter(self.BookStore.bid == bid)\
            .update({
                self.BookStore.title : title,
                self.BookStore.author : author,
                self.BookStore.year : year,
                self.BookStore.isbn : isbn
                })

        session.commit()
    

db = Book_Database("database_info")


if __name__ == '__main__':

    # db.insert_item("testbook", 'tester', 2021, 99)
    # print(db.view_items())
    # print(db.search_by("testbook", 'tester', 2021, 99))
    # db.delete_by_id(5)

    db.update(6, "testbook6", 'tester6', 2021, 966)
    print(db.view_items())