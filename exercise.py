# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     name = input('Enter a name: (blank to quit) ')
#     if name == '':
#         break
#     if name in birthdays:
#         print('%s is the birthday of %s' % (birthdays[name], name))
#     else:
#         print('I do not have birthday information for %s' % name)
#         bday = input('What is their birthday?: ')
#         birthdays[name] = bday
#         print('Birthday information added.')

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for c in message:
    count.setdefault(c, 0)
    count[c] = count[c] + 1

pprint.pprint(count)
print(pprint.pformat(count))


