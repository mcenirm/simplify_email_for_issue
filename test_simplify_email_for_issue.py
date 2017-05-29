#!/usr/bin/env python

import io
import os
import unittest

from simplify_email_for_issue import *


def load_input_and_expected(message_name):
    messages = []
    for ext in ['input', 'expected']:
        file_name = '.'.join([message_name, ext])
        file_path = os.path.join('testdata', file_name)
        with open(file_path) as f:
            message = f.read()
            messages.append(message)
    return tuple(messages)


class Tests(unittest.TestCase):
    def test_one(self):
        self.x('one')

    def x(self, name):
        input, expected = load_input_and_expected(name)
        message = simplify_email_from_file(io.StringIO(input))
        result = message.as_string()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
