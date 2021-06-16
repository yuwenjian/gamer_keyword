import json
import time
import random
import requests
from lxml import etree
from select_game.Db_unitl import write_Db
keyword = ""
def startRequest(keyword, gameLookBaseUrl2):
    gameLookBaseUrl = "http://www.gamelook.com.cn/?s=" + keyword

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "UM_distinctid=179abb7132050f-0ea1c4988ff10a-113a6054-384000-179abb713219e0; CNZZDATA1687346=cnzz_eid%3D695419067-1622080444-%26ntime%3D1622096650",
        "Host": "www.gamelook.com.cn",
        "Referer": "http://www.gamelook.com.cn/?s=%E4%B8%A4%E4%B8%AA",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    if len(gameLookBaseUrl2) == 0:
        response = requests.get(gameLookBaseUrl, headers=headers)
    else:
        response = requests.get(gameLookBaseUrl2, headers=headers)
    html = etree.HTML(response.text)
    getData(html)

# 获取数据
def getData(html):
    titleList = html.xpath('//div[@class="archive-list category-list"]/ul[@class="article-list clearfix"]/li[@class="item"]/div[@class="item-content"]/h2[@class="item-title"]/a/@title')
    aricteUrlList = html.xpath('//div[@class="archive-list category-list"]/ul[@class="article-list clearfix"]/li[@class="item"]/div[@class="item-content"]/h2[@class="item-title"]/a/@href')
    arictUrlTimeList = html.xpath('//div[@class="archive-list category-list"]/ul[@class="article-list clearfix"]/li[@class="item"]/div[@class="item-content"]/div[@class="item-meta"]/span/text()');
    # 判断是否有下一页
    isNextPage = html.xpath('//div[@class="archive-list category-list"]/div[@class="pagination clearfix"]/a[@class="next"]/@href')
    resultList= []
    for i in range(0, len(titleList)):
        result = {
            'article_title': titleList[i],
            'article_url': aricteUrlList[i],
            'article_time': arictUrlTimeList[i],
            'keyword': keyword,
            'source_name': "GameLook"
             }
        saveData(result)
        # resultList.append(result)

    if len(isNextPage) == 0:
        print("全部爬完了")
    else:
        time.sleep(random.randint(2, 5))
        startRequest(keyword, isNextPage[0])

# 存数据
def saveData(result):
    write_Db(result)



if __name__ == "__main__":
    print("开始网络请求！")
    keyword = "开催"
    startRequest(keyword, "")
