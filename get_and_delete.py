#!/usr/bin/python3
from sys import argv, stderr
from random import randint
from time import sleep

# DEFAULT = ''
DEFAULT = 'http://clist.by/'

contents = []
try:
    with open(argv[1], 'r') as f:
        contents = f.read().splitlines()
except FileNotFoundError:
    stderr.write('provide the existent newline-separated list as the only argument.\n')
except IndexError:
    stderr.write('provide the existent newline-separated list as the only argument.\n')
    
    
EXITCODE = 0
if len(contents) == 0:
    stderr.write('your list is empty.\n')
    if DEFAULT != '':
        stderr.write('defaulting to {default}\n'.format(default=DEFAULT))
        contents.append(DEFAULT)
        EXITCODE = 2
    else:
        stderr.write('tip: set DEFAULT next time.\n')
        exit(4)
        
chosen = randint(1, len(contents)) - 1
print(contents.pop(chosen))

try:
    with open(argv[1], 'w') as f:
        f.write('\n'.join(contents))
except IndexError:
    pass
except: # try again
    while True:
        try:
            sleep(1)
            with open(argv[1], 'w') as f:
                f.write('\n'.join(contents))
        except:
            pass

exit(EXITCODE)
