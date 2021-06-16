import requests
import json


def startRequest():

    baseUrl = "https://xindong.slack.com/api/conversations.history"

    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-length": "1178",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryGiYthxqTLmDviF7y",
        "cookie": "_gcl_au=1.1.126641886.1619408608; _fbp=fb.1.1619408609652.1613755984; __adroll_fpc=02b22d653f6be4b703d37cb4a4433699-1619408609970; _lc2_fpi=e00b11ac9c9b--01f464crp0fbn0kv2x7g47sa49; __qca=P0-658470046-1619408610434; G_ENABLED_IDPS=google; b=.cccnyhg7xjdpjosvol6oa41gi; shown_ssb_redirect_page=1; shown_download_ssb_modal=1; show_download_ssb_banner=1; no_download_ssb_banner=1; _ga=GA1.3.1676926231.1619408609; optimizelyEndUserId=oeu1619422279676r0.9318870454542343; ssb_instance_id=14a17425-3787-5678-aff2-1bd5dc5a6a65; __ar_v4=4UHU5P4P3FESHLUMNBLWAU%3A20210426%3A9%7CQCM34G7NBZEHHATIFDIUBJ%3A20210426%3A9%7CK2HN2U4VSJGOVKC2WJLQNH%3A20210426%3A7%7CKDMBLDIYHFHI5NUNKGJ4LV%3A20210426%3A2; _li_dcdm_c=.slack.com; _gid=GA1.2.389542877.1621997518; d=4z4rNB3NIGCHKGHNZrD8B1BB0gL%2FM%2BlEdfRc64DlLIi8llGClj3zfbgGNBe7Pv%2FOr09%2B6SMBgMLJbHFdOV0%2FhJkKbH2fhXwWTq5OCHDhZn0a5Lt%2BJdSo%2FSW0gJDWM5W83Aah37ZlKC5JsKiSpmNf7xXqYXNeT%2BrmGK7Dz1JJvK544jFCMSZzEA%3D%3D; d-s=1621997807; lc=1621997807; _ga=GA1.1.1676926231.1619408609; OptanonConsent=isIABGlobal=false&datestamp=Wed+May+26+2021+14%3A56%3A23+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.12.0&hosts=&consentId=8e08f985-7c0d-45a8-a470-9576e296e653&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false&geolocation=%3B; OptanonAlertBoxClosed=2021-05-26T06:56:23.038Z; _ga_QTJQME5M5D=GS1.1.1622011500.5.1.1622012189.0",
        "origin": "https://app.slack.com",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }

    params = (
        ("_x_id", "7e87ac7b-1622018107.761"),
        ("_x_csid", "M_RZOd3nV5M"),
        ("slack_route", "T02AYQYFS"),
        ("_x_version_ts", "1621988215"),
        ("_x_gantry", "true"),
        # ("channel", "C01LMCCV69Y"),
        # ("limit", "28"),
        # ("ignore_replies", "true"),
        # ("include_pin_count", "true"),
        # ("inclusive", "true"),
        # ("no_user_profile", "true"),
        # ("token", "xoxc-2372848536-2005643166708-1992701745158-581989beb1bc5de75fbbfb950b26cd1f2c66baf4a0d079ab597a8a4dc83dbc6d"),
        # ("_x_reason", "requestOfflineHistory"),
        # ("_x_mode", "online")

    )


    data = {
        'limit': (None, 28),
        'ignore_replies': (None, "true"),
        'include_pin_count': (None, "true"),
        'inclusive': (None, "true"),
        'no_user_profile': (None, "true"),
        'token': (None, "xoxc-2372848536-2005643166708-1992701745158-581989beb1bc5de75fbbfb950b26cd1f2c66baf4a0d079ab597a8a4dc83dbc6d"),
        '_x_reason': (None, "requestOfflineHistory"),
        '_x_mode': (None, "online")
    }

    response = requests.post(baseUrl, params=params, files=data)
    print(response.status_code, response.text)

if __name__ == '__main__':
    startRequest()