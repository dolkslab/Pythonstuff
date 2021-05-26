import sys
import re

keys = {
    'a': 'aegisa',
    'b': 'csgob',
    'c': 'CB_em',
    'd': 'TheD',
    'e': 'letter_E',
    'f': 'fraud',
    'g': 'gmod',
    'h': 'hyperion',
    'i': 'tobinfo',
    'j': 'jcoin',
    'k': '_K_',
    'l': 'and_bone',
    'm': 'lemmam',
    'n': 'nitrogen',
    'o': 'p2aperture',
    'p': 'letterp',
    'q': 'odrown',
    'r': 'rdlogo',
    's': 'salvagebits',
    't': 'TR_T',
    'u': 'qube2magnet',
    'v': 'SFvictory',
    'w': 'comicw',
    'x': 'pinball_close',
    'y': 'Y',
    'z': 'NZA2_Zed',
    '!': 'Refrain_exclamation' 
}

out = ""

for c in sys.argv[1]:
    if c == ' ':
        out += "   "
    elif c.isalpha() or re.search("[!]",c):
        out += ":" + keys[c.lower()] + ":"

    else:
        out += c

print(out)
