# coding=utf-8
# 作者：小狐狸FM
# 检测状态码
import requests

#文本路径
pth = "url.txt"
new_pth = "new.txt"
#连接超时时长,秒
time = 3
#匹配的状态码，符合时才会将url写入文件
state = 200
#需要添加到url末尾的路径
add = ""
#字符串
s1 = ""
s2 = ""
#文件读取
with open(pth,"r") as fp:
    s1 = fp.read()
lis = list(s1.split("\n"))
#遍历
for url in lis:
    try:
        r = requests.get(url,timeout=time)
        if r.status_code == state:
            s2 += url + add + "\n"
            print(url)
    except:
        continue
#文件写入
with open(new_pth,"w") as fp:
    fp.write(s2)


