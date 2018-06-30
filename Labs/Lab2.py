'''
1. Write a function named powers that has one parameter named num. This function should always produce 11 lines of output, one for the parameter raised to the 0th power through one for the parameter raised to the 10th power.

Show both your function definition and three calls of the function, along with the output from those calls. Here are my three calls along with their output.

>>> powers(2)
1
2
4
8
16
32
64
128
256
512
1024
>>> powers(3)
1
3
9
27
81
243
729
2187
6561
19683
59049
>>> powers(10)
1
10
100
1000
10000
100000
1000000
10000000
100000000
1000000000
10000000000
>>>

2. Write a function named palindrome that has five parameters, named l1, l2, l3, l4, and l5. This function should be called with five single-char string arguments. palindrome should produce two lines of output, one of the parameters in order from left to right, and one of the parameters in order from right to left, so that a quick visual inspection will reveal whether the parameter is a palindrome or not. (A palindrome is a word that is spelled the same forwards as backwards.)

Show both your function definition and three calls of the function, along with the output from those calls. Here are my three calls along with their output.

>>> palindrome('l','e','v','e','l')
level
level
>>> palindrome('r','e','f','e','r')
refer
refer
>>> palindrome('s','y','r','u','p')
syrup
purys
>>> 

3. Write a function named miles_converter that has one parameter, named miles. This function should produce one line of output, showing the number of yards, feet, and inches represented by miles.

Show both your function definition and one call of the function, along with the output from that call. Here is my one call along with its output.

>>> miles_converter(3.4)
3.4 miles = 5984.0 yards, 17952.0 feet, 215424.0 inches
>>>
'''

#Question 1
def powers(num):
print(num**0)
print(num**1)
print(num**2)
print(num**3)
print(num**4)
print(num**5)
print(num**6)
print(num**7)
print(num**8)
print(num**9)
print(num**10)

powers(4)
powers(5)
powers(6)
#Output 1
'''
1
4
16
64
256
1024
4096
16384
65536
262144
1048576

1
5
25
125
625
3125
15625
78125
390625
1953125
9765625

1
6
36
216
1296
7776
46656
279936
1679616
10077696
60466176
'''
#Question 2
def palindrome(l1,l2,l3,l4,l5):
print(l1+l2+l3+l4+l5)
print(l5+l4+l3+l2+l1)

palindrome('h','a','p','p','y')
palindrome('r','o','g','o','r')
palindrome('l','e','b','e','l')
#Output 2
'''
happy
yppah

rogor
rogor

lebel
lebel
'''
#Question 3
def miles_converter(miles):
yards = 1760 * miles
feet = 5280 * miles
inches = 63360 * miles
print (miles,"miles =",yards,"yards,",feet,"feet,",inches,"inches")

miles_converter(3.2)
miles_converter(4.8)
miles_converter(9.6)
#Output 3 
'''
3.2 miles = 5632.0 yards, 16896.0 feet, 202752.0 inches
4.8 miles = 8448.0 yards, 25344.0 feet, 304128.0 inches
9.6 miles = 16896.0 yards, 50688.0 feet, 608256.0 inches
'''