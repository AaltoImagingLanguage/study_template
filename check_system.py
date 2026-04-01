"""System checker.

This script performs a series of checks on the system to see if everything is
ready to run the analysis pipeline.
"""

import importlib
import os
import re
from pathlib import Path

import mne

from config import fname

# Check to see if the python dependencies are fullfilled.
dependencies = Path("requirements.txt").read_text().split()

print("Checking dependencies:")
missing = list()
for dep_string in dependencies:
    # Convert the dependency string in the TOML file to a plain python package name.
    package_name = re.split(r"[<>=!~\[]", dep_string)[0].replace("-", "_").strip()

    try:
        mod = importlib.import_module(package_name)
        print(f"├☑ {package_name:<21}", end="")
        if hasattr(mod, "__version__"):
            print(mod.__version__)
        else:
            print()
    except ImportError:
        print(f"├☐ {package_name:<21}")
        missing.append(package_name)
print()

# Raise an error if dependencies are not met
if len(missing) > 0:
    raise ImportError(f"Missing dependencies: {' '.join(missing)}")

# Check that the data is present on the system
if not os.path.exists(fname.raw_data_dir):
    raise ValueError(
        "The `raw_data_dir` points to a directory that does not exist: "
        + fname.raw_data_dir
    )

# Prints some information about the system
mne.sys_info()

with open(fname.system_check, "w") as f:
    f.write("System check OK.")

print(
    "\nAll seems to be in order.\n"
    "You can now run the entire pipeline with: python -m doit"
)
