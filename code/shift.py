"""
Caesar cipher solver by Daniel Chatfield

"""

from collections import Counter
from heapq import heappush, nsmallest

EN_DIST = {
    "A": 8.167,
    "B": 1.492,
    "C": 2.782,
    "D": 4.253,
    "E": 12.70,
    "F": 2.228,
    "G": 2.015,
    "H": 6.094,
    "I": 6.966,
    "J": 0.153,
    "K": 0.772,
    "L": 4.025,
    "M": 2.406,
    "N": 6.749,
    "O": 7.507,
    "P": 1.929,
    "Q": 0.095,
    "R": 5.987,
    "S": 6.327,
    "T": 9.056,
    "U": 2.758,
    "V": 0.978,
    "W": 2.361,
    "X": 0.150,
    "Y": 1.974,
    "Z": 0.074,
}


def char_to_int(char):
    char = char.upper()

    value = ord(char) - 65
    if -1 < value < 26:
        return value

    raise ValueError("The char '%s' is not in A-Z" % char)


def int_to_char(value):
    return chr(value + 65)


def solve_caesar(ciphertext):
    c = Caesar(ciphertext=ciphertext)

    return c.solve()


def score_plaintext(plaintext):
    plaintext = ''.join(c for c in plaintext if c.isupper())
    counter = Counter(plaintext)

    total_diff = 0
    max_diff = 0

    for letter in EN_DIST:
        target = EN_DIST[letter]
        actual = 100.0 * counter[letter] / len(plaintext)

        diff = (target - actual) ** 2
        total_diff += diff

        if diff > max_diff:
            max_diff = diff

    return total_diff - max_diff


class Caesar():
    def __init__(self, ciphertext=None, offset=None):
        self.ciphertext = ciphertext
        self.offset = offset

    def decrypt(self, offset=None):
        output = ''

        if offset is None:
            offset = self.offset

        assert offset is not None

        for char in self.ciphertext:
            try:
                integer = char_to_int(char)
                integer -= offset
                output += int_to_char(integer % 26)
            except ValueError:
                output += char

        return output

    def solve(self, limit=1):
        # Try each offset and return best decodings

        h = []

        for i in xrange(26):
            plaintext = self.decrypt(i)
            score = score_plaintext(plaintext)

            heappush(h, (score, plaintext))

        return nsmallest(limit, h)

if __name__ == '__main__':
    ciphertext = "LUXDZNUAMNDODJUDTUZDGYQDLUXDGOJDCKDTKKJDOZ"

    c = Caesar(ciphertext)

    solutions = c.solve(5)

    print "Found the following possible solutions:\n"

    for sol in solutions:
        print "(%d) %s" % sol
