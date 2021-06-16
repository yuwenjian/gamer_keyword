import pandas as pd
from sqlalchemy import create_engine
import pymysql


# 链接数据库
def connect_Db():
    engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', 'Woshiyuwenjian12', 'localhost', '3306', 'news_db'))
    read_Db(engine)

# 读取数据库
def read_Db(engine):
    # 填写自己所需的SQL语句，可以是复杂的查询语句
    sql_query = 'select * from new;'
    df_read = pd.read_sql_query(sql_query, engine)
    print(df_read)

# 写入数据
def write_Db():
    db = pymysql.connect(host='localhost', user='root', password='Woshiyuwenjian12', port=3306, db='news_db')
    cursor = db.cursor()
    data = {
        'article_title': 'mm',
        'article_url': "http://www.baidu.com",
        'article_time': "2020-03-20",
        'keyword': "关键字",
        'source_name': "百度资源"
    }
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
    write_Db()
