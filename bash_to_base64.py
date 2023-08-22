# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：bash命令base64编码转换
import base64
import argparse
import sys
def bash_to_base64(command):
    command = base64.b64encode(command.encode("utf-8"))  # base64编码
    command = command.decode()  # 将bytes转换为string
    command = "bash -c {echo," + command + "}|{base64,-d}|{bash,-i}"  # 转换命令的格式
    return command
if __name__ == '__main__':
    # 参数获取
    arg = argparse.ArgumentParser(description="功能：将bash命令base64编码转换输出")
    arg.add_argument('-c', '--command', help="传入的命令\n")
    args = arg.parse_args()
    if len(sys.argv) == 1:  # 未传入参数时
        arg.print_help()  # 打印帮助信息
        sys.exit()
    command = str(args.command)
    # 功能
    print(bash_to_base64(command))
