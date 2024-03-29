# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：提取fscan结果中的IP，递增排序显示IP，并写入文件

import re
import sys
import argparse

if __name__ == '__main__':  # 主函数
    fscan_pth = input("fscan结果文件路径：")  # 读取的文件路径
    result_pth = input("输出文件路径：")  # 写入的文件路径
    fscan_lis = []
    result_lis = []
    pattern = "\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"  # 正则表达式，IP地址
    # 读取
    with open(fscan_pth, "r", encoding="utf-8") as fp:
        fscan_lis = fp.read().split("\n")
    # print(fscan_lis)
    # 处理
    for i in fscan_lis:
        if "alive" in i and "keep-alive" not in i:
            try:
                result_lis.append(re.findall(pattern, i)[0])
            except:
                continue
    # 排序
    result_lis = sorted(result_lis,key = lambda x:int(x.split(".")[-1])) #根据IP的最后一位的数值大小递增排序
    # 显示
    for i in result_lis:
        print(i)
    # 写入
    with open(result_pth,"w") as fp:
        fp.write("\n".join(result_lis))
