import sys


from warcio.archiveiterator import ArchiveIterator

filename = sys.argv[1]

with open(filename, 'rb') as stream:
    for record in ArchiveIterator(stream):
        print(record.rec_type)
        # print(dir(record))
        # e
