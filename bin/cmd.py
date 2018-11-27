#!/bin/python

import subprocess

#Two ways of running commands that are not intended for Python.  See lines 6 and 7.
try:
    #code = subprocess.call(['ls', '-l'])
    output = subprocess.check_output('ls reverse-file', stderr=subprocess.STDOUT)
except OSError as err:
    print("Caught OSError")
    output = err
except subprocess.CalledProcessError as err:
    print("Caught CalledProcessError")
    output = err
print(output)

#if code == 0:
#    print("command finished successfully")
#else:
#    print("failed with code: %i" % code)