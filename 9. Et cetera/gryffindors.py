students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


gryffindors = filter(lambda student: student["house"] == "Gryffindor", students)
for gryffindor in sorted(gryffindors, key=lambda gryffindor: gryffindor["name"]):
    print(gryffindor["name"], end=" ")

# dictionnary generation

students = ["Hermione", "Harry", "Ron"]
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)

for index, student in enumerate(students):
    print(f"{index + 1}. {student}")
