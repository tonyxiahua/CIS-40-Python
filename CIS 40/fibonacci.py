"""
A function outputs the first number of Fibonacci number
"""
def fibonacci(index):
    number1 = 0
    number2 = 1
    counter = 0
    
    if index <= 0:
        print("Enter a value greater than 0")
    elif index == 1:
        print(number1)
    else:
        while counter < index:
            print(number1)
            numberNext = number1 + number2
            number1 = number2
            number2 = numberNext
            counter += 1
        
fibonacci(12)

"""
Output:

0
1
1
2
3
5
8
13
21
34
55
89
"""