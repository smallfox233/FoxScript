# 作者：小狐狸FM
# 功能：过滤nmap扫描结果，正则匹配获取开放端口
import re
file_pth = "data/nmap.txt" #读取的文件路径
result_pth = "data/result.txt" #写入的文件路径
nmap_lis = []
result_lis = []
pattern = "\d{1,6}/" #正则表达式，端口/协议
#读取
with open(file_pth,"r") as fp:
    nmap_lis = list(fp.read().split("\n"))
# print(nmap_lis)
#处理
for i in nmap_lis:
    if "open" in i:
        result_lis.append(re.findall(pattern,i)[0].replace("/",""))
#转换
for i in range(len(result_lis)): #转换为int
    result_lis[i] = int(result_lis[i])
#排序
result_lis = sorted(result_lis)
#转换
for i in range(len(result_lis)): #转换为str
    result_lis[i] = str(result_lis[i])
#写入
with open(result_pth,"w") as fp:
    fp.write("\n".join(result_lis))
