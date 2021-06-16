import pandas as pd
from sqlalchemy import create_engine
import pymysql

from flask import Flask, jsonify, abort, request
app = Flask(__name__)


# 连接接数据库
def connect_Db():
    engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', 'Woshiyuwenjian12', 'localhost', '3306', 'news_db'))
    read_Db(engine)

# 读取数据库
def read_Db(keyword):

    host = 'localhost'
    user = 'root'
    password = 'Woshiyuwenjian12'
    database = 'news_db'
    port = 3306
    conn = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(user, password, host, port, database))
    sql = 'select * from new where keyword="'+str(keyword)+'"'
    results = pd.read_sql(sql, conn)
    print(results)
    results1 = results.to_dict(orient='index')
    print(type(results1))

    return results1

# 写入数据
def write_Db(data):
    db = pymysql.connect(host='localhost', user='root', password='Woshiyuwenjian12', port=3306, db='news_db')
    cursor = db.cursor()
    table = 'new'
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                         values=values)
    update = ','.join([" {key} = %s".format(key=key) for key in data])
    sql += update
    try:
        cursor.execute(sql, tuple(data.values()) * 2)
        print('Successful')
        db.commit()
    except:
        print('Failed')
        db.rollback()
    cursor.close()
    db.close()

if __name__ == "__main__":
    read_Db("开催")
