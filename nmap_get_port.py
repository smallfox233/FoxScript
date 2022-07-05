# 作者：小狐狸FM
# 功能：过滤nmap扫描结果，获取开放端口
file_pth = "data/nmap.txt" #读取的文件路径
result_pth = "data/result.txt" #写入的文件路径
nmap_lis = []
result_lis = []
#读取
with open(file_pth,"r") as fp:
    nmap_lis = list(fp.read().split("\n"))
# print(nmap_lis)
#显示
for i in nmap_lis:
    if "open" in i:
        result_lis.append(i.split("/")[0])
#写入
with open(result_pth,"w") as fp:
    fp.write("\n".join(result_lis))