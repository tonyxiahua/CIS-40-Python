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
        median = int(gradeList[int(counter/2)+1])
        #Fixed before
        #median = int(gradeList[counter/2+1])
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
gradeAnalyzer("numbers-odd.txt")

'''
Output
Mean grade is : 56.8125
Median grade is : 52.5
Mode grade(s) : 0 46 95 occurred 2 time(s) each
'''

'''
Mean grade is : 57.53333333333333
Median grade is : 53
Mode grade(s) : 0 95 occurred 2 time(s) each
'''