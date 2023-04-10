# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：过滤nmap扫描结果，获取存活IP

file_pth = input("nmap结果文件路径：") #读取的文件路径
result_pth = input("输出文件路径: ") #写入的文件路径
nmap_lis = []
result_lis = []
#读取
with open(file_pth,"r") as fp:
    nmap_lis = list(fp.read().split("\n"))
# print(nmap_lis)
#显示
for i in nmap_lis:
    if "Nmap scan report for" in i:
        print(i.replace("Nmap scan report for",""))
        result_lis.append(i.replace("Nmap scan report for",""))
#写入
with open(result_pth,"w") as fp:
    fp.write("\n".join(result_lis))
