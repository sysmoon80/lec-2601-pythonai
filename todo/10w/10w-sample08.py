scoreDic = {}
with open("./data/10w/score.txt", "r") as f:
    line = f.readline()
    while line != "":
        tempList = line.split(":")
        scoreDic[tempList[0]] = int(tempList[1].strip("\n"))
        line = f.readline()

print(scoreDic)
