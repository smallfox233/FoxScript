# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：提取minio xml文件路径，拼接文件URL
import argparse
import sys
    
def minio_get_url(url,result_filename="url.txt",filename="download.xml"):
    # 变量处理
    if url == "None":
        url = "http://127.0.0.1/minio"
    if filename == "None":
        filename = "download.xml"
    if result_filename =="None":
        result_filename = "url.txt"
    if url[:-1]!="/":
        url += "/"
    # 变量
    tmp = ""
    lis = []
    # 读取
    with open(filename,"r",encoding="utf-8") as fp:
        tmp = fp.read().split("<Key>")
        
        
    # print(tmp)
    for i in range(1,len(tmp)):
        # print(tmp[i])
        tmp2 = tmp[i].split("</Key>")[0]
        # print(tmp2)
        lis.append(url + tmp2)
    # result = url.join(lis)
    # print(result)
    
    # 写入
    with open(result_filename,"w") as fp:
        fp.write('\n'.join(lis))

if __name__ == '__main__': #主函数
    arg = argparse.ArgumentParser(description="功能：提取minio xml文件路径，拼接文件URL")
    arg.add_argument('-u', '--url', help="URL根路径（默认http://127.0.0.1/minio/），例：http://xxxx/minio/\n")
    arg.add_argument('-f', '--file', help="xml文件路径（默认download.xml）\n")
    arg.add_argument('-o', '--output', help="输出文件路径（默认url.txt）\n")
    args = arg.parse_args()
    if len(sys.argv) == 1:  # 未传入参数时
        arg.print_help()  # 打印帮助信息
        sys.exit()
    minio_get_url(url=str(args.url),filename=str(args.file),result_filename=str(args.output))