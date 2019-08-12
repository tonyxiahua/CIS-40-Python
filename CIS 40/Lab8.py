def gradeAnalyzer(file):
    total = 0 
    counter = 0
    gradeDic = {}
    gradeList = []    
    text = ''
    demo = []
    '''Part 1'''
    for value in open(file):
        gradeList.append(value.strip())
        total += int(value)
        counter += 1
        if value.strip() in gradeDic:
            gradeDic[value.strip()] += 1
        else:
            gradeDic[value.strip()] = 1
    print("Mean grade is :",total/counter)
    gradeList = sorted(gradeList)
    '''Part 2'''
    if counter %2 == 0:
        median = (int(gradeList[int(counter/2)])+int(gradeList[int(counter/2+1)]))/2
    else:
        median = int(gradeList[int(counter/2+1]))
    print("Median grade is :",median)
    '''Part 3'''
    if max(gradeDic.values()) == 0:
        print("Error")
    else:    
        for keys in gradeDic.keys():
            if gradeDic[keys] == max(gradeDic.values()):
                demo.append(keys)
        for elem in sorted(demo):
            text += elem +' '
        print("Mode grade(s) :",text+"occurred",max(gradeDic.values()),"time(s) each")
gradeAnalyzer("numbers-even.txt")
'''
Output
Mean grade is : 56.8125
Median grade is : 52.5
Mode grade(s) : 0 46 95  occurred 2 time(s) each
'''

'''
Write a grade-analyzer program that takes as its input the name of a file containing student scores between 0 and 100, inclusive, and outputs three values:

mean - average of all the scores
median - arithmetic midpoint of all the scores
mode - most frequently occurring score(s) and the number of times that score(s) appeared
NOTE: If the number of scores in the input file is odd, then the median should be the middle value, arithmetically. If the number of scores in the input file is even, then the median should be the average of the values around the midpoint. For example, a file with 16 scores would have a median that was the average of the 8th and 9th values.

To submit your assignment, upload a single source code file.

You should test your program against at least this file: numbers-even.txtPreview the document

My program's output, using the above file for input, is:
'''