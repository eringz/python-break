while True:
    name = input('Who are you? ')
    if name != 'Joe':
        continue
    password = input('Hello, ' + name + '. What is the password? ')
    if password == 'swordfish':
        break
    print('Try again')
print('Access granted')