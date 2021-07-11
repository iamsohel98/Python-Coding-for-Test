# Input will be like 78253648 . Saparate odd places integer 8,5,6,8 you have to return a 4 digit OTP by squiring the digit. So OTP like 

input_num = input()
length_num = len(input_num)
result =""

for index_odd in range(1,length_num,2):
    result += str(int(input_num[index_odd])**2)

print(result[0:4])
