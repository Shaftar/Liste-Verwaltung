from termcolor import colored
liste = []
anfrage = str
print("Hallo, was möchtest du tun?")
print("a) Liste anzeigen")
print("b) Listenelemente hinten anfügen")
print("c) Listenelement an einer bestimmten Stelle einfügen")
print("d) Listenelement löschen")
print("e) Suchen (Vorhandensein bestätigen und Index eines Elementes ausgeben)")
print("Bitte geben Sie einen Buchstaben von (a,b,c,d,e) ein")
print("To close  'Enter' ")
print()
while True:
    print()
    eingabe = input('Enter new order:')
    if eingabe == 'a':
        if not liste:
            text = colored('List is empty', 'red')
            print(text)
        else:
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
                text2 = colored("pleas enter index of element: ", 'orange')
                zahl = int(input(text2))
                if zahl <= len(liste):
                    #liste.remove(liste[zahl])
                    liste.append(eingabe2[zahl])
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
            if eingabe3 != '':
                liste.remove(eingabe3)
            else:
                break
    elif eingabe == 'e':
        print(".................to exit 'Enter'")
        while anfrage != '':
            text5 = colored('please enter element to show index: ')
            eingabe4 = input(text5)
            liste.index(eingabe4)
            if eingabe4 == '':
                liste.remove('')
                break
    else:
        exit()