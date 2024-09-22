"""
with open("students.csv") as file:
    for line in sorted(file):
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house} ")
"""

import csv

students = []
"""
with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
"""


"""
To read
with open("students.csv") as file:
    reader = csv.DictReader(file)  # il faut mettre le nom des clés en haut
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
"""
"""
To write
import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow(
        [name, home]
    )  # will automatically put "" if there's a "," in what i write
"""

import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(
        file, fieldnames=["name", "home"]
    )  # pour savoir quelle colonne correspond à quelle clé
    writer.writerow({"name": name, "home": home})
