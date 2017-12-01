#! /usr/bin/env python

import os

from . import autoComplete

if os.environ.get('LC_CTYPE', '') == 'UTF-8':
    os.environ['LC_CTYPE'] = 'en_US.UTF-8'


def complete():
    cline = os.environ.get('COMP_LINE') or os.environ.get('COMMAND_LINE') or ''
    cpoint = int(os.environ.get('COMP_POINT') or len(cline))
    try:
        autoComplete.complete(cline, cpoint)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    complete()
