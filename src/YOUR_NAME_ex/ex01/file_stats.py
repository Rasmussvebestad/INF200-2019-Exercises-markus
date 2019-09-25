import numpy as np


def char_counts(textfilename):


    with open(textfilename, 'r', encoding='utf-8') as textfile:
        ordliste = [ord(i) for i in textfile.read()]
        results = np.zeros(256)
        for i in ordliste:
            results[i] += 1
    return results

    pass


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )