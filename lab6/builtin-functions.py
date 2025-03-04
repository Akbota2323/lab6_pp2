from functools import reduce
def mult(x, y):
    return x * y

num=[1,2, 3, 4, 5]

result = reduce(mult, num)

print( result)




#2
def count_case(string):
    up_count = sum(c.isupper() for c in string)
    low_count = sum(c.islower() for c in string)
    
    return up_count, low_count

i_string = input()

upper, lower = count_case(i_string)

print(upper)
print(lower)


#3
def palindrome(string):
    string = string.replace(" ", "").lower()
    
    return string == string[::-1]
i_string = input()
if palindrome(i_string):
    print("YES")
else:
    print("NO")



#4
import time
import math

num = float(input())
milli = int(input())

sec = milli / 1000

result = math.sqrt(num)

print(f"Square root of {num} after {milli} milliseconds is {result}")

#5
def myFunction(tup):
    return all(tup)

i_tuple = (1, 2, 3, 4)

if myFunction(i_tuple):
    print(True)
else:
    print(False)

    