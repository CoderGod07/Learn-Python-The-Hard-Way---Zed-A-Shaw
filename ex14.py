from sys import argv

script, user_name = argv
prompt = '> '      # handy to use so that we dont have to type everytime we use an input

print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer fo you have?")
computer = input(prompt)

print(f"""
Alright so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
