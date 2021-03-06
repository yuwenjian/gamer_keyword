from flask import Flask, jsonify
from JpGame import startNetQuest, saveForLocalFile
from Db_unitl import read_Db
from flask import request
import time
import random
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)


# 开始爬虫
@app.route('/startGrab', methods=['GET'])
@cross_origin()
def startGrab():
    request_data = request.args.to_dict()
    keyword = request_data.get('keyword')
    pages =[0]
    for page in pages:
        time.sleep(random.randint(10, 20))
        startNetQuest((page * 20), keyword)
    return jsonify({'message': "爬取完成！"})

# 获取爬取的信息
@app.route('/getnew', methods=['GET'])
@cross_origin()
def getNews():
    request_data = request.args.to_dict()
    keyword = request_data.get('keyword')
    result = read_Db(keyword)
    print(type(result))
    return jsonify(result)

# 保存爬取的信息
@app.route('/saveNew', methods=['GET'])
@cross_origin()
def saveNews():
    saveForLocalFile()
    return jsonify({'message': "保存完成！"})

if __name__ == '__main__':
    app.run(host="172.17.0.13", port="5000", debug=True)
