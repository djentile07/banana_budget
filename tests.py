import os
import ast

import pytest
import requests

from utils import calculate_cost
from utils import clean_totalcost

base_url = "https://bananabudget.azurewebsites.net"
INVALID_START_DATE = "Invalid startDate"
INVALID_NUMBER_OF_DAYS_MSG = "Invalid numberOfDays"
REQUIRED_PARAMETERS_MSG = "Must provide startDate and numberOfDays"

def test_valid_parameters(start_date, number_of_days):
    number_of_days = int(number_of_days)
    parameters = "?startDate={}&numberOfDays={}"
    parameters = parameters.format(start_date, number_of_days)
    end_point = os.path.join(base_url, parameters)

    expected_cost = calculate_cost(start_date, number_of_days)
    r = requests.get(end_point)
    r_dict = ast.literal_eval(r.text)
    total_cost = clean_totalcost(r_dict['totalCost'])
    assert total_cost == expected_cost

def test_invalid_date():
    start_date = "17-10-12"
    number_of_days = 20
    parameters = "?startDate={}&numberOfDays={}"
    parameters = parameters.format(start_date, number_of_days)
    end_point = os.path.join(base_url, parameters)
    r = requests.get(end_point)
    r_dict = ast.literal_eval(r.text)
    assert r_dict['error'] == INVALID_START_DATE

def test_invalid_number_of_days():
    start_date = "10-12-2017"
    number_of_days = 0
    parameters = "?startDate={}&numberOfDays={}"
    parameters = parameters.format(start_date, number_of_days)
    end_point = os.path.join(base_url, parameters)
    r = requests.get(end_point)
    r_dict = ast.literal_eval(r.text)
    assert r_dict['error'] == INVALID_NUMBER_OF_DAYS_MSG

def test_required_start_date():
    number_of_days = 20
    parameters = "?numberOfDays={}"
    parameters = parameters.format(number_of_days)
    end_point = os.path.join(base_url, parameters)
    r = requests.get(end_point)
    r_dict = ast.literal_eval(r.text)
    assert r_dict['error'] == REQUIRED_PARAMETERS_MSG

def test_required_number_of_days():
    start_date = "10-12-2017"
    parameters = "?startDate={}"
    parameters = parameters.format(start_date)
    end_point = os.path.join(base_url, parameters)
    r = requests.get(end_point)
    r_dict = ast.literal_eval(r.text)
    assert r_dict['error'] == REQUIRED_PARAMETERS_MSG
