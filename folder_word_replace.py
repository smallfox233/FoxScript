import argparse
import sys
from threading import Thread #线程加速
import os

def get_file_name(folder,ext):
    '''
    读取文件夹内所有指定后缀文件路径（包括子目录）
    :param folder: str，文件夹绝对路径
    :param ext: str,文件后缀
    :return: list,文件绝对路径列表
    '''
    if ext[0]==".": #去小数点
        ext = ext.replace(".","")
    name_lis = []
    ext = "."+ext
    for root,dirs,files in os.walk(folder):
        # print(root,dirs,files)
        for file in files:
            if file[-len(ext):] == ext: #判断后缀
                name_lis.append(root + "\\"+file)
    # print(len(name_lis))
    return name_lis
# print(get_file_name("D:\\","zip"))

def word_replace(file,word,target):
    data = ""
    #读文件
    with open(file,"r",encoding="utf-8") as f:
        for line in f: #逐行读取
            if word in line: #替换关键字
                line = line.replace(word,target)
            data += line
    #写文件
    with open(file,"w",encoding="utf-8") as f:
        f.write(data)
# word_replace("D:\\1.txt","./","../")

if __name__ == '__main__':
    arg = argparse.ArgumentParser(description="功能：递归替换文件夹下指定后缀文件的指定字符串")
    arg.add_argument('-fol','--folder', help="文件夹路径\n")
    arg.add_argument('-w', '--word', help="需替换的字符串\n")
    arg.add_argument('-t', '--target', help="替换后的字符串\n")
    arg.add_argument('-ext', '--ext', help="指定需要替换的文件后缀\n")
    args = arg.parse_args()
    if len(sys.argv) == 1:  # 未传入参数时
        arg.print_help()  # 打印帮助信息
        sys.exit()
    folder = str(args.folder)
    word = str(args.word)
    target = str(args.target)
    ext = str(args.ext)
    # 检测文件夹是否存在
    if os.path.exists(folder)==False:
        print("文件夹不存在!")
        sys.exit()
    name_lis = []

    name_lis = get_file_name(folder,ext)
    for i in name_lis:
        # 线程
        t = Thread(target=word_replace, args=[i,word,target])
        t.start()
        t.join()
        # word_replace(i,word,target)
    print("替换完成")
