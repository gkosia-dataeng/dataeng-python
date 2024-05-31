""" Create help functionality and receive arguments
Usage:
    system_Receive_Arguments.py  --date=<date>
    system_Receive_Arguments.py (-h | --help)

Options:
    -h --help         Show this screen. 
"""

from docopt import docopt




if __name__ == '__main__':

    args = docopt(__doc__)
    date = args['--date']
    print(f"Passed date {date}")

