"""
将txt格式保存为md格式
txt格式为：
ppp:    aaa

md格式：
遇i个空行则转换为#*(5-i) ；
<span name="{i.j.k}"></span>\n
ppp [ans](#ans_i.j.k)\n
(51个字节,)

文件尾
<span name="ans_{i.j.k}"></span>\n
aaa [back](#i.j.k)\n

需要同时对文件的两个点做延展 -- 分两个线程
动态延展：难以实现
预先把偏移指针移到足够大的位置。
p内容相对较小。
考虑一个p，10个汉字,utf8 30+51=81字节～90字节
预设5k个p
P_TO_ANS:45000

实现方式：
    单进程能处理：
    每次读一行，分离出p和ans。
    写入p，记录p_point，移动到ans_point,写入ans，记录ans_point，移动回p_point
    无阻塞 读n次

!   多进程：进程之间不共用偏移量指针
    - 主进程：
        读n次，匹配并且读出p，写入p
    - 子进程：
        读n次，匹配并且读出ans，写入ans

    多线程：共用读和写偏移量指针
    各读取n次太过繁琐。

    另：
        一次将txt文本内容全部读出，然后用正则表达式匹配出p和ans的列表
        除了初始化p_point和ans_point，不用再操作偏移量

    一次将空行之间的所有文本内容读出，然后用正则表达式匹配。
    能够对范围内的内容排序
    得到text，

    //count=0，1,2,3,4,5
    //每次读取一行，读到一个空行则count++，直到读到非空行，

    记录fir，sec，thr，forth=0
    每次读取一行，读到空行后，下一行内容为#num title
    num=1   fir++，  \n*3#×num fir title
    num=2   sec++，  \n#×num fir.sec title



主线程中读出一行p和ans，
提取出ans,
主程序和线程都要使用偏移量指针 --- 上锁
多进程，多偏移量，多线程共享偏移量

写入md文件
因为p和ans距离远，不考率偏移量重叠的情况

### 如果在不同进程中打开相同文件，同时操作 ###
"""
import os
import re
import sys
from multiprocessing import Process

P_TO_ANS = 22000
NOTEPATH = "note/origin/"
MARKDOWNPATH="note/md/"


point = 0

# 打开笔记 over
def openNote(notename):
    # notename = input("笔记名：")  # 将笔记文件复制到响应文件夹下
    dir = NOTEPATH + notename
    # 打开笔记
    try:
        note = open(dir, "r",encoding="utf8")
    except Exception as e:
        print("无此笔记")
        sys.exit()
    # return note, notename
    return note


# 创建md文件 over
def createMD(notename):
    # 创建md文档
    filename = re.sub(r"\.\w*", ".md", notename)
    fileDir = MARKDOWNPATH + filename
    file = open(fileDir, "wb")
    # print(filename)

    return file


# 对文档中的\n进行转义
def wrap(content):
    # 转义\n
    pattern="\\\\n"
    # print(re.split(pattern,content))
    return re.sub(pattern,"\n",content)

# 生成跳转体
def getAttach(isP):
    if isP:  # pro
        attach = "{0}   [ans](#{1})<a name='{2}'></a>\n\n"
    else:  # ans
        attach = "<a name='{1}'></a>\n{0}   [back](#{2})\n\n"
    return attach

# 生成标题格式
def writeTitle(title):
    md = ""
    global point
    if point == 0:
        # txt 格式 空行# 表示上一个板块的标题
        md += f"\n# PRO\n[toc]\n\n---\n{title}"
        # print(md)
        point+=1
    elif point == P_TO_ANS:
        md += f"\n===\n---\n# ANS\n\n---\n{title}"
        point+=1
    else:
        md += f"\n\n\n---\n{title}\n"
    return md


# 在线程中向md文档写入ans
def writeFile(file, content, title, isP):
    # data为写入的内容列表
    global point
    data = getData(content, isP)
    try:
        name = str(title).split(" ")[2]  # 获得板块名
    except IndexError:
        print(f"title '{title}' wrong")
        sys.exit()
    count = 1
    # 生成跳转体
    attach=getAttach(isP)
    # 生成标题
    md=writeTitle(title)
    file.write(md.encode())

    # isP:data[xxx,{{xxx}},xxx:]
    # ans:data[xxx,{{}},]
    for i in data:
        textname_p = name[0:-1] + str(count)
        textname_ans = "ans_" + name[0:-1] + str(count)
        count += 1
        # print(i)
        # 转义'\n'
        i=wrap(i)
        # 构造输出字符串
        m=attach.format(i, textname_ans, textname_p)
        # 判断是否为{{}}
        if i.startswith("{{") and i.endswith(("}}")):
            if isP:
                m="**"+i[2:-2]+"**\n\n"
            else:
                continue
        # 处理- > 等特殊格式
        # if i.startswith("   ")or i.startswith("- ") or i.startswith("> ")\
        #         or i.startswith("* ") or i.startswith("+ "):
        #     m+="\n"
        file.write(m.encode())
        print(f"isP:{isP}   in {file.tell()}")


# 读取笔记，isP为1，则读取p，为0，则读取ans
def readNote(note):
    # 空行之间的内容
    content = []
    flag = 1
    # print(note.tell())
    while True:
        # data=xxx:  xxx\n
        # data={{xxx}}\n
        # data=xxx:\n
        data = note.readline()
        # 读到文件末尾：
        if not data:
            # return content, data
            return None, None
        # 读取到空行则开始统计，flag设为0，content关闭统计
        if data == '\n':
            flag = 0
            continue  # 读取#
        # 没有遇到空行，则往content内添加数据
        if flag:
            content.append(data)
        else:
            # data 为带有#号的本板块信息
            return content, data


def getData(content, isP):
    pattern = "[:：]\s+"
    res = []
    for i in content:
        # i=xxx:  xxx\n
        # i={{xxx}}\n
        # i=xxx:\n
        line = re.split(pattern, i, 1)
        p=line[0]
        # print(os.getpid(),line)
        if isP:
            res.append(p.split("\n")[0])
        else:
            if len(line)==1:
                if p.startswith("{{") and p.endswith("}}\n"):
                    res.append("{{}}")
                    continue
                res.append("暂无资料")
            else:
                res.append(line[1].split("\n")[0])
    # print(res)
    # isP:res[xxx,{{xxx}},xxx:]
    # ans:res[xxx,{{\n}},]
    return res


# 文本写入，isP为1，则写入p，为0，则写入ans,
def transform(isP,file,notename):
    note=openNote(notename)
    # 如果写入p
    global point
    if isP == 1:
        # 暂不考虑添加笔记的情况
        file.seek(0)
        point = 0
    elif isP == 0:
        file.seek(P_TO_ANS)
        point = P_TO_ANS

    while True:
        # 读取数据
        content, title = readNote(note)
        # print(content)
        # if not isP:
        #     print(content)
        if not title:
            # if not isP:
            #     print("flush")
            # print("file close")
            file.close()
            note.close()
            return
        writeFile(file, content, title, isP)


# over
def main():
    # 主进程 --p
    # 子进程 --ans

    # 打开txt笔记，获取file对象和笔记名
    # note, notename = openNote()
    # 打开md笔记
    # file = createMD(notename)
    # 建立子进程，处理ans
    notename = input("笔记名：")
    file = createMD(notename)
    # 不能使用多进程
    # p = Process(target=transform, args=(0,file,notename))
    # p.start()

    # 主进程处理p
    transform(1,file,notename)
    transform(0,file,notename)
    # print(point)
    print("转换成功")


if __name__ == "__main__":
    main()
