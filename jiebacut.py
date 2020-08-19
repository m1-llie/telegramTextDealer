import os 
import jieba
basedir="./cleanTexts"

#准备停用词库
with open("baidu_stopwords.txt") as f:
    stopwords=f.read().splitlines()

for root,dirs,files in os.walk(basedir):
    for singlefile in files: 
        nowfile=os.path.join(root,singlefile)
        outputfile=nowfile+'.part'
        with open(nowfile) as f:
            print("开始处理文件："+nowfile)
            finalstr=""
            try:
                texts=f.readlines()
            except:
                print("遇到编码问题")
                continue
            for line in texts:
                linecut=jieba.cut(line.replace("\n",""))
                linecut=list(linecut)
                #去停用词
                for singleword in linecut:
                    if singleword in stopwords:
                        linecut.remove(singleword)
                linestr=' '.join(linecut)
                linestr=linestr+"\n"
                finalstr+=linestr
        with open(outputfile,"w+") as f:
            f.write(finalstr)


        

