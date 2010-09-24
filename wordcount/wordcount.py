#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""
import sys
import string

def print_top(dic):
        count = 0
        item_dic = dic.items()
        sort_by_key = sorted(item_dic,key = lambda x:x[0])
        sort_by_value = sorted(sort_by_key,key = lambda x:x[1],reverse = True)
        for i in sort_by_value:
                p,q = i
                print p,q
                count += 1
                if(count >= 20):
                        break


def print_words(filename):
        count = 0
        dic = {}
        f = open(filename,'r+')
        read_file = f.read()
        read_file = read_file.lower()
        split_file = read_file.split()
        set_file = set(split_file)
        set_file = list(set_file)
        set_file.sort()
        length = len(set_file)
        for i in range(len(set_file)):
                for j in range(len(split_file)):
                        if(set_file[i] == split_file[j]):
                                count += 1
                dic [set_file[i]] = count
                count = 0
        print_top(dic)

print print_words('/home/ic2010/Aug31/a')
	
# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
