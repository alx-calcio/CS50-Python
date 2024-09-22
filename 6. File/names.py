name = input("what's your name ? ")
"""
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
"""

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(f"Hello, {line.rstrip()}")


with open("names.txt", "r") as file:  # "r" default donc pas besoin de l'écrire
    for line in file:
        print("hello,", line.rstrip())


names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

"""

with open("names.txt") as file:
    for line in sorted(file):
        print(f"hello, {line.rstrip()}")
