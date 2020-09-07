import collections, datetime, functools, itertools
import json, logging, pathlib, random, re
import argparse
import secrets
from logging import DEBUG, INFO, WARNING, ERROR, FATAL

SILENT = 0

log = logging.getLogger(__name__)


def main():

    frontend()


ALL_SETS = frozenset("bdlsum")


def chars_string(s):

    letters = set(s)

    for letter in letters:

        if letter not in ALL_SETS:

            raise ValueError(
                "'{letter}' not a valid character set. Compose a string using only '{all_sets'".format(
                    letter=letter, all_sets=ALL_SETS
                )
            )

    return letters


def add_set(current, extra):

    return current.union(extra)


add_lowercase = functools.partial(add_set, extra="abcdefghijklmnopqrstuvwxyz")
add_uppercase = functools.partial(add_set, extra="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
add_digits = functools.partial(add_set, extra="0123456789")
add_basic_symbols = functools.partial(add_set, extra="!?#$&*@")
add_more_symbols = functools.partial(add_set, extra="%()+-=[]{}|~.,")

similar = "0OoIl1"


def remove_similar(current):

    return current.difference(similar)


def gen_password(
    length,
    lowercase=False,
    uppercase=False,
    digits=False,
    basic_symbols=False,
    more_symbols=False,
    skip_similar=False,
):

    charset = set()

    flags = (lowercase, uppercase, digits, basic_symbols, more_symbols, skip_similar)

    set_functions = (
        add_lowercase,
        add_uppercase,
        add_digits,
        add_basic_symbols,
        add_more_symbols,
        remove_similar,
    )

    for modifier in (modifier for flag, modifier in zip(flags, set_functions) if flag):

        charset = modifier(charset)

    charset = tuple(charset)

    password = "".join(secrets.choice(charset) for i in range(length))

    return password


char2flag = {
    "l": "lowercase",
    "u": "uppercase",
    "d": "digits",
    "b": "basic_symbols",
    "m": "more_symbols",
    "s": "skip_similar",
}


def frontend():

    parser = argparse.ArgumentParser(
        description="Generate passwords",
        epilog="""
l - Use [L]owercase Letters abcdefghijklmnopqrstuvwxyz
d - Use [D]igits 0123456789
u - Use [U]ppercase Letters ABCDEFGHIJKLMNOPQRSTUVWXYZ
b - Use [B]asic Symbols !?#$&*@
m - Use [M]ore Symbols %()+-=[]{}|~.,
s - [S]kip Similar Looking Characters 0OoIl1
""",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "-c",
        "--chars",
        default="ldubms",
        type=chars_string,
        help="a string of character sets. Default: ldubms",
    )

    parser.add_argument(
        "password_length", type=int, default=32, nargs="?", help="Password length"
    )

    args = parser.parse_args()

    flags = {char2flag[x]: True for x in args.chars}

    out = gen_password(length=args.password_length, **flags)

    print(out)


if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="%(asctime)s %(levelname)-4s %(name)s %(message)s",
        style="%",
    )

    main()
