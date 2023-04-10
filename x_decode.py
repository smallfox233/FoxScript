# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：对\x开头数据进行解码
from urllib import parse

t = input("输入数据：")
t = t.encode('unicode_escape')
# print(t)
t = t.decode('utf-8').replace('\\x','%')
t = parse.unquote(t)
print("解码结果：",t)