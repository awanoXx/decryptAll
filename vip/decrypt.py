import hashlib
from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto.Util.Padding import unpad
import base64

def aes_encrypt(msg, secret):
    cipher = AES.new(secret.encode('utf-8'), AES.MODE_ECB)
    pad_msg = msg + (16 - len(msg) % 16) * chr(16 - len(msg) % 16)
    encrypted = cipher.encrypt(pad_msg.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

def derive_key_and_iv(password, salt, key_length, iv_length):
    d = d_i = b""
    while len(d) < key_length + iv_length:
        d_i = MD5.new(d_i + password + salt).digest()
        d += d_i
    return d[:key_length], d[key_length:key_length + iv_length]

def aes_decrypt(encrypted_msg, secret):
    # Base64 解码密文
    encrypted_data = base64.b64decode(encrypted_msg)

    salt = encrypted_data[8:16]
    ciphertext = encrypted_data[16:]

    # 根据密码和 salt 生成密钥和 IV
    key, iv = derive_key_and_iv(secret.encode('utf-8'), salt, 32, 16)

    # 创建 AES 解密器，使用 CBC 模式
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 解密并去除填充
    decrypted_data = cipher.decrypt(ciphertext)
    try:
        return unpad(decrypted_data, AES.block_size).decode('utf-8')
    except ValueError:
        print("解密失败，返回原始内容：")
        return decrypted_data.hex()

def sha1(msg):
    return hashlib.sha1(msg.encode('utf-8')).hexdigest()

def hash_param(params):
    del params['api_key']
    # 将参数按键名排序
    sorted_keys = sorted(params.keys())
    result = []

    # 拼接键值对为字符串
    for key in sorted_keys:
        result.append(f"{key}={params[key]}")

    # 用 & 连接键值对
    concatenated_params = "&".join(result)
    print(f"concatenated_params: {concatenated_params}")
    # 返回哈希化后的参数
    return sha1(concatenated_params)

def get_st(key):
    # 已加密的密钥表，不同端
    encrypted_keys = {
        "70f71280d5d547b2a7bb370a529aeea1": "U2FsdGVkX197SM3Eh62XyjAwTXznW9DdALdNR1gKNsewAg3fzwA0x/+UQldlbi3oYBn8eFHgTtBUcGneYPCjIA==",
        "8cec5243ade04ed3a02c5972bcda0d3f": "U2FsdGVkX1+ZmG8rT/n9qDbrWBnK0K3G0gsoPo0N6/6qx8AklnZmXLyulj0KAy07ixFAu6oMKmOY0+VH3DjQ2Q==",
        "adf779847ac641dd9590ccc5674e25d2": "U2FsdGVkX1/VI+95aRUsSZCDB3rmMe2DPSUO+rSH7U/tlNnA5u9anTM3oHI+XgIeHWA5XDAo0Z19ddwzFeHFXA=="
    }

    # 获取目标加密密钥
    encrypted_key = encrypted_keys.get(key)
    if not encrypted_key:
        raise ValueError("Key not found in encrypted keys")

    # 解密密钥
    return aes_decrypt(encrypted_key, "qyrohlf5sjazleru")

def get_sign(input_params, mars_cid, mars_sid):
    # 预定义的变量
    request_path = "/vips-mobile/rest/shopping/pc/detail/main/v6"  # 固定接口路径
    hashed_params = hash_param(input_params)  # 已排序并拼接的参数
    decrypted_key = get_st(api_key)  # 来源自请求参数的api_key
    print(f"hashed_params: {hashed_params}")
    print(f"mars_cid: {mars_cid}")
    print(f"mars_sid: {mars_sid}")
    print(f"decrypted_key: {decrypted_key}")
    decrypted_key = 'ea6f62dad8ee40638832f3bd125f1a37'

    # 使用 SHA1 加密生成签名
    sign_result = sha1(request_path + hashed_params + mars_sid + mars_cid + decrypted_key)
    print(request_path + hashed_params + mars_sid + mars_cid + decrypted_key)
    # 添加签名前缀
    sign_result = "OAuth api_sign=" + sign_result
    return sign_result

def main(args):
    # 请求参数
    input_params = {"app_name":"shop_pc","app_version":"4.0","warehouse":"VIP_NH","fdc_area_id":"","client":"pc","mobile_platform":"1","province_id":"","api_key":"","user_id":"","mars_cid":"","wap_consumer":"c","is_default_area":"1","scene":"detail","productId":"6921016273020048285","opts":"priceView:13;quotaInfo:1;restrictTips:1;panelView:3;foreShowActive:1;invisible:1;floatingView:1;announcement:1;svipView:2;showSingleColor:1;svipPriceMode:1;promotionTips:6;foldTips:3;formula:2;extraDetailImages:1;shortVideo:1;countryFlagStyle:1;saleServiceList:1;storeInfo:2;brandCountry:1;freightTips:3;priceBannerView:1;bannerTagsView:1;buyMoreFormula:1;mergeGiftTips:0;kf:1;priceIcon:1;tuv:3;promotionTags:7;mergeGiftTips:3;topDetailImage:2;deliveryInfo:1;installServiceList:1;relatedProdSpu:1","tfs_fp_token":""}
    mars_cid = '' #来自cookie
    mars_sid = '' #来自cookie
    # 生成签名
    sign = get_sign(input_params, mars_cid, mars_sid)
    print(sign)
    pass
