import sys, pyperclip

TEXT = {
    'youtube': 'https://www.youtube.com/watch?v=t8OZPJfpcTM',
    'anime': 'www.9animetv.to',
    'kdrama': 'https://dramacool.sh/your-honor-2018-episode-5/',
   
}

if len(sys.argv) < 2:
    print('Usage: mclip.py [keyPhrase] - website to visit')
    sys.exit()
    
keyPhrase = sys.argv[1]

if keyPhrase in TEXT:
    pyperclip.copy(TEXT[keyPhrase])
    print('you can paste it now on web browser')
else:
    print('There is no text for %s' % keyPhrase)
    
