# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
###NOTE [0] start using indexing
print("Starts with D:")
a = [
    human.name for human in humans if human.name[0] is 'D'
]
print(a) # ['Daphne', 'David']
##tested in intelliJ WORKS

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
###NOTE [-1] end using indexing
print("Ends with e:")
b = [
    human.name for human in humans if human.name[-1] is 'e'
]
print(b) #['Alice', 'Charlie', 'Daphne', 'Eve']
##tested in intelliJ WORKS

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
# NOTE itirate through list to print names beginning with 'C' and 'G
print("Starts between C and G, inclusive:")
c = [
    human.name for human in humans if human.name.startswith(('C', 'D','E','F',"G"))
] #used built in method startswith
print(c) # ['Charlie', 'Daphne', 'Eve', 'Frank', 'Glenn', 'David']
##tested in intelliJ WORKS

# Write a list comprehension that creates a list of all the ages plus 10.
# NOTE write logic for list that adds all ages then adds 10
print("Ages plus 10:")
d = [
    human.age + 10 for human in humans
]
print(d) #[39, 42, 47, 40, 36, 28, 52, 22, 51, 41]
##tested in intelliJ WORKS

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
# NOTE add name + "-" + str
print("Name hyphen age:")
e = [
    human.name + "-" + str(human.age) for human in humans
]
print(e) # ['Alice-29', 'Bob-32', 'Charlie-37', 'Daphne-30', 'Eve-26', 'Frank-18', 'Glenn-42', 'Harrison-12', 'Igon-41', 'David-31']
##tested in intelliJ WORKS

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [
    (human.name, human.age) for human in humans if human.age >= 27 and human.age <= 32
]
print(f) #[('Alice', 29), ('Bob', 32), ('Daphne', 30), ('David', 31)]

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
# NOTE make use of built in .upper
print("All names uppercase:")
g = [
    Human(human.name.upper(), human.age+5) for human in humans
]
print(g) #[<Human: ALICE, 34>, <Human: BOB, 37>, <Human: CHARLIE, 42>, <Human: DAPHNE, 35>, <Human: EVE, 31>, <Human: FRANK, 23>, <Human: GLENN, 47>, <Human: HARRISON, 17>, <Human: IGON, 46>, <Human: DAVID, 36>]


# Write a list comprehension that contains the square root of all the ages.
# NOTE i hate math
print("Square root of ages:")
import math
h = []
print(h)
