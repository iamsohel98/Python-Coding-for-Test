# Take a string as input ,Saparate all the integer from it, Then take each integer  only once and from a largest even number possible. 
# print largest even number possible and if the number can't be made, then print -1.

import re
input_str = input()
digit = list(set(re.findall("\d",input_str)))

#using LIST COMPHARESION
# digit = [ i for i in set(input_str) if i.digit()]

digit.sort() # sorting the number

digit.reverse() # reverse the digit
Number = int("".join(digit))

if Number %2 == 0:
    print(Number)
else:
    length = len(digit)
    for i in range(length -1,0,-1):
        if int(digit[i]) %2 == 0:
            a = digit[i]
            digit.remove(a)
            digit.insert(length -1,a)
            even = int("".join(digit))
            print(even)
            break
    else:
        print(-1)
