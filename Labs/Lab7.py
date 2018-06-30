dic = {}
keys = dic.keys()
''' Handle '''
for line in open("words.txt"):
    line = line.strip()
    for word in line:
        if word in keys:
            dic[word] += 1
        else:
            dic[word] = 1
''' Printer '''
for data in sorted(dic.values()):
    for elem in dic.keys():
        if dic.get(elem) == data:
            print(elem,":  ",data)