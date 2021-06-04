char = len(input("what is your name ?"))

# Example of type error 
#print("Your name has " + char + "characters")

# Example of type checking
print(type(char)) 

# Example of type conversion or type casting

new_char = str(char)
print("Your name has " + new_char + " characters")
