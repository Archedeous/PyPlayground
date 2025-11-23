numbers = [3,6,192,499,2200,122,12355,2991,339023]
wordlist = ["strange","covid","jabber","strange","jamalungma"]
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 28},
    {"name": "Ethan", "age": 35},
    {"name": "Ethanes", "age": 38}
]


def even():
    even_number = []
    for i in numbers:
        if i % 2 == 0:
            even_number.append(i)
    return even_number

#print(even())

def largest():
    biggest = 0
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

#print(largest())

def age_acceptance():
    person_list = []
    for a in people:
        if a["age"] >= 25:
            person_list.append(a)
    return person_list

print(age_acceptance())
