from argparse import ArgumentParser
from random import randint
from os import stat
from string import maketrans

leet = maketrans('aoe','403') # make translation table
sep = "-" # character to use to separate words
chunk_size = 35 # number of consecutive characters to read from file

parser = ArgumentParser()
parser.add_argument("filename", help="name of the file to use to generate a password")
args = parser.parse_args()

file_size = stat(args.filename).st_size
random_point = randint(0, file_size - chunk_size)
with open(args.filename, 'r') as f:
    f.seek(random_point)
    chunk = f.read(chunk_size)
    parts = chunk.split()
    phrase = parts[1:len(parts)-1]
    pw = phrase[0].title() + sep
    pw += sep.join(phrase[1:-1])
    pw += sep + phrase[-1].translate(leet)
    print(pw)
