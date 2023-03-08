"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Robert Zunt
email: robert.zunt@gmail.com
discord: telemarkista#2523
"""
import pprint
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
splitter = "----------------------------------------"
username = input("username?")
password = input("password?")
users = {"bob": "123",
          "ann" : "pass123",
          "mike" : "password123",
          "liz" : "pass123"}
if username in users.keys():    #checks if username is in users dict
    if password == users.get(username):   #if so checks password
        print(f"Welcome to the app, {username}! \nWe have 3 texts to be analyzed.\n{splitter}")
    else:
        print("username:", username, "\npassword:", password, "\n This is unregistered user, terminating the program..")
        exit()
else:
    print("username:",username, "\npassword:", password,"\n This is unregistered user, terminating the program..")
    exit()

number_input = input("Enter a number btw. 1 and 3 to select:")  #user choose text

if number_input.isnumeric():    #checks if number is numeric
    pass
else:
    print(f"{number_input} in not whole number.")
    exit()


if int(number_input) == 1 or int(number_input) == 2 or int(number_input) == 3:  #checks if input is in range
    pass
else:
    print(f"{number_input} is out of range!! Terminating program")
    exit()

choosen_text = TEXTS[int(number_input)-1]

separated_text = choosen_text.split()
processed_text = list()

for word in separated_text:
    processed_text.append(word.strip(",.:;?!"))


capital_letter = list()
first_capital = list()
numbers_list = list()
uppercase_words = list()
lowercase_words = list()

for upperword in processed_text:    #adds CAPITAL word to list
    if upperword.isupper():
        capital_letter.append(upperword)

for capital in processed_text:      #adds words STARTING with capital to list
    if capital.istitle():
        first_capital.append(capital)

for uppercase in processed_text:       #adds uppercase words to list
    if uppercase.isupper() and not uppercase.isalpha():       #excludes numbers
        uppercase_words.append(uppercase)

for numbers in processed_text:      #add numbers to list
    if numbers.isnumeric():
        numbers_list.append(int(numbers))

for lowercase in processed_text:
    if lowercase.islower():
        lowercase_words.append(lowercase)

num_capitals = len(capital_letter)
num_titles = len(first_capital)
word_count = len(processed_text)
uppercase_count = len(uppercase_words)
numbers_count = len(numbers_list)
numbers_suma = sum(numbers_list)
lowercase_count = len(lowercase_words)

print(splitter)
print(f"There are {word_count} words in the selected text. "
      f"\nThere are {num_titles} titlecase words."
      f"\nThere are {uppercase_count} uppercase words."
      f"\nThere are {lowercase_count} lowercase words."
      f"\nThere are {numbers_count} strings."
      f"\nThe sum of all the numbers {numbers_suma}.")
print(splitter)
words_stat = dict()
for word in separated_text:
    if len(word) not in words_stat:
        words_stat[len(word)] = 1
    else:
        words_stat[len(word)] = words_stat[len(word)] + 1

for x,y in words_stat.items():
    z=y*"*"
    print(f"{x}|{z}")


