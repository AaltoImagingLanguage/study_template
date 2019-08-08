# A template for new data analysis pipelines

When starting a new data analysis project, you can use this repository as a template to get you started.
It is a barebones implementation that incorporates all the tips featured in:

[Marijn van Vliet (2019): Guidelines for data analysis scripts](https://arxiv.org/abs/1904.06163)

This template contains a mock analysis pipeline with:
 * 2 subjects
 * 2 analysis steps
 * 2 figures

## Running the analysis pipeline
* Download the study template by clicking [here](https://github.com/AaltoImagingLanguage/study_template/archive/master.zip)
* Extract the downloaded zip file
* Open a terminal and move into the folder containing the study template
* Make sure all required python packages are installed by running: `pip install -r requirements.txt`
* Run the analysis by either:
  * run `doit` to use a build system to run all the analysis steps
  * alternatively, run `python master.py` to use a simple master script to run all the analysis steps
  
After the analysis has been completed, te processed data should be in the `processed/` folder, the HTML reports should be in the `reports/` folder and the generated figures should be in the `figures/` folder.

## Getting started with a new data analysis pipeline based on the study template
* Download the study template by clicking [here](https://github.com/AaltoImagingLanguage/study_template/archive/master.zip)
* Extract the downloaded zip file
* Modify `config.py`
  * Add your system to the list, indication where your data is, how many cores you have on your machine, etc.
  * Add all parameters relevant to your analysis to the script
  * Add all filenames relevant to your analysis to the script
* Add new scripts for each analysis step and each figure
* Modify the master script to execute the scripts you have added by either:
  * Add new tasks to the `dodo.py` script to use the `doit` build system to run all the analysis steps
  * alternatively, add new lines to execute the scripts you have added to the `master.py` file to use a simple master script to run all the analysis steps
* Modify `requirements.txt`
  * Add all python packages your analysis pipeline needs
