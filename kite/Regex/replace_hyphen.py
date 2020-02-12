import re

pattern = "([\d{3}])\-(\d{3})-([\d{4}])"

user_input = input()

new_user_input = re.sub(pattern,r"\1\2\3", user_input)

print(new_user_input)
