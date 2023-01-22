# String
book = "labor of the land"
print('hi' + 'mom' * 3)
print(bool(2.0))
print(int(float('2.0')))

#Conditionals
order = 12

if order > 25:
    shipping = 0.00
else:
    shipping = 5.99

print(order)
print(shipping)

# Input/Output

# name = input('What is your name? ')
# age = int(input('How old are you? '))
# age = age + 5

# print("name: " + name)
# print('I will be ' + str(age + 5) + ' years old next year')

#While Loop

# password = ""
# while password != 'hello world':
#     password = input('Give me a fucking password')
#     if password == 'hello world':
#         print('Successful')
#     else:
#         print("Try again later")



# String

name = 'Stephen'
intro = 'My name is'

sentence = '{} {} and I like snacks'.format(intro, name)

print(sentence)

# # Function
# def getSum(a, b):
#     return a + b
# def printShit():
#     return "bookie"

def absolute(val):
    if val < 0:
        return -val
    else:
        return val

print(absolute(10))

# FOR LOOP

# while loop counterpart
animal = 'cat'
result = ""
count = 0

while count < len(animal):
    print(animal[count])
    count += 1

# for loop counterpart
# for char in animal:
#     result = result + char
#     print(result)

# for i in range(len(animal)):
#     result = result + animal[i]
#     print(result)

# LISTS
figures = [1,1,1,2,2,2,3,4,5,7,5,2,3,4,5, 6]

# print(figures[::-1])
# print(figures[:len(figures) - 1])

pets = ['Cooper', 'Zoey', 'Magic', 'Finn']
pets.append('doggy')
pets.insert(0, 'jaylo')
pets.insert(len(pets), 'bingo')
pets.extend(['gigz', 'liffy', 'broky'])
pets.pop()
pets.pop(3)
pets.remove('jaylo')
print(pets)
# # for figure in figures:
# #     print(figure)

# count = {}

# SETS
year = {1995, 2020, 1992, 1920, 1776, 2020}
word = set('Hello my gee')
strW = set([1,2,1,2,3,5,4,4,5])

year.add('fuck')
year.remove(1920)
year.pop()
print(word)
print(year)
print(strW)

# for figure in figures:
#     if figure in count:
#         count[figure] += 1
#     else:
#         count[figure] = 1

# # while count < len(figures):
# #     print(figures[count])
# #     count += 1

# Dictionaries

movie_info = {
    'title': 'Sherlock Holmes',
    'year': 2009,
    'rating': 5.0,
    'running_time': 112,
    'actors': ['Robert Downey Jr.', 'Dr. Watson']
}
movie_info['sequel'] = True
movie_info.pop('year')
print(movie_info)
print(movie_info['actors'])

for k in movie_info:
    print(k + ': ')
    print(movie_info[k])