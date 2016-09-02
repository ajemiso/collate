import datetime

b1_income_info = {
                'employer_name': 'Intel',
                'start_date': '04/13/2008',
                'income_amount': '$40,000',
                'period_end_date': '11/01/2016',
                'pay_frequency': 'semi-monthly'
                }

b2_income_info = {
                'employer_name': 'Hewlett Packard',
                'start_date': '02/23/2011',
                'income_amount': '$60,000',
                'period_end_date': '11/15/2016',
                'pay_frequency': 'semi-monthly'
                }


def income_calculator(income, pay_frequency):
    """
    Calculates monthly income based on pay frequency
    """
    income = income.replace('$', '')
    income = income.replace(',', '')
    income = int(income)

    if pay_frequency == "bi-weekly":
        return (income * 26) / 12
    elif pay_frequency == "semi-monthly":
        return income * 2
    elif pay_frequency == "monthly":
        return income
    elif pay_frequency == "weekly":
        return (income * 52) / 12
    return None


def create_string(income):
    """
    concatenate income employment string:

    "B1: employed with [employer] for [years], [pay type] pay,
    [dollar amount]/mo, good through [4 months out - date]"
    """

    employer_name = income['employer_name']
    start_date = income['start_date']
    income_amount = income_calculator(income['income_amount'], income['pay_frequency'])
    period_end_date = income['period_end_date']
    pay_frequency = income['pay_frequency']

    # convert string to datetime object
    start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y')

    # extract year integer from datetime object
    year = start_date.year

    # get current year
    current_year = datetime.datetime.now()
    current_year = current_year.year

    # get number of years employed
    years_employed = current_year - year

    # if less than a year, modify string output
    if years_employed >= 1:
        years_employed = "{} years".format(years_employed)
    elif years_employed < 1:
        years_employed = "less than one year"

    # add 4 months to period ending datetime
    period_end_date = datetime.datetime.strptime(period_end_date, '%m/%d/%Y')
    try:
        good_through_date = datetime.date(period_end_date.year,
                                          period_end_date.month+3,
                                          period_end_date.day)
    except ValueError:
        month = period_end_date.month
        # month plus three minus 12
        month = (month + 3) - 12
        good_through_date = datetime.date(period_end_date.year,
                                          month,
                                          period_end_date.day)

    return "B1: employed with {} for {}, {} pay, {}/mo, good through {}/{}/{}".format(
            employer_name, years_employed, pay_frequency, income_amount,
            good_through_date.month, good_through_date.day, good_through_date.year)

print(create_string(b1_income_info))
