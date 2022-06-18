# bash命令base64编码转换
import base64

command = input("命令: ")
command = base64.b64encode(command.encode("utf-8"))  # base64编码
command = command.decode()  # 将bytes转换为string
command = "bash -c {echo," + command + "}|{base64,-d}|{bash,-i}"  # 转换命令的格式
print(command)
