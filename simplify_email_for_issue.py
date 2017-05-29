#!/usr/bin/env python

import argparse
import email
import sys


HEADERS_TO_KEEP = frozenset([_.lower() for _ in [
    'From',
    'Date',
    'To',
    'Message-ID',
    'Subject',
]])


def simplify_email_from_file(f):
    '''
    Simplify an email message so it is suitable for adding
    as a comment to an issue.
    '''

    message = email.message_from_file(f)
    before = set(message.keys())
    to_be_removed = [
        _ for _ in message if _.lower() not in HEADERS_TO_KEEP
    ]
    for x in to_be_removed:
        del message[x]
    after = set(message.keys())
    return message


def main():
    arguments = parse_arguments()
    message = simplify_email_from_file(sys.stdin)
    print(message)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description=simplify_email_from_file.__doc__,
    )
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    sys.exit(main())
