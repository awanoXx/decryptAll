import requests
import execjs
from urllib.parse import quote
import hashlib
import json
import time
import random
import string

#适用数据罗盘、策略、抖店、千川

def get_a_bogus(js_file, req_str):
    a_bogus = execjs.compile(open(js_file).read()).call("get_a_bogus", [0, 1, 14, req_str, '', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'])
    print(a_bogus)
    return f"{a_bogus}"

# qc-key、qc-date、qc-auth
def qc_header(api, post_data, method):
    # 生成随机字符串
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    # 当前时间戳
    timestamp = str(int(time.time() * 1000))

    # 将JSON对象转换为字符串
    post_data_str = json.dumps(post_data, separators=(',', ':'))
    print(post_data_str)
    # 拼接字符串
    method = "POST"  # 在此处插入对应的t值
    joined_str = f"{random_str}X&Y{post_data_str}M#N{method}M#N{api}M#N{timestamp}X&Y{random_str}"
    print(joined_str)
    # 计算MD5哈希值
    md5_hash = hashlib.md5(joined_str.upper().encode('utf-8')).hexdigest()

    # 打印结果
    return [random_str,timestamp,md5_hash]

def urlencode(datetime_str):
    # 对格式化后的字符串进行URL编码
    encoded_date_str = quote(datetime_str, safe='=&')
    return encoded_date_str

def encode_reqstr(req_str):
    # 替换成自己的请求参数、verifyFp、msToken、_lid生成见js文件
    fp = 'verify_m22px9k7_7e258dd0_5246_117a_bd93_f579deb907fc'
    msToken = 'LY79HIaPCsE3B9CKX2vZ5IsN__bJIxkcfm6j1VX6T2zLNF-Hu-Ow01DHBlEU6yEJwwZ7whsHCNCiYW4sfbWXoBrIrasCF_VPRnSNFF2tL5aeROisVwdamvXTbmMb'
    # 千川没有_lid
    _lid = '220805677153'
    return req_str + f"&_lid={_lid}&verifyFp={fp}&fp={fp}&msToken={msToken}"

if __name__ == '__main__':
    #demo
    req_str = 'begin_date=2024/10/10 00:00:00&end_date=2024/10/10 00:00:00&date_type=2&activity_id=&search_info=&brand_type=1&category_id=20046&industry_id=18&top_myshop=true&sort_field=flow_index&is_asc=false&page_no=1&page_size=10'
    req_str = urlencode(encode_reqstr(req_str))
    a_bogus = get_a_bogus('./bdms.js', req_str)
    # http 请求
    req_url = f"https://compass.jinritemai.com/compass_api/shop/mall/shop_rank/product_card?{req_str}&a_bogus={a_bogus}"
    # 填上自己的header
    headers = {}

    response = requests.get(url=req_url,headers=headers)
    print(response.status_code)  # 打印状态码
    print(response.text)  # 打印响应内容
