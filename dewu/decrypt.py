# 得物商家后台签名生成
import json
import hashlib

def get_sign(params, salt="048a9c4943398714b356a696503d2d36"):
    def get_value_string(val):
        if val is None:
            return ""
        if isinstance(val, dict):
            return json.dumps(val, separators=(',', ':'), ensure_ascii=False)
        if isinstance(val, list):
            return ",".join([get_value_string(v) for v in val])
        return str(val)

    params_token = ""
    # 正序+盐
    for key in sorted(params.keys()):
        # 无论值是否为None，都应包含键
        params_token += key + get_value_string(params[key])

    params_token += salt

    # 计算并返回MD5哈希值
    return hashlib.md5(params_token.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    # 请求参数示例
    params = {"categoryLv1Id":"29","timeType":7,"startTime":"20240818","endTime":"20240818","topType":"industrySize","qualificationStatus":None}
    sign = get_sign(params)
    print(sign)