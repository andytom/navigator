from __future__ import print_function
from functools import wraps
import sys
# TODO - Add doc strings


#-----------------------------------------------------------------------------#
def catch_exit_keys(f):
    """Catch Ctrl-c and Ctrl-d and exit cleanly"""
    @wraps(f)
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except KeyboardInterrupt:
            print()
            sys.exit(0)
        except EOFError:
            print()
            sys.exit(0)
    return wrapped
