"""
print(f"Deux tiers vaut {200000/3:.2f}")
print(f"Grand nombre {1000000000:,}")
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
for student in students:
    print(student)  # affiche les clés

students = [{"name": "Alex", "age": 20}, {"name": "Bob", "age": 24}]
print("name" in students[0])


try:
    exec('print("salut)')
except SyntaxError:
    print("T'as fait une erreur de syntaxe patate")
else:
    print("Ca a marché")
"""

a = ["aa", "bb", "cc", "dd"]
print(a[:3])

"""
 ____             _           _   _ _       _      
|  _ \ __ _ _ __ | |__   __ _(_)_(_) |   __| | ___ 
| |_) / _` | '_ \| '_ \ / _` |/ _ \| |  / _` |/ _ \
|  _ < (_| | |_) | | | | (_| |  __/| | | (_| |  __/
|_| \_\__,_| .__/|_| |_|\__,_|\___||_|  \__,_|\___|
__     __  |_|            _   _                    
\ \   / /_ _| | ___ _ __ | |_(_)_ __               
 \ \ / / _` | |/ _ \ '_ \| __| | '_ \              
  \ V / (_| | |  __/ | | | |_| | | | |             
   \_/ \__,_|_|\___|_| |_|\__|_|_| |_|                  
Ascii Art                                                                   
"""
