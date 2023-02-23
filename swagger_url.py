# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：提取swagger v2/docs中的路径信息
import json
tmp = ""
result = ""
filename = input("xxx.json") #目标文件
with open(filename,"r",encoding='utf-8') as fp:
    tmp = fp.read()
# print(tmp)
tmp = json.loads(tmp)
# print(tmp)
for key,value in tmp.items():
    if key=='paths':
        # print(tmp[key])
        for url,j in value.items():
            print(url)
