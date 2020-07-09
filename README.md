# A template for new data analysis pipelines

When starting a new data analysis project, you can use this repository as a template to get you started.
It is a barebones implementation that incorporates all the tips featured in:

[Marijn van Vliet (2020): Seven quick tips for analysis scripts in neuroimaging](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007358)

This template contains a mock analysis pipeline with some mock data:
 * 2 subjects
 * 2 analysis steps (`00_example_step.py` and `01_grand_average.py`)
 * 2 figures (`figure_example1.py` and `figure_grand_average.py`)

## Running the analysis pipeline
1. Download the study template by clicking [here](https://github.com/AaltoImagingLanguage/study_template/archive/master.zip)
1. Extract the downloaded zip file
1. Open a terminal and move into the folder containing the study template
1. Make sure all required python packages are installed by running: `pip install -r requirements.txt`

1. Run the analysis by either:
   * run `doit` to use a build system to run all the analysis steps
   * alternatively, run `python master.py` to use a simple master script to run all the analysis steps
  
After the analysis has been completed:
 * the processed data should be in the `processed/` folder
 * the HTML reports should be in the `reports/` folder
 * the generated figures should be in the `figures/` folder.
 
## Explanation of all the files in this repository

| Filename                | Explanation   |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .gitignore              | Configuration file for Git so it ignores non-code files   
| 00_example_step.py      | The first step of the analysis                                                                                                                                                                       |
| 01_grand_average.py     | The second step of the analysis                                                                                                                                                                      |
| LICENSE                 | BSD 3-clause license. This is the license under which this study template is published.                                                                                                              |
| README.md               | The README document you are currently reading.                                                                                                                                                       |
| check_system.py         | Script that checks whether all required Python packages are installed, whether the data can be found, etc. This is run before the actual analysis starts to catch installation errors.               |
| config.py               | The configuration file that is used by all analysis scripts. It defines all variables shared across scripts. This includes things like filter settings, but also all filenames used in the analysis. |
| dodo.py                 | A version of the master script that is meant to be consumed by the build system "pydoit". Use either this script as master script or use `master.py`.                                                |
| figure_example1.py      | Script that produces the first figure in this analysis.                                                                                                                                              |
| figure_grand_average.py | Script that produces the second figure in this analysis.                                                                                                                                             |
| fnames.py               | Helper class to manage filenames. Used in `config.py` to define all filenames. Used by the analysis scripts for convenient access to the filenames.                                                  |
| master.py               | A plain python version of the master script. Use either this script or `dodo.py` to run the entire analysis.                                                                                         |
| requirements.txt        | A list of python packages required to run the analysis. You can install these with `pip install -r requirements.txt`                                                                                 |

## Getting started with a new data analysis pipeline based on the study template
1. Download the study template by clicking [here](https://github.com/AaltoImagingLanguage/study_template/archive/master.zip)
1. Extract the downloaded zip file

1. Modify `config.py`
   1. Add your system to the list at the top, indicate where your data is, how many cores you have on your machine, etc.
   1. Add all parameters relevant to your analysis to the script
   1. Add all filenames relevant to your analysis to the script

1. Add new scripts for each analysis step and each figure

1. Modify the master script to execute the scripts you have added by either:
   * Add new tasks to the `dodo.py` script to use the `doit` build system to run all the analysis steps. Delete `master.py`.
   * alternatively, add new lines to execute the scripts you have added to the `master.py` file to use a simple master script to run all the analysis steps. Delete `dodo.py`.

1. Modify `requirements.txt`
   1. Add all python packages your analysis pipeline needs
