import pymysql

from dbutils.pooled_db import PooledDB

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

    spool = PooledDB(pymysql, **db_config)

    conn = spool.connection()
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM bookstore;'
        sql1 = 'SHOW CREATE TABLE dictionary;'
        cursor.execute(sql)
        f = cursor.fetchall()
        print(f)



spool = PooledDB(pymysql, **db_config)
conn = spool.connection()
table_name = "bookstore"


def insert_mysql(title, author, year, isbn):
    with conn.cursor() as cursor:
        insert_sql = f"insert into {table_name} values ({title}, {author}, {year}, {isbn});"
        cursor.execute(insert_sql)


def view_items_mysql():
    with conn.cursor() as cursor:
        view_sql = f"select * from {table_name};"
        cursor.execute(view_sql)
        result = cursor.fetchall()
    return result

"""
    Bug -- SQL syntax error
"""
def search_mysql(title="", author="", year="", isbn=""):
    with conn.cursor() as cursor:
        search_sql = f"SELECT * FROM {table_name} WHERE title={title} OR author={author} OR year={year} OR isbn={isbn}"
        cursor.execute(search_sql)
        result = cursor.fetchall()
    return result


if __name__ == "__main__":
    print(search_mysql(author="MK"))