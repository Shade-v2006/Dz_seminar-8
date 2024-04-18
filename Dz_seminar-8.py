def contactadd():
    phonebook = open('phones.txt', 'a+', encoding='utf-8')
    fio = input('введите имя: ')
    pfonenum = input('введите номер телефона: ')
    comments = input('введите коментарии: ')
    phonebook.writelines(f'{fio},{pfonenum},{comments}\n')
    phonebook.close()
    
def contactsshow():
    phonebook = open('phones.txt', 'r')
    for i in phonebook:
        print(i)
    phonebook.close()
    
def allcontacts():
    with open('phones.txt', 'r+', encoding='utf-8') as phonebook:
        return phonebook.readlines()
    
def contactsfind():
    phonebook = allcontacts()
    findname = input('кого надо найти: ')
    for contacts in phonebook:
        if findname.lower() in contacts.lower():
            print(contacts)
            
def contactschange():
    phonebook = open('phones.txt', 'r+', encoding='utf-8')
    phonechange = phonebook.readlines()
    whoneed = input('Кого хотим исправить: ')
    shortlist = []
    counter = 1
    for contats in phonechange:
            if whoneed.lower() in contats.lower():
                print(f'{counter},{contats}')
                shortlist.append(contats)
                counter += 1
    if shortlist == []:
        notfind = int(input('Контакт не найден!\nПопробуем еще раз?\n1-Да\n2-нет\nВыберите порядковый номер: '))
        if notfind == 1:
            return contactschange()
        else:
            return print('Попробуйте в следующий раз.')
    else:
        if counter > 2:
            rightcontact = int(input('Уточните порядковый номер корректируемого контакта: '))
            if rightcontact >= counter:
                notfind = int(input('Такого варианта нет!\nПопробуем еще раз?\n1-Да\n2-нет\nВыберите порядковый номер: '))
                if notfind == 1:
                    return contactschange()
                else:
                    return print('Попробуйте в следующий раз.')
            else:
                shortlist = shortlist[rightcontact-1]
        whatfind = int(input('Что будем менять:\n1-имя\n2-номер\n3-комментарий\nВведите число: '))
        if whatfind == 1 or whatfind == 2 or whatfind == 3:
            correctcontact = input('Введите новое значение: ')
            newshortlist = shortlist[0].split(',')
            newshortlist[whatfind-1] = correctcontact
            newshortlist = [f'{newshortlist[0]},{newshortlist[1]},{newshortlist[2]}']
            for i in range(len(phonechange)):
                if phonechange[i] == shortlist[0]:
                    if whatfind == 1 or whatfind == 2:
                        phonechange[i] = newshortlist[0]
                    elif whatfind == 3:
                        phonechange[i] = f'{newshortlist[0]}\n'
            phonebook.close()
            phonebook = open('phones.txt', 'w', encoding='utf-8')
            phonebook.writelines(phonechange)
            phonebook.close()
        else:
            notfind = int(input('Такого варианта нет!\nПопробуем еще раз?\n1-Да\n2-нет\nВыберите порядковый номер: '))
            if notfind == 1:
                return contactschange()
            else:
                return print('Попробуйте в следующий раз.')
            
def contactsdel():
    phonebook = open('phones.txt', 'r+', encoding='utf-8')
    phonechange = phonebook.readlines()
    whoneed = input('Кого хотим удалить: ')
    shortlist = []
    counter = 1
    for contats in phonechange:
            if whoneed.lower() in contats.lower():
                print(f'{counter},{contats}')
                shortlist.append(contats)
                counter += 1
    print(shortlist)  
    if shortlist == []:
        notfind = int(input('Контакт не найден!\nПопробуем еще раз?\n1-Да\n2-нет\nВыберите порядковый номер: '))
        if notfind == 1:
            return contactsdel()
        else:
            return print('Попробуйте в следующий раз.')
    else:
        if counter > 2:
            print(shortlist) 
            rightcontact = int(input('Уточните порядковый номер контакта: '))
            if rightcontact >= counter:
                notfind = int(input('Такого варианта нет!\nПопробуем еще раз?\n1-Да\n2-нет\nВыберите порядковый номер: '))
                if notfind == 1:
                    return contactsdel()
                else:
                    return print('Попробуйте в следующий раз.')
            else:
                shortlist = shortlist[rightcontact-1]
                print(rightcontact-1)
                print(shortlist) 
    phonechange = list(filter(lambda x: x != shortlist, phonechange))
    print(phonechange)
    phonebook.close()
    phonebook = open('phones.txt', 'w', encoding='utf-8')
    phonebook.writelines(phonechange)
    phonebook.close()
        
              
    

    
whatdowitcontact = int(input('что Вы хотите сделать:\n1-посмотреть записную книгу\n2-найти контакт\n3-добавить контакт\n4-исправить контакт\n5-удалить контакт\nВыберите порядковый номер: '))
if whatdowitcontact == 1:
    print(*allcontacts(), sep='')
elif whatdowitcontact == 2:
    contactsfind()
elif whatdowitcontact == 3:
    contactadd()
elif whatdowitcontact == 4:
    contactschange()
elif whatdowitcontact == 5:   
    contactsdel() 