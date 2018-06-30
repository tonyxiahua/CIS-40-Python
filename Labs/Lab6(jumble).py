'''
Core Function 
'''
def searchCore(text):
    vocaDic = ['','','','','','','','','','','','','','','','','','','','','','','','','','']
    textString = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for character in text:
        for index in range(0,26):
            if (character == textString[index]):
                vocaDic[index] += textString[index]
    for elem in vocaDic:
        result += elem
    result.strip()
    return result

'''
Interface 
'''
def handle(text):
    #Part one text handle 
    text = text.lower()
    searchText = searchCore(text)
    #Part two text search
    fin = open("words.txt")
    for line in fin:
        line = line.strip()
        if(searchText == searchCore(line)):
            print(line,end=" ")


text = input("Enter a jumbled word of any length: ")
handle(text)

'''
Example Output

Enter a jumbled word of any length: aa
aa 


Enter a jumbled word of any length: UPsYr
pursy syrup 

'''