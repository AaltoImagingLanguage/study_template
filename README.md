# A template for new data analysis pipelines

When starting a new data analysis project, you can use this repository as a template to get you started.
It is a barebones implementation that incorporates all the tips featured in:

[Marijn van Vliet (2019): Guidelines for data analysis scripts](https://arxiv.org/abs/1904.06163)

This template contains a mock analysis pipeline with:
 * 2 subjects
 * 2 analysis steps
 * 2 figures

## Running the mock analysis pipeline
* Clone this repository
* Move into the folder
* Make sure all required python packages are installed by running: `pip install -r requirements.txt`
* Run `doit`

## Getting started with a new data analysis pipeline
* Modify `requirements.txt`
  * Add all python packages your analysis pipeline needs
* Modify `config.py`
  * Add your system to the list, indication where your data is, how many cores you have on your machine, etc.
  * Add all parameters relevant to your analysis to the script
  * Add all filenames relevant to your analysis to the script
* Modify `dodo.py`
  * Add tasks for all analysis steps
* Add new scripts for each analysis step and each figure
