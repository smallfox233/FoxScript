# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：MD5子串爆破，停止程序时将会保存一个临时文件

# PHP函数介绍：https://www.php.net/manual/zh/function.substr.php
# substr(主串，offset，length)
# offset为匹配的初始位置
# length为匹配的长度

import hashlib
import os
import string
import random
import sys

# 随机数种子
random.seed()
# 字符集,大小写字母+数字
char = string.ascii_letters + string.digits
# 需要匹配的子串内容(必须)
sub_str = input("需要匹配的子串: ") # 例：8b184b
# 明文长度
m_len = random.randint(1,20)
# 已爆破过的明文
m_lis = []
# 已爆破过的明文存放路径
m_pth = sub_str + ".txt"
# 需要匹配的子串初始位置(必须)，0表示第一个字符，-1表示最后一个字符
sub_start = -6
# 需要匹配的子串长度(必须)
sub_len = 6
# 需要匹配的子串结束位置
sub_end = sub_start + sub_len
if sub_start >= m_len:  # 初始位置超过主串长度时
    print("md5_len必须大于sub_start!!")
    sys.exit()
if sub_len < 0:  # 子串长度负数
    print("sub_end不能为负数!!")
    sys.exit()
if sub_end == 0: #子串结束位置为0时
    sub_end = 32
# 随机生成新MD5
with open(m_pth, "a+") as fp:
    while True:  # 死循环
        # 明文
        m = ''.join(random.choice(char) for i in range(m_len))
        # 密文,32位md5
        c = str(hashlib.md5(m.encode()).hexdigest())
        if c[sub_start:sub_end:] == sub_str:  # 未生成过的明文，且成功获取内容时
            print("解密成功！")
            print("明文:", m)
            print("密文:", c)
            sys.exit()
        if m not in m_lis:
            fp.write(m + "$" + str(c) + "\n")

