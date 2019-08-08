"""
Do-it script to execute the entire pipeline using the doit tool:
http://pydoit.org

All the filenames are defined in config.py
"""
from config import fname, subjects

# Configuration for the "doit" tool.
DOIT_CONFIG = dict(
    # While running scripts, output everything the script is printing to the
    # screen.
    verbosity=2,

    # When the user executes "doit list", list the tasks in the order they are
    # defined in this file, instead of alphabetically.
    sort='definition',
)


def task_check():
    """Check the system dependencies."""
    return dict(
        file_dep=['check_system.py'],
        targets=[fname.system_check],
        actions=['python check_system.py']
    )


# This example task executes a single analysis script for each subject, giving
# the subject as a command line parameter to the script.
def task_example_step():
    """Step 00: An example analysis step that is executed for each subject."""
    # Run the example script for each subject in a sub-task.
    for subject in subjects:
        yield dict(
            # This task should come after `task_check`
            task_dep=['check'],

            # A name for the sub-task: set to the name of the subject
            name=subject,

            # If any of these files change, the script needs to be re-run. Make
            # sure that the script itself is part of this list!
            file_dep=[fname.input(subject=subject), '00_example_step.py'],

            # The files produced by the script
            targets=[fname.output(subject=subject)],

            # How the script needs to be called. Here we indicate it should
            # have one command line parameter: the name of the subject.
            actions=['python 00_example_step.py %s' % subject],
        )


# Here is another example task that averages across subjects.
def task_example_summary():
    """Step 01: Average across subjects."""
    return dict(
        task_dep=['example_step'],  # This task should come after `task_example_step`
        file_dep=[fname.output(subject=s) for s in subjects] + ['01_grand_average.py'],
        targets=[fname.grand_average],
        actions=['python 01_grand_average.py'],
    )


def task_figures():
    """Make all figures. Each figure is a sub-task."""
    # Make figure 1
    yield dict(
        name='figure_example1',
        file_dep=['figure_example1.py'],
        targets=[fname.figure1],
        actions=['python figure_example1.py'],
    )

    # Make figure 2
    yield dict(
        name='figure_grand_average',
        file_dep=[fname.grand_average, 'figure_grand_average.py'],
        targets=[fname.figure_grand_average],
        actions=['python figure_grand_average.py'],
    )
