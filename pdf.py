import sys
from utility import help_print
from pdf_merge import merge

if __name__ == '__main__':
    arguments = sys.argv
    if len(arguments) <2:
      help_print()

    command = arguments[1]

    if command == "merge":
      merge(arguments[:])


    pass