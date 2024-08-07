'''
    Write a function that take a list as an argument 
    Returns a string with all the items separated by a comma and a space, 
        with and inserted before the last item.
    Should be able to work with any list value passed to it.
    Should also test empty string 
'''


def toString(list):
    if len(list) == 0:
        return 'Empty List'
    elif len(list) == 1:
        return list[0] + ' only on the list'
    else:
        result = ''
        for i in range(len(list) - 1):
            result += list[i] + ', '
        result += 'and ' + list[-1]
        return result

# Example as default
spam = ['apples', 'bananas', 'tofu', 'cats']

# Example of only 1 item on list
maling = ['maling']

# Empty list example
bacon = []



print(toString(bacon))
print(toString(maling))
print(toString(spam))

