from fontTools.ttLib import TTFont
import xml.etree.ElementTree as ET

# TTFont打开字体文件
# font = TTFont("3a8b04f1-ad7e-497e-9756-5ad9699f3995.otf")
# # 将字体文件保存为可读的xml文件
# font.saveXML('font.xml')
# 找字体的映射关系，字体的映射关系在cmap中体现

# 解析XML内容
xml_content = '''  <cmap>
    <tableVersion version="0"/>
    <cmap_format_4 platformID="0" platEncID="3" language="0">
      <map code="0x20" name="space"/><!-- SPACE -->
      <map code="0x25" name="percent"/><!-- PERCENT SIGN -->
      <map code="0x2b" name="plus"/><!-- PLUS SIGN -->
      <map code="0x2c" name="comma"/><!-- COMMA -->
      <map code="0x2d" name="hyphen"/><!-- HYPHEN-MINUS -->
      <map code="0x2e" name="period"/><!-- FULL STOP -->
      <map code="0x30" name="zero"/><!-- DIGIT ZERO -->
      <map code="0x31" name="one"/><!-- DIGIT ONE -->
      <map code="0x32" name="two"/><!-- DIGIT TWO -->
      <map code="0x33" name="three"/><!-- DIGIT THREE -->
      <map code="0x34" name="four"/><!-- DIGIT FOUR -->
      <map code="0x35" name="five"/><!-- DIGIT FIVE -->
      <map code="0x36" name="six"/><!-- DIGIT SIX -->
      <map code="0x37" name="seven"/><!-- DIGIT SEVEN -->
      <map code="0x38" name="eight"/><!-- DIGIT EIGHT -->
      <map code="0x39" name="nine"/><!-- DIGIT NINE -->
      <map code="0xa0" name="space"/><!-- NO-BREAK SPACE -->
      <map code="0xa5" name="yen"/><!-- YEN SIGN -->
      <map code="0x2212" name="minus"/><!-- MINUS SIGN -->
      <map code="0x4e07" name="uni4E07"/><!-- CJK UNIFIED IDEOGRAPH-4E07 -->
      <map code="0x4ebf" name="uni4EBF"/><!-- CJK UNIFIED IDEOGRAPH-4EBF -->
      <map code="0x5143" name="uni5143"/><!-- CJK UNIFIED IDEOGRAPH-5143 -->
      <map code="0x5206" name="uni5206"/><!-- CJK UNIFIED IDEOGRAPH-5206 -->
    </cmap_format_4>
    <cmap_format_4 platformID="3" platEncID="1" language="0">
      <map code="0x20" name="space"/><!-- SPACE -->
      <map code="0x25" name="percent"/><!-- PERCENT SIGN -->
      <map code="0x2b" name="plus"/><!-- PLUS SIGN -->
      <map code="0x2c" name="comma"/><!-- COMMA -->
      <map code="0x2d" name="hyphen"/><!-- HYPHEN-MINUS -->
      <map code="0x2e" name="period"/><!-- FULL STOP -->
      <map code="0x30" name="zero"/><!-- DIGIT ZERO -->
      <map code="0x31" name="one"/><!-- DIGIT ONE -->
      <map code="0x32" name="two"/><!-- DIGIT TWO -->
      <map code="0x33" name="three"/><!-- DIGIT THREE -->
      <map code="0x34" name="four"/><!-- DIGIT FOUR -->
      <map code="0x35" name="five"/><!-- DIGIT FIVE -->
      <map code="0x36" name="six"/><!-- DIGIT SIX -->
      <map code="0x37" name="seven"/><!-- DIGIT SEVEN -->
      <map code="0x38" name="eight"/><!-- DIGIT EIGHT -->
      <map code="0x39" name="nine"/><!-- DIGIT NINE -->
      <map code="0xa0" name="space"/><!-- NO-BREAK SPACE -->
      <map code="0xa5" name="yen"/><!-- YEN SIGN -->
      <map code="0x2212" name="minus"/><!-- MINUS SIGN -->
      <map code="0x4e07" name="uni4E07"/><!-- CJK UNIFIED IDEOGRAPH-4E07 -->
      <map code="0x4ebf" name="uni4EBF"/><!-- CJK UNIFIED IDEOGRAPH-4EBF -->
      <map code="0x5143" name="uni5143"/><!-- CJK UNIFIED IDEOGRAPH-5143 -->
      <map code="0x5206" name="uni5206"/><!-- CJK UNIFIED IDEOGRAPH-5206 -->
    </cmap_format_4>
  </cmap>'''  # 替换为你的完整 XML 内容

root = ET.fromstring(xml_content)

# 提取映射
char_to_name = {}
for cmap in root.findall('.//cmap_format_4'):
    for mapping in cmap.findall('map'):
        code = mapping.get('code')
        name = mapping.get('name')
        char_to_name[code] = name

print(char_to_name)


