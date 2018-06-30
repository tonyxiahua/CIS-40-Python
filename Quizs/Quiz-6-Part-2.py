countList = [0, 0, 0]
def counter(countList):
    fin = open("python-description.txt")
    for line in fin:
        countList[0] += 1;
        countList[1] += len(line.split());
        for characters in line:
            countList[2] += 1;
    print(countList[0],countList[1],countList[2]);
counter(countList);