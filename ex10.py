tabby_cat = "\tI'm tabbed in" #\t indents tabs, spaces after using this gives more spaces
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat." # \\ is used to enter a backslash

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print("I'm \ a \ cat") # another method for line 3
print(fat_cat)

print(f"Hey!\n{tabby_cat}")