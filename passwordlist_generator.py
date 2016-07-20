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
wordlist = []
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
seperated with a single space:\n \
e.g.: nicknames, family, id number, cellphone number, usernames, etc.)\n> ')
if additional:
    wordlist.extend(additional.split(' '))

wordlist_up = []
for item in wordlist:
    wordlist_up.append(cap(item))
wordlist.extend(wordlist_up)

final_wordlist.extend(wordlist)
final_wordlist.extend(wordlist_up)
for x in list(permutations(wordlist, 2)):
    if x[1].lower() != x[0].lower():
        final_wordlist.append(''.join(x))
for y in list(permutations(wordlist, 3)):
    if y[1].lower() != y[0].lower() and \
       y[2].lower() != y[1].lower() and \
       y[2].lower() != y[0].lower():
            final_wordlist.append(''.join(y))
final_wordlist = list(set(final_wordlist))
final_wordlist.sort()
final_wordlist.sort(key=len)

with open(filepath, 'w') as file:  # linux pass the arg newline='\n'
    for pswrd in final_wordlist[:-1]:
        file.write(pswrd + '\n')
    file.write(final_wordlist[-1])
with open(filepath, 'r') as file_read:
    print('Mission accomplished ^__^')
    print("A wordlist of", len(file_read.read().split("\n")), "passwords has been created")
