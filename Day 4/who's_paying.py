# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#.split(", ") take out , and space and put everything in list.
#Write your code below this line 👇
#num_items=len(names)
#random_choice=random.randint(0, num_items-1)#last index is actually one less than no. of items.  
#pay=names[random_choice]

#using random.choice instead
pay=random.choice(names)

print(pay+" is going to pay today")