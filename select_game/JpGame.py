import json
import random
import re
import time
import requests
from Db_unitl import write_Db

totalUrlResult = ""
def startNetQuest(startNum, keyword):
     global totalUrlResult
     baseUrl = "https://cse.google.com/cse/element/v1"

     headers = {
         "sec-ch-ua": "' Not A;Brand';v='99', 'Chromium';v='90', 'Google Chrome';v='90'",
         "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
         "accept-language": "zh-CN,zh;q=0.9",
         "cookie": "__Secure-3PSID=9Qe67rSHAWLB2VTQ4bKxTtT8AOciSX8FHEoiKvJLH0KFwvmaV3NMxDcBFUFhbt7eRzTaiQ.; __Secure-3PAPISID=EY1AfrF_NLQTuEUA/AN99GODnGtCONPmE4; NID=216=EhwnXRkqRjvxlqNnVmKuBJUtkIYguwsBk9YT7QpDmaCrJ_pzgPEloBdyo0C8bCYVaLh4_WhyRxX8bmcKhVKTWNhQ3Y751HGb_FmPxd_oCTelka6JATVk9l1Wis4EyGD__co9zC9A-SAc-pr1hUg1ipinpIvjqVLYFJlQ4L5a2VlzKDThwqZEU9AxmE4wmo4GsgpJLIRRDw8oYk6t454zAgXvt-xx9E1GfBZUJl4xFaZaS-GHy1CvBh16uyvHkopWvGk-hpxdcCRLFmc274UlKmVL05AGLtMpww; 1P_JAR=2021-05-21-03; __Secure-3PSIDCC=AJi4QfHqGhVEkUf-J_UFVafLeW-gfCbcYOE_D1YWmj4GRTR4wWD72ujKUp-LLE1o-ffGVOtcWYo"
     }
     params = (
         ('rsz', 20),
         ('num', 20),
         ('hl', 'ja'),
         ('source', 'gcsc'),
         ('gss', '.com'),
         ('start', startNum),
         ('cselibv', '323d4b81541ddb5b'),
         ('cx', '008277887561957062446:paqn5nbl6hs'),
         ('q', keyword),
         ('safe', 'off'),
         ('cse_tok', 'AJvRUv0JUloKV7yzTNoODS9tATSv:1624002709755'),
         ('filter', 1),
         ('sort', 'date'),
         ('exp', 'csqr,cc'),
         ('callback', 'google.search.cse.api4073'),
     )

     response = requests.get(baseUrl, headers=headers, params=params, verify=False)
     UrlResult = response.text
     parseResult(UrlResult, keyword)

def parseResult(dataUrl, keyword):
    aa = dataUrl[34:-2]
    for rr in json.loads(aa)["results"]:
        str1 = rr["formattedUrl"]
        it = re.findall(r"\d+", str1)
        article_time = it[len(it) - 1]
        temp = {
            'article_url': rr["formattedUrl"],
            'article_title': rr["title"],
            'article_time': article_time,
            'keyword': keyword,
            'source_name': "4gamer"
        }
        print(temp)
        write_Db(temp)

if __name__ == '__main__':
    pages =[0]
    keyword = '配布'
    for page in pages:
        startNum = page * 20
        time.sleep(random.randint(20, 40))
        startNetQuest(startNum, keyword)