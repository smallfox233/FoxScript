# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：提取swagger v2/docs中的路径信息
import json
# 自定义参数
result_filename = "path.txt"
filename = input("api-docs.json文件路径：") #目标文件
# 临时
tmp = ""
result = ""
# 文件读取
with open(filename,"r",encoding='utf-8') as fp:
    tmp = fp.read()
# print(tmp)
# 导入
tmp = json.loads(tmp)
# print(tmp)
# 数据处理
for key,value in tmp.items():
    if key=='paths':
        # print(tmp[key])
        for url,j in value.items():
            # print(url)
            result += str(url) + "\n"
# 写入
with open(result_filename,"w") as fp:
    fp.write(result)
