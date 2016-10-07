from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from submittals.models import Person, Submittal


class TestApp(TestCase):

    def setUp(self):

        self.good_user = User.objects.create(username="test", password="password123", first_name="Andre",
                                             last_name="Jemison")
        self.good_person = Person.objects.create(user=self.good_user)
        self.good_submittal = Submittal.objects.create(
                                loan_number=10938475,
                                account_type='EQ',
                                loan_officer='Loan Officer',
                                loan_processor=self.good_person,
                                loan_story='Needs a car. Bad.',

                                b1_first_name='Sam',
                                b1_last_name='Wallace',

                                b2_first_name='Sue',
                                b2_last_name='Hankinsonson',

                                b1_employer_name="Blimpie's Subs & Salads",
                                b2_employer_name="Subway",

                                b1_hire_date='09/12/1987',
                                b2_hire_date='3/06/2011',

                                b1_income_amount=1723.72,
                                b2_income_amount=2431.64,

                                b1_pay_frequency='SM',
                                b2_pay_frequency='BW',

                                b1_period_end_date='10/01/2016',
                                b2_period_end_date='09/30/2016',

                                b1_income_output='B1: employed at blah blah blah blah blah blah blah',
                                b2_income_output='B2: employed at blah blah blah blah blah blah blah',

        )

    def test_lookup(self):
        """ test query to locate created person and created submittal """
        person = Person.objects.get(user=self.good_user)
        submittal = Submittal.objects.get(loan_number=10938475)
        self.assertEqual(person.user.first_name, "Andre")
        self.assertEqual(submittal.loan_number, 10938475)

    def test_show_income(self):
        """ test query to ensure income field in database saves as float """
        submittal = Submittal.objects.get(loan_number=10938475)
        self.assertEqual(submittal.b1_income_amount, 1723.72)
