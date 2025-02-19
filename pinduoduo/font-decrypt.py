from fontTools.ttLib import TTFont
import xml.etree.ElementTree as ET


def read_psnames_from_font(font_url):
    # TTFont打开字体文件
    font = TTFont(font_url)
    # # 将字体文件保存为可读的xml文件
    font.saveXML(r'\\192.168.2.210\待删除\拼多多\数据中心商品\font.xml')

    tree = ET.parse(r'\\192.168.2.210\待删除\拼多多\数据中心商品\font.xml')
    root = tree.getroot()

    # 查找extraNames节点
    extranames = root.find('.//extraNames')
    if extranames is None:
        print("未找到extraNames节点")
        return []

    # 获取所有psName节点，保持原始顺序
    unicode_values = []
    for psname in extranames.findall('psName'):
        name = psname.get('name')
        if name and name.startswith('uni'):
            # 从'uni'后面提取Unicode值
            hex_value = '0x' + name[3:].lower()
            unicode_values.append(hex_value)

    print("按XML顺序的Unicode值:")
    for i, value in enumerate(unicode_values):
        print(f"{i}: {value}")

    print(unicode_values)
    # 创建一个字典来存储映射关系
    char_map = {}

    # 确保我们有足够的值进行映射
    if len(unicode_values) < 10:
        print(f"警告：找到的Unicode值数量不足10个 (只有{len(unicode_values)}个)")

    # 按照0-9的顺序创建映射
    for i, unicode_val in enumerate(unicode_values):
        if i < 10:  # 只映射0-9
            char_map[unicode_val] = str(i)
    print(char_map)
    return char_map


def decrypt_price(encrypted_text, char_map):
    unicode_values = [hex(ord(c)) for c in encrypted_text]
    # print("待解密文本的 Unicode 值:", unicode_values)

    print(char_map)
    result = ""

    for unicode_val in unicode_values:
        if unicode_val == '0x2e':  # 小数点
            result += '.'
        elif unicode_val == '0x25':  # 百分号
            result += '%'
        else:
            # 从映射表中获取对应的数字
            if unicode_val in char_map:
                result += char_map[unicode_val]
            # else:
            # print(f"未知字符映射: {unicode_val}")

    return result


def decrypt_json_data(json_data, char_map):
    if isinstance(json_data, dict):
        return {k: decrypt_json_data(v, char_map) for k, v in json_data.items()}
    elif isinstance(json_data, list):
        return [decrypt_json_data(item, char_map) for item in json_data]
    elif isinstance(json_data, str) and any(ord(c) >= 0xe000 for c in json_data):
        # 如果字符串包含私有区域的 Unicode 字符，则进行解密
        return decrypt_price(json_data, char_map)
    else:
        return json_data


