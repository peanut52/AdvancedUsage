import zipfile

"""
向zip文件中写入python文件
本例中向pickle_module.zip中写入test.py，前提是test.py文件必须有，自动创建pickle_module.zip
"""
my_zip = zipfile.ZipFile('pickle_module.zip', 'w')

my_zip.write('test.py')
my_zip.close()
