import hashlib
m = hashlib.md5()
m.update(b'123')
print(m.hexdigest())
'202cb962ac59075b964b07152d234b70'

# 或者可以这样
print(hashlib.md5(b'123').hexdigest())
'202cb962ac59075b964b07152d234b70'

# 也可以使用hash.new()这个一般方法
print(hashlib.new('md5', b'123').hexdigest())
'202cb962ac59075b964b07152d234b70'