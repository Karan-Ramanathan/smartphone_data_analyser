# Smartphone Data Analyser

## Requirements

For running the script to generate structured data for analysis, you will need the following:

- An IDE - Preferably [Pycharm](https://www.jetbrains.com/pycharm/download/) or [Visual Studio Code](https://www.jetbrains.com/pycharm/download/)
- Python 3 or above

## Setting up dependencies

- Clone the `smartphone_data_analyser` github repository to your computer.
- In a terminal, navigate to the location where you have cloned this repository.
- We will create a Virtual Environment that only installs dependencies required to run this project.
- Run the commands mentioned [here](https://docs.python.org/3/library/venv.html#module-venv) to setup and activate your virtual environment.
- To check if virtual environment has been activated, check if `.venv` appears in front of the command prompt.
- Once the virtual environment has been activated, we will install the packages defined in `requirements.txt` in this project by running:
```
pip install -r requirements.txt
```

- All the dependencies required to run the script have now been setup

## Running the script

- To run the project, simply run the command:
```
python3 clean_data.py
```

## What happens on running the script

- On running the `clean_data.py` script, the script looks at data defined in various text files like `X-train.py`, `Y-train.py` and `features.txt`.
- To understand how these files are related to each other, read the `README.txt` file attached in this repository.
- This script consolidates data defined in those files into a single file in the same directory called - `clean_train_data.csv` containing 561 columns and 7532 rows.
- Out of these 561 columns containing information about different vectors and features, we retain only 119 columns contaning magnitude information in them as well as the activity and subject for each record.
- This has been done to facilitate easier visualisation of data in the csv file.
