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
'''
Write a histogram program which counts every letter in words.txt, then outputs each character and its number of occurrences. 
The output should be in sorted order from least-frequently occurring letter to most-frequently occurring letter. 
Your program should treat each letter in a case-insensitive fashion which isn't relevant for words.txt 
but is relevant for many other input files on which such a textual analysis program might be used.
Your program should right-justify the counts in a manner similar to my output below, but as always, 
without using any features we haven't yet studied.
You must use a dictionary to store your letter/count pairs, i.e., 
I do NOT want to see 26 variables, one per letter of the alphabet, in your code!
To submit this assignment, upload a file which I can download and execute to test.
'''