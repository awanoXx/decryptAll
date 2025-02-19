import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


def read_glyph_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 存储字形数据的字典
    glyph_data = {}

    # 遍历所有TTGlyph节点
    for glyph in root.findall('.//TTGlyph'):
        name = glyph.get('name')
        if name and name.startswith('uni'):
            points = []
            # 收集所有点的坐标
            for contour in glyph.findall('contour'):
                contour_points = []
                for pt in contour.findall('pt'):
                    x = int(pt.get('x'))
                    y = int(pt.get('y'))
                    contour_points.append((x, y))
                points.append(contour_points)

            # 存储字形数据
            unicode_value = '0x' + name[3:].lower()
            glyph_data[unicode_value] = points

    return glyph_data


def plot_glyph(points, title):
    plt.figure(figsize=(5, 5))
    plt.title(title)

    # 绘制每个轮廓
    for contour in points:
        # 添加第一个点到末尾以闭合轮廓
        contour = contour + [contour[0]]
        xs, ys = zip(*contour)
        plt.plot(xs, ys, 'b-')

    plt.axis('equal')
    plt.grid(True)
    plt.show()


# 使用示例
xml_file = 'font.xml'
glyph_data = read_glyph_data(xml_file)

# 可视化每个字形
print("字形可视化:")
for unicode_val, points in glyph_data.items():
    print(f"\n显示字形: {unicode_val}")
    plot_glyph(points, f"Unicode: {unicode_val}")