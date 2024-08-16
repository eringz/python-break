#! python3
# mclip.py - A multi-clipboard program.


TEXT = {
    'aggree': """Yes, I aggree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you conside making this a monthly donation?""",
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] #first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for %s copied to clipboard' % keyphrase)
else:
    print('There is no text for %s' % keyphrase)