# list and dictionary comprehensions
import pandas
import random

# list comprehension =  create new list from existing list
list = [1, 2, 3, 4, 5]
new_list = []
for i in list:
    new_list.append(i+1)

print(list, new_list)


new_list_comprehension = [n+1 for n in list]
print(new_list_comprehension)

name = "Abhinav"
myList = [letter for letter in name]
print(myList)

numList = [num*2 for num in range(1, 5)]
print(numList)

# we can add a test to the list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = [n for n in numbers if n % 2 == 0]
print(even_nums)

names = ["Alex", "Beth", "Randy", "Caroline", "Dave", "Herman"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) >= 5]
print(short_names)
print(long_names)


# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

new_names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student: random.randint(10,101) for student in new_names}
passed_students = {student: value for (student, value) in students_scores.items() if value > 60 }
print(students_scores)
print(passed_students)

# DataFrame looping
students = {
    "student": ["Abhinav", "James", "Lily"],
    "score": [56, 76, 98]
}

student_Dataframe = pandas.DataFrame(students)
print(student_Dataframe)

print("\n")

# loop through rows of dataframe
for (index, row) in student_Dataframe.iterrows():
    # print(index)
    # print("\n")
    # print(row)
    # print("\n")
    print(row.student)
    print(row.score)