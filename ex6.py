# storing value in variable
types_of_people = 10
# storing a string with a varianle in it
x = f"There are {types_of_people} types of people"
#stroing a string in a variable
binary = "binary"
# storing a string in a variable
do_not = "don't"
# storing a string with a variable with a string in it
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
#storing a string in a variable
joke_evaluation = "Isn't that joke so funny?! {}"
#printing the variable and performing format method to add another variable storing a value to the variable storing string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)