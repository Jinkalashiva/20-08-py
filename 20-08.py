# # Armstrong Number

# num1 = int(input('Enter Number'))
# temp = num1
# count = len(str(num1))

# sum = 0
# while temp > 0:
#     digit = temp % 10
#     print(digit)
#     sum +=digit ** count
#     temp = temp //10

# if sum == num1:
#     print("Armstong Number")

# else:
#     print("Not Armstrong Number")



# with out convert string
# num1 = int(input("enter number"))
# temp = num1
# num2 = num1
# count = 0

# while num2 > 0:
#     digit = num2 % 10
#     num2 = num2 // 10
#     count +=1
# print(count)
# sum = 0
# while temp >0:
#     digit = temp % 10
#     print(digit)
#     sum +=digit ** count
#     temp = temp //10

# if sum == num1:
#     print('Armstrong')

# else:
#   print('Not Armstrong')





# method 2
num1 = int(input('enter number'))
str_num = str(num1)
sum = 0
for i in str_num:
    sum += int(i)**len(str_num)
    num1 // 10
    
    

print(sum)
if sum == num1:
    print("a")
else:
    print("n")









# 153 =>1**3+5**3+3**3 =1+125+27

# num1=int(input('enter number'))
# temp = num1
# sum = 0
# while num1 >0:
#     rem = num1 % 10
#     print(rem)
#     sum += rem**3
#     num1 = num1 //10

# print(sum)
# if temp == sum:
#     print("Armstrong Number")
# else:
#     print("NOt Armstrong Number")