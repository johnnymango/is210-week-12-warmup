#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """This class logs errors."""

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Creates the log"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Processes the file"""
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log = 'Can not open file.'
            raise IOError('Can not open file.')

        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except IOError:
            self.log = 'Write File Error.'
        finally:
            fhandler.close()

        for index in handled[::-1]:
            if IOError:
                raise IOError
            else:
                del self.msgs[index]
