import re
from langconv import Converter


def find_chinese(a):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', a)
    return chinese


def convert(text, flag=1):  # 默认1,表示繁转简
    rule = 'zh-hans' if flag else 'zh-hant'
    return Converter(rule).convert(text)


spot = ': '.encode()  # string转byte.指定关注字符': '（因为观察result0.log发现发言内容只是后面一截）
for i in range(0, 3):  # 这里需人工指定。我给的示例telegram/result0.log~result2.log，故range(0,3)
    filename = 'telegram/result'+str(i)+'.log'
    filename_temp = 'tempTexts/result'+str(i)+'_temp.log'
    filename_clean = 'cleanTexts/result'+str(i)+'_clean.log'
    f1 = open(filename, 'r')
    lines = f1.readlines()
    for line in lines:
        index = line.index(spot)  # 返回:的索引
        line2 = line[index+2:-1].decode()  # 只保留每一行的发言内容
        line2 = find_chinese(line2)  # 只保留汉字
        line2 = convert(line2)   # 繁转简
        with open(filename_temp, 'a', encoding='utf-8') as f2:
            f2.write(line2+'\n')
    f1.close()

    # 下面去掉空行，从temp文件变为clean文件
    f2 = open(filename_temp, 'r', encoding='utf-8')  # 要去掉空行的文件
    f3 = open(filename_clean, 'w', encoding='utf-8')  # 生成没有空行的文件
    try:
        while True:
            line = f2.readline()
            if len(line) == 0:
                break
            if line.count('\n') == len(line):
                continue
            f3.write(line)
    finally:
        f2.close()
        f3.close()

