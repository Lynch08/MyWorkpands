while True:
    print ('Who are you?')
    name = input()
    if name != 'Enda':
        continue
    print ('Hi Enda. What is the Password? (is it a fish?'))
    password = input()
    if password == 'swordfish':
        break
print ('Access Granted')
