# telegramTextDealer
telegram spider aiming at multiple groups, with texts-cleaning and jieba-cutting stuff ---> 针对telegram群组的记录爬取、文本清洗及分词等处理

## 01 爬取指定telegram群组
spider功能由[Kosat](https://github.com/Kosat)提供，repo在[这里](https://github.com/Kosat/telegram-messages-dump)。根据他的提示，安装telegram-messages-dump包后即可工作。（前提：有自己的telegram账号，要接收验证码）<br>
但是！他的只能通过一个命令行指定爬取一个telegram群组。因此我们改进了一下，希望给定group.txt来指明一个群组列表。<br>
因此，你可以这样开始：<br>
1.安装包：
```python
pip install telegram-messages-dump
```
2.爬取group.txt中指定的所有群组：
```python
python whichGroup.py
```
备注：<br>
尝试发现本机挂代理仍可能有连接问题。建议放外国服务器上跑脚本。另外，爬取记录时的有关设置可以在whichGroup.py中更改，目前设置的是爬取群组建立以来的所有历史消息：<br>
```python
nowcmd="telegram-messages-dump -c@"+item+" -p +8612345678901 -l 0 -o result"+str(nowid)+".log"
```
可选参数等信息，从[Kosat](https://github.com/Kosat)的[repo](https://github.com/Kosat/telegram-messages-dump)介绍中拷贝过来了，供大家查阅：
```
telegram-messages-dump -c <chat_name> -p <phone_num> [-l <count>] [-o <file>] [-cl]

Where:
    -c,  --chat     Unique name of a channel/chat. E.g. @python.
    -p,  --phone    Phone number. E.g. +380503211234.
    -o,  --out      Output file name or full path. (Default: telegram_<chatName>.log)
    -e,  --exp      Exporter name. text | jsonl | csv (Default: 'text')
      ,  --continue Continue previous dump. Supports optional integer param <message_id>.
    -l,  --limit    Number of the latest messages to dump, 0 means no limit. (Default: 100)
    -cl, --clean    Clean session sensitive data (e.g. auth token) on exit. (Default: False)
    -v,  --verbose  Verbose mode. (Default: False)
      ,  --addbom   Add BOM to the beginning of the output file. (Default: False)
    -h,  --help     Show this help message and exit.
```
这时群组记录就爬取下来了。放进telegram文件夹中。本例中我在telegram文件夹中已经提供了result0.log，result1.log和result2.log。<br>
## 02 文本清洗
需要先手动建立tempTexts和cleanTexts两个空文件夹。<br>
```python
python text-cleaning.py
```
此时会从telegram中读取文件，经过去特殊符号、去标点符号、去数字字母、去空格、繁转简等操作后将纯简体中文字符文本存入tempTexts文件夹，命名如result0_temp.log；<br>
再去除空行后存入cleanTexts文件夹，命名如result0_clean.log。<br>
我给的例子中目前是两个空文件夹，你可以尝试运行得到处理后文本。
## 03 结巴分词、去停用词：
```python
python jiebacut.py
```
从cleanTexts中读取文件如result0_clean.log进行处理并覆盖文本。
