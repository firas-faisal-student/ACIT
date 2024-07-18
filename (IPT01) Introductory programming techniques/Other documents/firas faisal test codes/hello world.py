# # name = "mr mohamed joseph ali"
# # nam1= (name[3:10])
# # nam2= (name[11:18])
# # nam3= (name[18:22])
# # print (nam1 +' ' + nam2+' ' + nam3)
# # print ("going to correct the grammar of name \n  here is corrected name")
# # print (nam1.title() +" "+nam2.title()+" "+nam3.title()+".")

# # .upper ()
# # .lower ()
# # .title ()
# # \n (put it in the string itself with no breaks in between)
# # list
# fruits = ["apple" , "banana", "guava" , "chili", "cabbage", "carrot"]
# print (fruits)
# # it will be put in square brackets
# #veg = (fruits[3:])
# #print (veg)
# #fruits.pop()
# #fruits.append("tomato")

# #pop function is to remove the last item in the list
# #append function is to attach a new item to the last place in the list, you can attach a new list as well using a variable 
# #insert() function can be used to add something to a specific place in the list use VARIABLE.insert(INDEX_NUMBER,"ITEM")
# fruits.insert(1,"mango")
# print (fruits)
# fruits.sort()
# #print (fruits)
# fruits.sort(reverse=True)
# #print(fruits)
# #.sort() function is to sort alphabetically
# #.Sort(reverse=True) is to sort in descending alphabetical order
# #remove is to delete that  item from the list
# #fruits.remove("cabbage")
# print(fruits)
# fruits[1]="cherry"
# print(fruits)
# #use variable + square bracket + to replace that item in list
# fruits[4:6]=["melon", "cucumber"]
# print(fruits)
# print("mango" in fruits)
# #the reserved word "in" says if it is in the list or not by true or false

guess=(input("what is your guess? "))
target=5
if guess == target :
    print ("congra! your guess is correct")
elif guess > target :
    print ("your number is too big")
else :
    print ("your number is too small")    

