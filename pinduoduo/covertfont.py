from fontTools.ttLib import TTFont
import xml.etree.ElementTree as ET

# TTFont打开字体文件
font = TTFont("95788c1a07c548b9bf556f150c9829c2-a0148bfb2eea4bcca5943fb86a2cb23d.ttf")
# # 将字体文件保存为可读的xml文件
font.saveXML('font4.xml')
