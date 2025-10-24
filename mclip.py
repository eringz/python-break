import sys, pyperclip

TEXT = {
    'youtube': 'https://www.youtube.com/watch?v=t8OZPJfpcTM',
    'anime': 'www.9animetv.to',
    'kdrama': 'https://dramacool.sh/your-honor-2018-episode-5/',
    'secret': 'https://www.pornhub.com/view_video.php?viewkey=66b3693ad8f2a',
    'online': 'https://onlinehelpers.info/online-installation-technician/',
    'jealous': 'https://www.youtube.com/watch?v=5O0YDHiosD0',
    'korean-lesson': 'https://www.youtube.com/@JOSHUACHOPH'
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
    
