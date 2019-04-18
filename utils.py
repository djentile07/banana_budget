import datetime

def calculate_cost(startDate, numberOfDays):
    """
    Calculates the budget needed to purchase bananas
    :param startDate: The start date in the format MM/DD/YYY
    :param numberOfDays: The number of days (min: 1, max:365)
    """
    total_cost = 0
    day_count = 0
    start_date = datetime.datetime.strptime(startDate, '%m-%d-%Y')
    while day_count < numberOfDays:
        date = start_date + datetime.timedelta(days=day_count)
        if date.weekday() != 5 and date.weekday() != 6:
            day = date.day
            if day <= 7:
                total_cost += 0.05
            elif day <= 14:
                total_cost += 0.1
            elif day <= 21:
                total_cost += 0.15
            elif day <= 28:
                total_cost += 0.2
            else:
                total_cost += 0.25
        day_count += 1
    return round(float(total_cost), 2)

def clean_totalcost(total_cost):
    total_cost = total_cost.replace("$", "")
    return float(total_cost)
