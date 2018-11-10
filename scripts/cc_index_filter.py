import sys


filename = sys.argv[1]
indexfile = filename + '.idx'
ifh = open(indexfile, 'w')

host = ''

def get_cc_index(domain):
    url = f'{host}'


with open(filename) as fh:
    for domain in fh:
        ccindex = get_cc_index(domain)
