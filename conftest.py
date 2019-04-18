import pytest

def pytest_addoption(parser):
    parser.addoption("--start_date",
                     action="store",
                     default=None,
                     help="Start date in format MM/DD/YYYY"
    )
    parser.addoption("--number_of_days",
                     action="store",
                     default=None,
                     help="Number of days (min: 1, max: 365)"
    )

@pytest.fixture
def start_date(request):
    return request.config.getoption("--start_date")

@pytest.fixture
def number_of_days(request):
    return request.config.getoption("--number_of_days")
