#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import argparse
    args = len(sys.argv) - 1
    if args == 0:
        print("{:d} arguments.".format(args))
    elif args == 1:
        print("{:d} argument:".format(args))
    else:
        print("{:d} arguments:".format(args))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
