__version__ = '0.0.0'
import argparse
import os
import sys

def create_parser():
    parser = argparse.ArgumentParser(description='Konstable command line interface')
    parser.add_argument('-v', '--version', dest='version', action='store_true',
                        help="""Current Konstable Version""")

    return parser.parse_args()

def main():
    print('Konstable running in ', os.getcwd())
    args = create_parser()
    if args.version:
        print('Version:', __version__)
        sys.exit()

def hello():
    return 'world'