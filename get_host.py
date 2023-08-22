# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：URL批量处理，删除协议头和端口等无关信息
import argparse
import sys
class delete:
    def __init__(self,file,target="new.txt"):
        self.lis_protocol = ["https", "http", "ftp"]  # 协议头，https需要放在http之前
        self.txt_path = file #URL存放的位置
        self.txt_new_path = target #提取IP后存放的位置
        self.lis_url = []
        # 处理
        with open(f"{self.txt_path}", "r", encoding="utf-8") as fp:  # 文件读取
            lis_url = list(fp.read().split("\n"))
        with open(f"{self.txt_new_path}", "w") as fp:  # 文件写入
            for i in lis_url:  # 遍历
                if i != "" and i != "\n":  # 不为空时
                    fp.write(self.DelOther(self.DelPort(self.DelProtocol(self.Format(str(i))))) + "\n")

    def DelPort(self,url):
        '''删除URL中的端口，需要先删除协议头中的冒号'''
        if ":" in url:
            return url[:url.index(":"):]  # 左闭右开，删除":端口"信息
        return url
    # print(DelPort("127.0.0.1:8080"))

    def DelProtocol(self,url):
        '''删除字符串中协议头'''
        for i in self.lis_protocol:
            if i in url:
                return (url.replace(i,"")).replace("://","")  # 左闭右开，删除"协议"和"://"
        return url
    # print(DelProtocol("https://www.baidu.com"))

    def DelOther(self,url):
        '''删除字符串之后的参数，保留IP\n需要提前删除端口和协议头'''
        if "/" in url:
            return url[:url.index("/"):] # 左闭右开，保留左侧IP
        elif "\\" in url:
            return url[:url.index("\\"):]
        return url
# print(DelOther("127.0.0.1/path/?upload=1.php"))
# print(DelOther("127.0.0.1\path\?upload=1.php"))

    def Format(self,url):
        '''将右斜杠格式化为左斜杠'''
        return url.replace("\\","/")
    # print(Format(r"http:\\www.baidu.com"))

if __name__ == '__main__': #主函数
    arg = argparse.ArgumentParser(description="功能：URL批量处理，删除协议头和端口等无关信息")
    arg.add_argument('-f', '--file', help="url文件路径（默认url.txt）\n")
    arg.add_argument('-o', '--output', help="输出文件路径（默认new.txt）\n")
    args = arg.parse_args()
    file = "url.txt"
    output = "new.txt"
    if len(sys.argv) == 1:  # 未传入参数时
        arg.print_help()  # 打印帮助信息
        sys.exit()
    if args.file != None:
        file = str(args.file)
    if args.output != None:
        output = str(args.output)
    d = delete(file=file,target=output)

