# 作者：小狐狸FM
# 功能：URL批量处理，删除协议头和端口等无关信息

lis_protocol = ["https", "http", "ftp"]  # 协议头，https需要放在http之前
txt_path = "test.txt" #URL存放的位置
txt_new_path = "new.txt" #提取IP后存放的位置
lis_url = []

def DelPort(url):
    '''删除URL中的端口，需要先删除协议头中的冒号'''
    if ":" in url:
        return url[:url.index(":"):]  # 左闭右开，删除":端口"信息
    return url
# print(DelPort("127.0.0.1:8080"))

def DelProtocol(url):
    '''删除字符串中协议头'''
    for i in lis_protocol:
        if i in url:
            return (url.replace(i,"")).replace("://","")  # 左闭右开，删除"协议"和"://"
    return url
# print(DelProtocol("https://www.baidu.com"))

def DelOther(url):
    '''删除字符串之后的参数，保留IP\n需要提前删除端口和协议头'''
    if "/" in url:
        return url[:url.index("/"):] # 左闭右开，保留左侧IP
    elif "\\" in url:
        return url[:url.index("\\"):]
    return url
# print(DelOther("127.0.0.1/path/?upload=1.php"))
# print(DelOther("127.0.0.1\path\?upload=1.php"))

def Format(url):
    '''将右斜杠格式化为左斜杠'''
    return url.replace("\\","/")
# print(Format(r"http:\\www.baidu.com"))

if __name__ == '__main__': #主函数
    with open(f"{txt_path}","r") as fp: #文件读取
        lis_url = list(fp.read().split("\n"))
    with open(f"{txt_new_path}","w") as fp: #文件写入
        for i in lis_url: #遍历
            if i!="" and i!="\n": #不为空时
                fp.write(DelOther(DelPort(DelProtocol(Format(str(i))))) + "\n")
