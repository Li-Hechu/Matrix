import time


def filelog(consequence: str):
    with open("filelog.log", "a+") as file:
        file.write(time.strftime("%Y-%m-%d %H-%M-%S",
                   time.localtime())+"  "+consequence+"\n")
