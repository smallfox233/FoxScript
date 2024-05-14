# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：连接smtp发送消息
# 依赖库：pip install sender
from sender import Mail

# 定义
smtp_server = "xxx" # smtp服务器
smtp_port = 25  # smtp服务器端口
smtp_user = "xxx" # smtp账号
smtp_pass = "xxx" # smtp密码
mail_name = "xxx" # smtp邮箱昵称
smtp_protocol = "http" # 协议，默认为http
mail_target = "xxx@qq.com" # 目标邮箱
mail_title = "xxxx" # 邮件标题
mail_body = "xxx" # 邮件正文


is_ssl = False
if smtp_protocol == "https":
    is_ssl = True

# 实例化
mail = Mail(smtp_server, port=smtp_port, username=smtp_user, password=smtp_pass,
            use_tls=is_ssl, use_ssl=is_ssl, debug_level=None)
# 来源邮箱
mail.fromaddr = (mail_name, smtp_user)

mail.send_message(mail_title, to=mail_target, body=mail_body)