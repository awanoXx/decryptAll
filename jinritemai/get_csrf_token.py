import requests

def get_csrf_token(url, cookie):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Cookie": cookie,
        "Pragma": "no-cache",
        "Priority": "u=1, i",
        "Referer":
        "https://compass.jinritemai.com/shop/mall-analysis?from_page=%2Fshop%2Fmall-recommend&btm_ppre=a6187.b01487.c0.d0&btm_pre=a6187.b7405.c0.d0&btm_show_id=b714c5ee-b602-4653-a314-2b6c6d5f793c",
        "Sec-CH-UA":
        '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "X-SecSdk-Csrf-Request": "1",
        "X-SecSdk-Csrf-Version": "1.2.22"
    }

    response_head = requests.session().head(url, headers=headers)
    if 'x-ware-csrf-token' in response_head.headers.keys() :
        return response_head.headers['x-ware-csrf-token'].split(',')[1]
    return ""

