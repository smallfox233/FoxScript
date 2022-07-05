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
#显示
for i in nmap_lis:
    if "open" in i:
        result_lis.append(re.findall(pattern,i)[0].replace("/",""))
#写入
with open(result_pth,"w") as fp:
    fp.write("\n".join(result_lis))
