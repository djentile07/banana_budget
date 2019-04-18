# Python and dependencies installation

The following steps assume that python 3 is already installed on your computer.

1. Install virtualenv by running command **pip install virtualenv**
2. Create a virtual environment and activate it
3. Install python dependencies by running command **pip -r install requirements.txt**

# Running the tests

Run the tests as follows:

**pytest  -s  --start_date=<START_DATE> --number_of_days=<NUMBER_OF_DAYS>**

where START_DATE and NUMBER_OF_DAYS are respectively a valid start date and a valid number of days.

e.g **pytest -s --start_date=10-12-2017 --number_of_days=30**

All tests in the tests.py file should run.

