from itertools import permutations
print("""
*************************************
 Targeted Wordlist Script By qualcom
        github.com/qualcom
        fb.com/violentpawn
*************************************""")
filepath = input('''\nEnter wordlist path:
e.g.: C:\\Users\\XYZ\\Desktop\\wordlist.txt\n> ''')


def cap(string):
    string = str(string)
    return string[0].upper() + string[1:]

final_wordlist = []
prefinal_wordlist = []
wordlist = []

print('\n!!! U can ignore any step by leaving it empty')

name = input('\nFull name: ')
name = name.lower()
wordlist.extend(name.split(' '))

while True:
    birthday_string = input('\nBirthday (dd/mm/yyyy): ')
    birthday = birthday_string.split('/')
    if len(birthday_string) == 10:
        wordlist.append(birthday[2])
        wordlist.append(''.join(birthday))
        wordlist.append(birthday[0] + birthday[1] + birthday[2][2:])
        wordlist.append(str(int(birthday[0])) + str(int(birthday[1])) + birthday[2][2:])
        break
    elif birthday_string and len(birthday_string) != 10:
        print(birthday)
        print('!!! Please enter a valid date.')
    else:
        break

additional = input('\nAdditional information \
seperated with a single space:\n\
e.g.: nicknames, family, id number, cellphone number, usernames, etc.)\n> ')
if additional:
    wordlist.extend(additional.split(' '))

answer = input('Any letter substitutions? e.g.: p@ssw0rd.'
               '\nWrite ur substitutions as following:\na:@ e:3 s:5 i:1 o:0 l:1\n> ')
if answer:
    subs_wordlist = []
    subs = dict(x.split(':') for x in answer.split(' '))
    for key, value in subs.items():
        occur_all = [wordlist[x].replace(key, value) for x in range(len(wordlist))]
        occur_first = [wordlist[x].replace(key, value, 1) for x in range(len(wordlist))]
        occur_last = [''.join(reversed(wordlist[x][::-1].replace(key, value, 1))) for x in range(len(wordlist))]
        subs_wordlist.extend(occur_all)
        subs_wordlist.extend(occur_first)
        subs_wordlist.extend(occur_last)
    for x in list(permutations(subs_wordlist, 2)):
        if x[1].lower() != x[0].lower():
            prefinal_wordlist.append(''.join(x))

wordlist_up = []
for item in wordlist:
    wordlist_up.append(cap(item))
wordlist.extend(wordlist_up)

prefinal_wordlist.extend(wordlist)
prefinal_wordlist.extend(wordlist_up)
for x in list(permutations(wordlist, 2)):
    if x[1].lower() != x[0].lower():
        prefinal_wordlist.append(''.join(x))
for y in list(permutations(wordlist, 3)):
    if y[1].lower() != y[0].lower() and \
       y[2].lower() != y[1].lower() and \
       y[2].lower() != y[0].lower():
            prefinal_wordlist.append(''.join(y))

final_wordlist.extend(prefinal_wordlist)
char = input('Any symbols at the end? e.g.: ? ! @ *'
             '\n!!! Note that this will make the wordlist huge\n> ')
char = char.split(' ')
for x in prefinal_wordlist:
    for y in char:
        final_wordlist.append(x + y)

final_wordlist = list(set(final_wordlist))
final_wordlist.sort()
final_wordlist.sort(key=len)

with open(filepath, 'w') as file:  # linux pass the arg """ newline='\n' """
    for pswrd in final_wordlist[:-1]:
        file.write(pswrd + '\n')
    file.write(final_wordlist[-1])
with open(filepath, 'r') as file_read:
    print('Mission accomplished ^__^')
    print("A wordlist of", len(file_read.read().split("\n")), "passwords has been created")
