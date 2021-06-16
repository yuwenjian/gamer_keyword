import json
import time
import random
import requests
from pandas.io.json import json_normalize

totalUrlResult = ""
def startNetQuest(startNum):
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
         ('q', '開催'),
         ('safe', 'off'),
         ('cse_tok', 'AJvRUv0CIlgcM24dXIpK-JW-U9OM:1621569223431'),
         ('filter', 1),
         ('sort', ''),
         ('exp', 'csqr,cc'),
         ('callback', 'google.search.cse.api1295'),
     )

     response = requests.get(baseUrl, headers=headers, params=params, verify=False)
     UrlResult = response.text
     parseResult(UrlResult)
     # print("=====当前是第 "+startNum / 20+" 页====")




def parseResult(dataUrl):
    # f = open('result', 'r')
    # lines = f.readlines()
    # resulta = "".join(lines)
    aa = dataUrl[34:-2]

    result = []
    for rr in json.loads(aa)["results"]:
        print(rr["cacheUrl"])
        temp = {
            'keyUrl': rr["formattedUrl"],
            'title': rr["title"]
        }
        result.append(temp)

    df = json_normalize(result)
    df.to_csv("开催Url.csv", mode="a+", header=False, encoding='utf-8', index=False)


if __name__ == '__main__':
    pages =[0, 1, 2, 3, 4, 5]
    for page in pages:
        startNum = page * 20
        time.sleep(random.randint(20, 40))
        startNetQuest(startNum)