import tarfile

"""
创建tar包，未压缩
"""
with tarfile.open('etc.tar', mode='w') as f:
    f.add('test.py')

"""
读取gzip算法压缩的tar包
"""
with tarfile.open('etc.tar', mode='r:gz') as f:
    pass
"""
写入一个bzip2算法压缩的tar包
"""
with tarfile.open('etc.tar', mode='w:bz2') as f:
    pass
# with tarfile.open('etc.tar') as t:
#     for member in t.getmembers():
#         print(member.name)
