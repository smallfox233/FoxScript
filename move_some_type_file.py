# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：将文件夹下的指定后缀文件（包括其子文件夹），统一复制到另一文件夹内
import os,re

# 定义
file_path = []
result_path = []
# 输入
origin_dir = input("源文件夹路径：")
file_type = input("需复制文件后缀（不包括点）：")
target_dir = input("目标文件夹路径：")
# 创建文件夹
if os.path.exists(target_dir)==False:
    os.mkdir(target_dir)
# 输入数据处理
if "." in file_type:
    file_type = file_type.replace(".","") #置空
# 获取名称
for root,dirs,files in os.walk(origin_dir): #获取该文件夹下的所有信息
    for i in files:
        # 筛选
        if "."+file_type not in i or "." not in i: #不符合条件时
            continue
        file_path.append((root+"\\"+i,i)) #元组：(路径，文件名)
# print(file_path)
#正则筛选
for tuple in file_path:
    match = re.search("\."+file_type+"$",tuple[1]) #匹配文件名
    if match:
        result_path.append(tuple)
#复制文件
# [print(i) for i in result_path]
for tuple in result_path: #遍历所有文件路径
    data = ""
    with open(tuple[0],"r",encoding="utf-8") as fp: #根据路径读取文件内容
        data = fp.read()
    with open(target_dir + "/" + tuple[1],"w",encoding="utf-8") as fp: #写入文件
        fp.write(data)
print("执行结束..")
