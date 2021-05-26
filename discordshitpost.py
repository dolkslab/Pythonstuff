import sys

keys = {
    'a': 'a',
    'b': 'b',
    'c': 'regional_indicator_c',
    'd': 'regional_indicator_d',
    'e': 'regional_indicator_e',
    'f': 'regional_indicator_f',
    'g': 'regional_indicator_g',
    'h': 'regional_indicator_h',
    'i': 'regional_indicator_i',
    'j': 'regional_indicator_j',
    'k': 'regional_indicator_k',
    'l': 'regional_indicator_l',
    'm': 'regional_indicator_m',
    'n': 'regional_indicator_n',
    'o': 'o2',
    'p': 'parking',
    'q': 'regional_indicator_q',
    'r': 'regional_indicator_r',
    's': 'regional_indicator_s',
    't': 'regional_indicator_t',
    'u': 'regional_indicator_u',
    'v': 'regional_indicator_v',
    'w': 'regional_indicator_w',
    'x': 'regional_indicator_x',
    'y': 'regional_indicator_y',
    'z': 'regional_indicator_z',
    '?': 'question'
}

out = ""

for c in sys.argv[1]:
    if c == ' ':
        out += " "
    elif c.isalpha():
        out += ":" + keys[c.lower()] + ": "
    else:
        out += c


print(out)
