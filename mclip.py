#! python3
# mclip.py - A multi-clipboard program.

import sys
import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [key_phrase] - copy phrase text')
    sys.exit()

key_phrase = sys.argv[1]  # first command line arg is the key_phrase

if key_phrase in TEXT:
    pyperclip.copy(TEXT[key_phrase])
    print('Text for ' + key_phrase + ' copied to clipboard.')
else:
    print('There is no text for ' + key_phrase)
