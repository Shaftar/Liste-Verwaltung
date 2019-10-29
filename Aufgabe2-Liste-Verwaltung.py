from termcolor import colored
liste = []
anfrage = str
hallotext = colored("To close  'Enter' ", 'magenta')
print("Hallo, was möchtest du tun?")
print("a) Liste anzeigen")
print("b) Listenelemente hinten anfügen")
print("c) Listenelement an einer bestimmten Stelle einfügen")
print("d) Listenelement löschen")
print("e) Suchen (Vorhandensein bestätigen und Index eines Elementes ausgeben)")
print("Bitte geben Sie einen Buchstaben von (a,b,c,d,e) ein")
print(hallotext)
print()
while True:
    print()
    eingabe = input('Enter new order:')
    if eingabe == 'a':
        if not liste:
            text = colored('List is empty', 'red')
            print(text)
        else:
            print('list contains: ... ', end='')
            for i in liste:
                print(i + " ", end=" ")
    elif eingabe == 'b':
        print("...............to exit 'Enter'")
        while anfrage != '':
            text0 = colored('please enter elements:', 'blue')
            WriteToList = input(text0)
            liste.append(WriteToList)
            if WriteToList == '':
                liste.remove('')
                break
    elif eingabe == 'c':
        print("..................to exit 'Enter'")
        while anfrage != '':
            text1 = colored("pleas enter element: ", 'blue')
            eingabe2 = input(text1)
            if eingabe2 != '':
                print("Index of list " + str(len(liste)))
                text2 = colored("pleas enter index of element: ", 'yellow')
                zahl = int
                try:
                    zahl = int(input(text2))
                except ValueError:
                    print('PLease input a valid integer')
                boolwert = False
                if zahl <= len(liste):
                    liste.insert(zahl, eingabe2)
                    text7 = colored(" added to list! ", 'green')
                    print(eingabe2 + text7)
                else:
                    text3 = colored("Index out of range", 'red')
                    print(text3)
                    pass
            else:
                break
    elif eingabe == 'd':
        print(".................to exit 'Enter'")
        while anfrage != '':
            text4 = colored("pleas enter element to delet: ", 'blue')
            eingabe3 = input(text4)
            boolwert1 = False
            if eingabe3 != '':
                for i in liste:
                    if eingabe3 == i:
                        boolwert1 = True
                if boolwert1:
                    liste.remove(eingabe3)
                    print(eingabe3 + ' has been removed!')
                else:
                    text6 = colored("Element is not in list!", 'red')
                    print(text6)
                    pass
            else:
                break
    elif eingabe == 'e':
        print("..................................to exit 'Enter'")
        while anfrage != '':
            text5 = colored('please enter element to show index: ', 'blue')
            eingabe4 = input(text5)
            boolwert2 = bool
            if eingabe4 != '':
                for i in liste:
                    if eingabe4 == i:
                        boolwert2 = True
                        break
                    else:
                        boolwert2 = False
                        pass
                if not boolwert2:
                    text3 = colored("Element is not in list!", 'red')
                    print(text3)
                    pass
                else:
                    print(str(liste.index(eingabe4)))
            else:
                break
    else:
        exit()
