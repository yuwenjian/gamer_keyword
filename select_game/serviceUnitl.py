from flask import Flask, jsonify
from Db_unitl import read_Db
from JpGame import startNetQuest
from flask import request
import time
import random


app = Flask(__name__)


# 开始爬虫
@app.route('/startGrab', methods=['GET'])
def startGrab():
    request_data = request.args.to_dict()
    keyword = request_data.get('keyword')
    pages =[0,1,2,3,4,5]
    for page in pages:
        time.sleep(random.randint(10, 20))
        startNetQuest((page * 20), keyword)
    return jsonify({'message': "爬取完成！"})

# 获取爬取的信息
@app.route('/getnew', methods=['GET'])
def getNews():
    request_data = request.args.to_dict()
    keyword = request_data.get('keyword')
    result = read_Db(keyword)
    print(type(result))
    return jsonify(result)

if __name__ == '__main__':
    app.run()
