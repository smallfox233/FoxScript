import argparse
import sys
import execjs #第三方库

def js_func(file_dic,file_js,func,output):
    #定义
    js = ""
    dic = ""
    #读取js
    with open(file_js,"r",encoding="utf-8") as fp:
        js = fp.read()
    #读取字典
    with open(file_dic,"r",encoding="utf-8") as fp:
        dic = fp.read().split("\n")
    #调用js
    test = execjs.compile(js)
    for i in range(len(dic)):
        dic[i] = test.call(func,dic[i])
    #写入字典
    with open(output,"w",encoding="utf-8") as fp:
        fp.write('\n'.join(dic))

if __name__ == '__main__':
    arg = argparse.ArgumentParser(description="功能：调用js函数，加密指定字典信息")
    arg.add_argument('-js', '--js', help="js文件路径\n")
    arg.add_argument('-dict', '--dict', help="字典文件路径\n")
    arg.add_argument('-output', '--output', help="新的字典文件路径\n")
    arg.add_argument('-func', '--function', help="js函数名称\n")
    args = arg.parse_args()
    if len(sys.argv) == 1:  # 未传入参数时
        arg.print_help()  # 打印帮助信息
        sys.exit()
    file_dic = str(args.dict)
    file_js = str(args.js)
    func = str(args.function)
    output = str(args.output)
    js_func(file_dic,file_js,func,output)