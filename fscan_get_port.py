# 作者: 小狐狸FM
# 版本: 2022.07.03
# 功能：提取fscan结果中各个IP开放的端口，显示并以IP为文件名写入对应的开放端口
# 提示：只需要输入含有IP:端口 open的那些字符串
import os

def get_host_port(str):
    '''
    获取字符串中的IP和端口信息
    例如处理192.168.123.11:3306 open
    返回192.168.123.11和3306两个字符串
    '''
    if "open" in str:
        # 置空
        str = str.replace("open", "")
        str = str.replace(" ", "")
        # 数值获取
        ip, port = str.split(":")
        return ip, port
# print(get_host_port("192.168.123.11:3306 open")[0])

def create_file_folder(result_file_folder):
    '''检测文件夹是否存在，不存在则创建'''
    if os.path.exists(result_file_folder):  # 存在时
        return
    else:  # 不存在时
        os.mkdir(result_file_folder)
# create_file_folder("test")

if __name__ == '__main__':  # 主函数
    # 参数
    fscan_pth = "data/fscan.txt"  # 读取的文件路径
    fscan_lis = [] #列表
    result_dic = {} #字典
    result_file_folder = "data"  # 保存各IP结果的文件夹路径
    create_file_folder(result_file_folder)
    # 读取
    with open(fscan_pth, "r", encoding="utf-8") as fp:
        fscan_lis = fp.read().split("\n")
    # print(fscan_lis)
    # 处理
    if result_file_folder[::-1] != '/':  # 末尾不为/时
        result_file_folder += '/'
    # print(result_file_folder)
    for i in fscan_lis:  # 初始化字典result_dic
        if 'open' in i:  # 含有指定字符串时
            result_dic[get_host_port(i)[0]] = []
    # print(result_dic)
    for i in fscan_lis: #添加端口信息
        if 'open' in i: #含有指定字符串时
            result_dic[get_host_port(i)[0]].append(get_host_port(i)[1])
    # print(result_dic)
    # 显示
    for host,port in result_dic.items(): #遍历键值对
        #输出IP
        print(host)
        #类型转换
        for i in range(len(port)):
            port[i] = int(port[i])
        #端口排序
        port = sorted(port)
        #类型转换
        for i in range(len(port)):
            port[i] = str(port[i])
        #输出端口
        print("\n".join(port))
        print()
    # 写入
    for host, port in result_dic.items():  # 遍历键值对
        # 类型转换
        for i in range(len(port)):
            port[i] = int(port[i])
        # 端口排序
        port = sorted(port)
        # 类型转换
        for i in range(len(port)):
            port[i] = str(port[i])
        # 创建文件并写入内容
        with open(result_file_folder + host,"w") as fp:
            fp.write('\n'.join(port))
