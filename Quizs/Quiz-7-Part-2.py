def AvgSentenceWords(file):
    sentence = 0
    words = 0    
    for line in open(file):
        words = words + len(line.split())
        for character in line:
            if character == '.': 
                sentence += 1
    print("Average number of words/sentence :",words/sentence)
AvgSentenceWords("python-description.txt")