import xml.etree.ElementTree as ET
import os

tree = ET.ElementTree(file='test.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)

# 修改某些结点的值
for price in root.iter('price'):
    # 原本是这样的 <price updated="up">49.95</price>
    new_price = float(price.text) + 10
    price.text = str(new_price)
    # 改变属性
    price.set("update", "up")
# 删除某个结点：
del root[1]
outpath = os.getcwd()
file = outpath + 'test.xml'
# 写如文件
tree.write(file)
