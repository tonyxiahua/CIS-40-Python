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

'''
Write a program to help one cheat at the online and/or hardcopy Jumble word game. Its input should be a single user-entered word (uppercase, lowercase, or a mixture of both). Its output should be every word in words.txtPreview the document that can be derived by reordering the letters in the input word. The input word and the output word(s) thus have to be the exact same length with the exact same set of letters, other than your program should ignore case when determining matches. Sample input and output is given below. Note that in most cases, your program will only find one output word. And of course, if the input word cannot be unjumbled to match a word in the words.txt file, your output line will be empty.

Submit your program via uploading a file named jumble.py, which I will execute myself.

As usual, do not use any features we have not studied (recursion + everything after Chapter 10 in the book).
'''