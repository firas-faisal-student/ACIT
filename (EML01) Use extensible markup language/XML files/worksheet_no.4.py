import math
def hyp(x,y):
    a=math.pow(x,2)
    b=math.pow(y,2)
    c=math.sqrt(a+b)
    print("hypotenuse length is ",c )

x = int(input("enter a "))
y = int(input("enter b "))

hyp(x,y)