if __name__ == '__main__':
    print("11111")
    tree = ET.parse(r'font4.xml')
    root = tree.getroot()

    # 查找extraNames节点
    extranames = root.find('.//extraNames')
    if extranames is None:
        print("未找到extraNames节点")

    # 获取所有psName节点，保持原始顺序
    unicode_values = []
    for psname in extranames.findall('psName'):
        name = psname.get('name')
        if name and name.startswith('uni'):
            # 从'uni'后面提取Unicode值
            hex_value = '0x' + name[3:].lower()
            unicode_values.append(hex_value)

    # print("按XML顺序的Unicode值:")
    # for i, value in enumerate(unicode_values):
    #     print(f"{i}: {value}")

    print(unicode_values)
    # 创建一个字典来存储映射关系
    char_map = {}

    # 确保我们有足够的值进行映射
    if len(unicode_values) < 10:
        print(f"警告：找到的Unicode值数量不足10个 (只有{len(unicode_values)}个)")

    # 按照0-9的顺序创建映射
    for i, unicode_val in enumerate(unicode_values):
        if i < 10:  # 只映射0-9
            char_map[unicode_val] = str(i)
    print(char_map)
    # json_data = '{"success":true,"errorCode":1000000,"errorMsg":null,"result":{"goodsDetailList":[{"statDate":"2025-01-15","goodsId":608147029788,"goodsName":"李宁童鞋跑步鞋男女大童2024新款减震回弹柔软支撑稳定低帮运动鞋","goodsFavCnt":"","goodsUv":"","goodsPv":"","payOrdrCnt":"","goodsVcr":".%","pctGoodsVcr":".%","payOrdrGoodsQty":"","payOrdrUsrCnt":"","payOrdrAmt":".","cfmOrdrCnt":"","cfmOrdrGoodsQty":"","goodsFavCntYtd":null,"goodsUvYtd":null,"goodsPvYtd":null,"payOrdrCntYtd":null,"goodsVcrYtd":".%","pctGoodsVcrYtd":".%","payOrdrGoodsQtyYtd":null,"payOrdrUsrCntYtd":null,"payOrdrAmtYtd":null,"cfmOrdrCntYtd":null,"cfmOrdrGoodsQtyYtd":null,"goodsUvPpr":0.4688,"goodsPvPpr":0.4419,"payOrdrCntPpr":0.0,"goodsVcrPpr":0.0,"cfmOrdrRtoPpr":0.0,"goodsFavCntPpr":2.0,"payOrdrGoodsQtyPpr":0.0,"payOrdrUsrCntPpr":0.0,"payOrdrAmtPpr":0.0,"cfmOrdrCntPpr":0.0,"cfmOrdrGoodsQtyPpr":0.0,"goodsUvPprIsPercent":true,"goodsPvPprIsPercent":true,"payOrdrCntPprIsPercent":false,"goodsVcrPprIsPercent":true,"cfmOrdrRtoPprIsPercent":true,"goodsFavCntPprIsPercent":true,"payOrdrGoodsQtyPprIsPercent":false,"payOrdrUsrCntPprIsPercent":false,"payOrdrAmtPprIsPercent":false,"cfmOrdrCntPprIsPercent":false,"cfmOrdrGoodsQtyPprIsPercent":false,"hdThumbUrl":"https://img.pddpic.com/gaudit-image/2024-06-24/7bb482f05f89732a95d175c90053be20.jpeg","cate3PctGoodsVcr":".%","cate3AvgGoodsVcr":".%","goodsVcrRised":-1,"cate3IsPgvAbove":0,"isCreated1m":0,"isNewstyle":0,"goodsLabel":null,"adStrategy":null,"url":null,"adStrategyStatus":5,"adStrategyDesc":"推广充值","adStrategyJumpUrl":"https://yingxiao.pinduoduo.com/marketing/main/undertake?channelId=100135&goodsId=608147029788","imprUsrCnt":"","imprUsrCntYtd":null,"imprUsrCntPpr":0.0,"imprUsrCntPprIsPercent":true,"imprUsrCntDetail":false,"ordrCrtUsrCnt":"","ordrCrtUsrCntYtd":"","ordrCrtUsrCntPpr":0.0,"ordrCrtUsrCntPprIsPercent":false,"ordrVstrRto":".%","ordrVstrRtoYtd":".%","ordrVstrRtoPpr":0.0,"ordrVstrRtoPprIsPercent":true,"payOrdrRto":".%","payOrdrRtoYtd":".%","payOrdrRtoPpr":0.0,"payOrdrRtoPprIsPercent":true,"goodsPtHelpRate":".%","goodsPtHelpRateRank":0.0,"goodsPtHelpRatePpr":0.0,"goodsPtHelpRatePprIsPercent":true,"cate1Id":14933,"cate1Name":"童鞋/婴儿鞋/亲子鞋","cate2Id":14948,"cate2Name":"运动鞋","cate3Id":14965,"cate3Name":"运动鞋","peerPerfPayOrdrAmt":1,"peerPerfGoodsUv":4,"peerPerfGoodsPv":4,"peerPerfGoodsFavCnt":4,"peerPerfGoodsCvr":1,"peerPerfOrdrVstrRto":1,"peerPerfPayOrdrRto":1,"peerPerfGoodsPtHelpRate":null,"activityInfo":{"activityType":43,"themeActivityId":null,"activityId":21312,"goodsBenefitLabel":null,"goodsBenefitSales":null,"goodsBenefitPrice":"￥157.99","enrollActionPointDesc":null,"priority":4,"isExitActivity":false,"goodsMetricDecreaseDesc":null,"activityName":"百亿补贴","enrollActivityDesc":"以￥157.99报名百亿补贴","isExperimentalGroup":true},"showCol":0,"hotGoodsActivityInfo":{"desc":"爆单啦！恭喜解锁保权重权益","showEntry":false}}],"totalNum":88,"timestamp":1736992391928,"delayData":0}}'
    print(decrypt_price('', char_map))
    pass
