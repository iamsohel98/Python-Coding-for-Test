# Programme to reverse a string after removing duplicates.
'''''
input_string = input()
output_string = ""

for i in input_string:
    if i not in output_string:
        output_string +=i
print(output_string[::-1])
'''
string = input()

d = list(dict.fromkeys(string)) # using dict in key valu are uniqe
d.reverse()
print("".join(d))
