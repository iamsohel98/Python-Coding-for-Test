# Statement : A string of comma saparated number are given such that the numbers 4 and 7 are already present in the list .
# Assume that 7 alwaya comes  after 4 in yhe given string
num_list = input().split(",")
length = len(num_list)

index_4 = num_list.index('4')
index_7 = num_list.index('7')

num1 = 0
num2 = ""

for i in range(0,length):
    if(i<index_4 or i>index_7):
        num1 +=int(num_list[i])

for i in range(index_4,index_7 +1):
    num2 +=num_list[i]

print(num1 + int(num2))
#Another way

L1 =list(map(int,input().split(",")))
num1 = sum(L1[:L1.index(4)]) + sum(L1[L1.index(7)+1:])
LST = L1[L1.index(4):L1.index(7)+1]
num2 = ""
for i in LST:
    num2 += str(i)

print(int(num2)+ num1)
