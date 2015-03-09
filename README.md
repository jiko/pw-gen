# A humble password generator

To use open a terminal in this directory and run:

`python pw-gen.py shakespeare.txt`

If you want to make a password from a different text, you can replace `shakespeare.txt` with any plain text file.

A brief explanation of what the script does:

1. Read a small chunk of the file, default 35 characters
2. Break that chunk into words
3. Capitalize the first word
4. Translate the last word into a subset of 1337 5p34k (only `a`, `e`, and `o` in this case)
5. Join all words into one using a separator character, default `-`

The 1337 translation table, chunk size, and separator character get assigned towards the beginning of the file, if you want to customize those variables.
