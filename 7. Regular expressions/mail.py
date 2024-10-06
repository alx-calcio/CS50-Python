import re

email = input("What's your email? ")

matches = re.search(r"([(\w)+(\-\.)?]*\w+)@((?:[\w-]+\.)+[\w-]{2,})", email)
print(matches.groups())
