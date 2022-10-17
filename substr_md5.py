# 作者：小狐狸FM
# 作用：MD5子串爆破，停止程序时将会保存一个临时文件用于下一次继续爆破
# PHP函数介绍：https://www.php.net/manual/zh/function.substr.php
# substr(主串，offset，length)
# offset为匹配的初始位置
# length为匹配的长度

import hashlib
import string
import random
import sys

# 随机数种子
random.seed()
# 字符集,大小写字母+数字
char = string.ascii_letters + string.digits
# 需要匹配的子串内容
sub_str = "8b184b"
# 明文长度
m_len = 8
# 已爆破过的明文
m_lis = []
# 已爆破过的明文存放路径
m_pth = sub_str + ".txt"
# 需要匹配的子串初始位置，0表示第一个字符，-1表示最后一个字符
sub_start = 6
# 需要匹配的子串长度
sub_len = 6
# 需要匹配的子串结束位置
sub_end = sub_start + sub_len
if sub_start >= m_len: #初始位置超过主串长度时
    print("md5_len必须大于sub_start!!")
    sys.exit()
if sub_end< 0 : #子串长度负数
    print("sub_end不能为负数!!")
    sys.exit()
with open(m_pth,"a+") as fp:
    m_lis = fp.read().split("\n")
    while True: #死循环
        # 明文
        m = ''.join(random.choice(char) for i in range(m_len))
        # 密文,32位md5
        c = hashlib.md5(m.encode())
        if m not in m_lis and m[sub_start:sub_end:sub_len]==sub_str: #未生成过的明文，且成功获取内容时
            print("解密成功！")
            print("明文:",m)
            print("密文:",c)
            break
        else:
            fp.write(m + "\n")