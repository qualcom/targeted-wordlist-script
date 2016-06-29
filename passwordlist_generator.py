print("Hello, welcome to the personalized passwordlist creator : ")
print("please enter the necessary information:")
print("!!! leave unknown information fields empty")
print(" ")
print("""1- info about subject
2- common number passwords
3- general password list
""")
wordlist = []


def shuffle():
    lst = []
    first_name = input("first name: ")
    family_name = input("family name: ")

    birthday = input("birthday (e.g.: 13/05/1990): ")
    birth = birthday.split('/')
    if birthday != '':
        birth_year = birth[2]
        wordlist.append(birth[0] + birth[1] + birth[2])
        lst.append(birth_year)

    nicknames = input("nicknames(separated with space): ")
    nicknames = nicknames.split(' ')
    additional = input('additional info(separated with space): ')
    additional = additional.split(' ')
    up = input('uppercase words? y/n : ')
    print("\n", " ")
    if first_name != '':
        lst.append(first_name)
    if family_name != '':
        lst.append(family_name)
    for h in nicknames:
        lst.append(h)
    for j in additional:
        lst.append(j)
    wordlist.extend(lst)

    if up == 'y':
        lst2 = []
        for xo in lst:
            lst2.append(xo.title())
    else:
        lst2 = []

    lst.extend(lst2)
    lst1 = lst
    lst3 = lst
    for w in lst:
        for y in lst1:
            a = w.lower()
            b = y.lower()
            if a != b:
                wordlist.append(w+y)
            for u in lst3:
                a = w.lower()
                b = y.lower()
                c = u.lower()
                if a != b and a != c and b != c:
                    wordlist.append(w + y + u)


def common_numbers():
    n = []
    nu = []
    for g in range(10):
        n.append(str(g))
        nu.append(''.join(n))

    s = []
    su = []
    for c in n:
        s.append(c*2)
        su.append(''.join(s))

    n.clear()
    nu1 = []
    for d in range(1, 10):
        n.append(str(d))
        nu1.append(''.join(n))
    nu2 = []
    for o in nu1:
        nu2.append(o+'0')

    s1 = []
    su1 = []
    for u in n:
        s1.append(u*2)
        su1.append(''.join(s))

    other = ['123123', '12341234', '24682468', '1357913579', 'abc123', '123abc', 'abcd1234']
    other1 = ['azerty', 'aqwzsx', 'fuckyou', 'azerty123', 'wxcvbn']
    num = list(filter(lambda z: 4 <= len(z), nu))
    suf = list(filter(lambda z: 8 <= len(z) <= 10, su))
    num.extend(list(filter(lambda z: 4 <= len(z), nu2)))
    num.extend(list(filter(lambda z: 4 <= len(z), nu1)))
    num.extend(other)
    suf.extend(list(filter(lambda z: 8 <= len(z) <= 10, su1)))
    total = []
    total.extend(num)
    total.extend(suf)
    total.extend(list(h[::-1] for h in total))
    total.extend(other1)
    wordlist.extend(total)

while True:
    choice = input('> ')
    filename = input('''enter path to save the passwordlist:
    e.g.: C:\\Users\\XYZ\\ABC\\passwordlist.txt
    >  ''')
    wordlist.clear()
    f = open(filename, 'w+')
    print(" ")
    if choice == '1':
        shuffle()
        wordlist1 = list(set(wordlist))
        wordlist1.sort()
        wordlist1.sort(key=len)
        for x in wordlist1:
            print(x, end=' - ')
            f.write(x + "\n")
        f.close()
        print("\n", " ")
        print("!!! Success ^_^")
        with open(filename, 'r') as f:
            print("A password list of", len(f.read().split("\n")), "has been created")
        break
    elif choice == '2':
        common_numbers()
        wordlist1 = list(set(wordlist))
        wordlist1.sort()
        wordlist1.sort(key=len)
        for x in wordlist1:
            print(x, end=' - ')
            write = f.write(x + "\n")
        f.close()
        print("\n", " ")
        print("!!! Success ^_^")
        with open(filename, 'r') as f:
            print("A password list of", len(f.read().split("\n")), "has been created")
        break
    elif choice == '3':
        shuffle()
        common_numbers()
        wordlist1 = list(set(wordlist))
        wordlist1.sort()
        wordlist1.sort(key=len)
        for x in wordlist1:
            print(x, end=' - ')
            f.write(x + "\n")
        f.close()
        print("\n", " ")
        print("!!! Success ^_^")
        with open(filename, 'r') as f:
            print("A password list of", len(f.read().split("\n")), "has been created")
        break
    else:
        print('!!! please enter a valid answer ')
