"""
One master script to call them all.
"""
import subprocess
import sys
import os
from config import subjects


def call(script, *params):
    """Call a script and exit if the script failed."""
    print('\n---- Running %s %s ----\n' % (script, ' '.join(params)))
    return_code = subprocess.call(['python', script] + list(params))
    if return_code != 0:
        # Something went wrong when executing the script. Drop everything and
        # exit the master script.
        sys.exit(return_code)


# First, check if everything is in order with the system.
if not os.path.exists('system_check.txt'):
    call('check_system.py')

# Do all analysis steps for all subjects
for subject in subjects:
    call('00_example_step.py', subject)

# Call a script that aggregates over all subjects
call('01_grand_average.py')

# Do all the figures
call('figure_example1.py')
call('figure_grand_average.py')
