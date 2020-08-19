import os

with open("group.txt") as f:
    channels=f.readlines()

for nowid,item in enumerate(channels):
    item=item.replace("\n","")
    nowcmd="telegram-messages-dump -c@"+item+" -p +8612345678901 -l 0 -o result"+str(nowid)+".log"
    os.system(nowcmd)
print("finished")