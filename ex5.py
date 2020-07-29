name = "Kush"
age = 22
height = 174 #cms
#InchestoCms = 
weight = 72 #kgs
eyes = "brown"
teeth = 'white'
hair = 'brown'

print(f"Let's talk about {name}")
print("let's talk about", name) # another way
print(f"He's {height} cms tall")
print(f"He's {weight} kgs heavy")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"He's teeth are usually {teeth} depending on the coffee")

# this line is tricky, try to get it exactly right
total = height + weight + age
print(f"If I add {height}, {age}, and {weight}, I get {total}")