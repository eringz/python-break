'''
    #! python3
    # bulletPointAdder.py - Adds Wikipedia bullet points to the start
    # of each line of text on the clipboard.

    Lists of animals
    Lists of aquarium life
    Lists of biologists by author abbreviation
    Lists of cultivars
'''
import pyperclip

text = pyperclip.paste()

# TODO: Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* %s' % lines[i]

text = '\n'.join(lines)

print(text)