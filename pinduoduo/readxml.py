import xml.etree.ElementTree as ET


def read_psnames_from_xml(xml_file):
    # 解析XML文件
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 查找extraNames节点
    extranames = root.find('.//extraNames')
    if extranames is None:
        print("未找到extraNames节点")
        return []

    # 获取所有psName节点
    psnames = []
    for psname in extranames.findall('psName'):
        name = psname.get('name')
        if name:
            psnames.append(name)

    return psnames

# 使用示例
xml_file = 'font4.xml'  # 替换为你的XML文件路径
psnames = read_psnames_from_xml(xml_file)
print("找到的psName值:")
for name in psnames:
    print(name)