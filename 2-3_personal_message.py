#from section 2.3 - basically use a variable to define a name and then print a message
first_name = "andy"
last_name = "mccann"
print(first_name)
print(first_name.upper())
print(f"{first_name} {last_name}") #this is not a good way of doing this - better to use a variable
full_name = f"{first_name} {last_name}"
print(full_name)
print(full_name.title())
print("Hello, {full_name} welcome to my program")
print(f"Hello, {full_name} welcome to my program") #good example of what f does