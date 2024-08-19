import pyperclip

text = pyperclip.paste()

# TODO: Seperate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

print(lines)


pyperclip.copy(text)