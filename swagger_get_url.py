# 作者：小狐狸FM
# 项目：https://github.com/smallfox233/FoxScript
# 功能：提取swagger v2/docs中的路径信息
import argparse
import sys
import json
def swagger_get_url(result_filename="path.txt",filename="api-docs.json"):
    # 变量处理
    if filename == "None":
        filename = "api-docs.json"
    if result_filename =="None":
        result_filename = "path.txt"
    # 临时
    tmp = ""
    result = ""
    # 文件读取
    with open(filename,"r",encoding='utf-8') as fp:
        tmp = fp.read()
    # print(tmp)
    # 导入
    tmp = json.loads(tmp)
    # print(tmp)
    # 数据处理
    for key,value in tmp.items():
        if key=='paths':
            # print(tmp[key])
            for url,j in value.items():
                # print(url)
                result += str(url) + "\n"
    # 写入
    with open(result_filename,"w") as fp:
        fp.write(result)
if __name__ == '__main__': #主函数
    arg = argparse.ArgumentParser(description="功能：提取swagger v2/docs中的路径信息")
    arg.add_argument('-f', '--file', help="api-docs文件路径（默认api-docs.json）\n")
    arg.add_argument('-o', '--output', help="输出文件路径（默认path.txt）\n")
    args = arg.parse_args()
    if len(sys.argv) == 1:  # 未传入参数时
        arg.print_help()  # 打印帮助信息
        sys.exit()
    d = swagger_get_url(filename=str(args.file),result_filename=str(args.output))
