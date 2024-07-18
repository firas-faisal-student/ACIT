# password = 123
# count = 0

# while count !=3:
#     user = int(input("please enter your password "))
#     if user==password:
#         print("welcome user")
#         break
#     else:
#         print("incorrect password ")
#         count +=1

# print("account blocked")

# x = 0
# while x < 50:
#         print(x)
#         x = x + 5

# for x in range(1,10,2):
#     print("Value of x = ", x)
# print("This is the end of the program")

# x = 0
# y = 0
# while x <= 6:
#     print("Firas Faisal", )
#     x +=1
#     y +=x

# print("sum of counting numbers", y)

number=0
evensum=0
oddsum=0
check=0
for number in range(0,20):
    number+=1
    check = number%2
    if check==0:
        evensum= evensum + number
    else:
        oddsum = oddsum + number

print("evensum is ", evensum)
print("odd sum is ",oddsum)

print("================")
for x in range(1,10):
  print("| ",x,"x 9 = " ,x*9, " |")
print("================")

x=1
print("================")
while x <=9:
  print("| ",x,"x 9 = " ,x*9, " |")
  x+=1
print("================")


    


