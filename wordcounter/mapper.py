import string
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    line = line.translate(str.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
        print('%s\t%s' % (word, 1))
