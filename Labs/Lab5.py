wordLongest =  ''
wordLongestCount = 0
wordShortest = ''
wordShortestCount = 1909 #Taken from longest english word lettes from wikipedia
wordCount = 0
wordTotal = 0

fin = open('words.txt')
for line in fin:
    word = line.strip()
    
    #For Part 1
    if len(word) > wordLongestCount:
        wordLongest = word
        wordLongestCount = len(word)

    #For Part 2 
    #the shortest will never greater than the longest
    if len(word) < wordShortestCount:
        wordShortest = word
        wordShortestCount = len(word)
        
    #For Part 3 
    wordTotal = wordTotal + 1
    wordCount = wordCount + len(word)
    
print("The longest words are", wordLongestCount ,"characters; an example is" , wordLongest)
print("The shortest words are", wordShortestCount ,"characters; an example is",wordShortest)
print("The average word length is",wordCount/wordTotal)


'''
Screen Output

The longest words are 21 characters; an example is counterdemonstrations
The shortest words are 2 characters; an example is aa
The average word length is 7.933511409466738
'''