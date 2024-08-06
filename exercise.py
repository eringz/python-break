def spam(eggs):
    print('1: ' + eggs)
    eggs = 'spam local'
    print('2: ' + eggs)

eggs = 'global'

spam(eggs)