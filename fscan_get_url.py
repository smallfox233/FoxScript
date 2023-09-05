# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：提取fscan结果中的URL信息
import re
import sys
import argparse
def get_url(data):
    if "*" not in data or "WebTitle" not in data:
        return False
    result = ""
    result = data.split(" ")[2]
    return result
def open_url(file="result.txt",output="url.txt"):
    result = ""
    lis =[]
    tmp = []
    # 读取
    with open(file,"r",encoding="utf-8") as fp:
        tmp = fp.read().split("\n")
    for line in tmp:
        x = get_url(line)
        if x==False:
            continue
        lis.append(get_url(line))
    # 去重
    lis = list(set(lis))
    # 排序
    lis = sorted(lis)
    result = "\n".join(lis)
    # 写入
    with open(output,"w",encoding="utf-8") as fp:
        fp.write(result)

if __name__ == '__main__':
    # 参数获取
    arg = argparse.ArgumentParser(description="功能：提取fscan扫描结果的url信息")
    arg.add_argument('-f','--file',help="fscan扫描结果路径\n")
    arg.add_argument('-o','--output',help="导入的url文件路径\n")
    args = arg.parse_args()
    if len(sys.argv) == 1: #未传参时
        arg.print_help()
        sys.exit()
    file = str(args.file)
    output = str(args.output)
    open_url(file,output)