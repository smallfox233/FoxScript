# coding=utf-8
# 作者：小狐狸FM
# 仓库：https://github.com/smallfox233/FoxScript
# 功能：GET请求，检测状态码
import requests

# 文本路径
pth = "url.txt"
# 检测成功时，URL的文本存储路径
new_pth = "new.txt"
# 连接超时时长,秒
time = 3
# 匹配的状态码，符合时才会将url写入文件
state = ['200','302','403']
# 需要添加到url末尾的路径，可用于IP不同，路径相同的情况
add_right = ""
# 需要添加到url开头的路径，可用于IP相同，路径不同的情况
add_left = ""
# 字符串
s1 = ""
s2 = ""
# 文件读取
with open(pth, "r") as fp:
    s1 = fp.read()
lis = list(s1.split("\n"))
# print(lis)
# 遍历
for url in lis:
    now_url = add_left + url + add_right
    try:
        r = requests.get(now_url, timeout=time)
        if str(r.status_code) in state:
            s2 += now_url + "\n"
            print("成功：",now_url)
        else:
            print("失败：",now_url)
    except:
        print("失败：",now_url)
        continue
# 文件写入
with open(new_pth, "w") as fp:
    fp.write(s2)
print("结果输出至文件: ",new_pth)
