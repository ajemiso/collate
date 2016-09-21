import datetime


class IncomeCalc(object):

    def __init__(self, *args, **kwargs):
        #import pdb; pdb.set_trace()

        if kwargs['borrower'][0] == '1':
            self.employer_name = kwargs['b1_employer_name'][0]
            self.start_date = kwargs['b1_hire_date'][0]
            self.income = kwargs['b1_income_amount'][0]
            self.period_end_date = kwargs['b1_period_end_date'][0]
            self.pay_frequency = kwargs['b1_pay_frequency'][0]


        elif kwargs['borrower'][0] == '2':
            self.employer_name = kwargs['b2_employer_name'][0]
            self.start_date = kwargs['b2_hire_date'][0]
            self.income = kwargs['b2_income_amount'][0]
            self.period_end_date = kwargs['b2_period_end_date'][0]
            self.pay_frequency = kwargs['b2_pay_frequency'][0]

        else:
            self.employer_name = None
            self.start_date = None
            self.income = None
            self.period_end_date = None
            self.pay_frequency = None


    def income_calculator(self):
        """
        Calculates monthly income based on pay frequency
        """
        income = self.income
        income = income.replace('$', '')
        income = income.replace(',', '')
        income = float(income)

        if self.pay_frequency == "bi-weekly":
            income = (income * 26) / 12
            return "$%.2f" % income
        elif self.pay_frequency == "semi-monthly":
            income = income * 2
            return "$%.2f" % income
        elif self.pay_frequency == "monthly":
            return "$%.2f" % income
        elif self.pay_frequency == "weekly":
            income = (income * 52) / 12
            return "$%.2f" % income
        else:
            return None


    def create_string(self):
        """
        concatenate income employment string:

        "B1: employed with [employer] for [years], [pay type] pay,
        [dollar amount]/mo, good through [4 months out - date]"
        """
        income_amount = self.income_calculator()


        # convert string to datetime object
        start_date = datetime.datetime.strptime(self.start_date, '%m/%d/%Y')

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
        period_end_date = datetime.datetime.strptime(self.period_end_date, '%m/%d/%Y')
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
                self.employer_name, years_employed, self.pay_frequency, income_amount,
                good_through_date.month, good_through_date.day, good_through_date.year)
