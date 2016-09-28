from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User)
    joined_at = models.DateTimeField(auto_now=True)

    #def __str__(self):
        #return "{0.user}".format(self)

    #def __repr__(self):
    #return "{0.__class__.__name__}({0.user})".format(self)

class Submittal(models.Model):
    ACCOUNT_TYPES = (
        ('EQ', 'Equity Line of Credit'),
        ('EL', 'Equity Loan'),
    )

    PAY_TYPES = (
        ('BW', 'Bi-Weekly'),
        ('SM', 'Semi-Monthly'),
        ('MO', 'Monthly'),
        ('WK', 'Weekly'),
    )

    EMAIL_TEMPLATE_TYPES = (
        ('IN', 'Initial Contact - Email'),
        ('PR', 'Processor Submit - Email'),
        ('IA', 'Initial Approval - Email'),
        ('FN', 'Final Approval - Email'),
    )

    SMS_TEMPLATE_TYPES = (
        ('IN', 'Initial Contact - SMS'),
        ('PR', 'Processor Submit - SMS'),
        ('IA', 'Initial Approval - SMS'),
        ('FN', 'Final Approval - SMS'),
    )

    loan_number = models.PositiveIntegerField(unique=True)
    account_type = models.CharField(max_length=256, blank=True, choices=ACCOUNT_TYPES)
    loan_officer = models.CharField(max_length=256, blank=True)
    loan_processor = models.ForeignKey(Person, related_name="submittals", null=True, blank=True)
    loan_story = models.CharField(max_length=2560, blank=True)

    b1_first_name = models.CharField(max_length=256, blank=True)
    b1_last_name = models.CharField(max_length=256, blank=True)

    b2_first_name = models.CharField(max_length=256, blank=True)
    b2_last_name = models.CharField(max_length=256, blank=True)

    b1_employer_name = models.CharField(max_length=256, blank=True)
    b2_employer_name = models.CharField(max_length=256, blank=True)

    b1_phone_number = models.CharField(max_length=256, blank=True)
    b2_phone_number = models.CharField(max_length=256, blank=True)
    sms_template_select = models.CharField(max_length=256, blank=True, choices=SMS_TEMPLATE_TYPES)

    b1_email_address = models.EmailField(max_length=256, blank=True)
    b2_email_address = models.EmailField(max_length=256, blank=True)
    email_template_select = models.CharField(max_length=256, blank=True, choices=EMAIL_TEMPLATE_TYPES)
    email_message = models.CharField(max_length=2048, blank=True)

    b1_hire_date = models.CharField(max_length=256, blank=True)
    b2_hire_date = models.CharField(max_length=256, blank=True)

    b1_income_amount = models.PositiveIntegerField(null=True, blank=True)
    b2_income_amount = models.PositiveIntegerField(null=True, blank=True)

    b1_pay_frequency = models.CharField(max_length=256, blank=True, choices=PAY_TYPES)
    b2_pay_frequency = models.CharField(max_length=256, blank=True, choices=PAY_TYPES)

    b1_period_end_date = models.CharField(max_length=256, blank=True)
    b2_period_end_date = models.CharField(max_length=256, blank=True)

    b1_income_output = models.CharField(max_length=256, blank=True)
    b2_income_output = models.CharField(max_length=256, blank=True)

    created_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return "/{}/submittals/{}/".format(self.loan_processor.user.username, self.id)

    def __str__(self):
        return str(self.loan_number)