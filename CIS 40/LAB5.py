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

'''
Create a program that reads words.txt (link near top of our home page) in order to:

Determine the length of the longest word(s) and output that length plus the first word of this length found.
Determine the length of the shortest word(s) and output that length plus the first word of this length found
Determine and output the average length of all the words in the list.
You should strip white space from each word before using its length in your calculations.

My solution's output is:
'''