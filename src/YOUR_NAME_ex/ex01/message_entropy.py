import collections
import math as m


def letter_freq(txt):
    streng = txt.lower()
    streng = ''.join(sorted(streng))
    tekst = collections.OrderedDict()

    for symbol in streng:
        if symbol in tekst:
            tekst[symbol] += 1
        else:
            tekst[symbol] = 1
    return tekst


def entropy(text):
    tekst = letter_freq(text)
    dict_keys = list(tekst.values())
    n = len(text)
    totalt = 0

    for i in range(len(dict_keys)):
        totalt += -((dict_keys[i] / n) * m.log2(dict_keys[i] / n))

    return totalt


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
