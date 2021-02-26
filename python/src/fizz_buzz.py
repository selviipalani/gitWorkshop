# lib imports
import logging
import sys

def fizz_buzz(limit):
    """
    FizzBuzz function
            Parameters:
                    limit (int): upper bound for our fizzbuzz

            Returns:
                    three, five, fifteen  ([int]): Array of number modulo by 3,
                    5, and or 15

    """
    three, five, fifteen = [], [], []
    # TODO HELP ME!!
    return three, five, fifteen


def main():
    """
    Entrypoint for fizz_buzz.py 
    Get command line args, if none 
    run fizz_buzz to a default value
    """
    n = len(sys.argv)
    three, five, fifteen = [], [], []
    if n == 1:
        three, five, fifteen = fizz_buzz(1000)
    elif n > 2:
        logging.warning("Usage: python fizz_buzz.py <int>")
        logging.error("Too many arguments only one allowed")
    else:
        up_lim = int(sys.argv[1])
        if up_lim <= 0:
            logging.error("Please input a non negative non zero value")
            sys.exit()
        three, five, fifteen = fizz_buzz(up_lim)
    print(len(three), len(five), len(fifteen))

if __name__ == '__main__':
    main()
