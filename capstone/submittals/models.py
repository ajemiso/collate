from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User)
    joined_at = models.DateTimeField(auto_now=True)


class Submittal(models.Model):
    loan_number = models.PositiveIntegerField(unique=True)
    account_type = models.CharField(max_length=256)
    loan_officer = models.CharField(max_length=256)
    loan_processor = models.ForeignKey(Person, related_name="submittals")

    b1_first_name = models.CharField(max_length=256)
    b1_last_name = models.CharField(max_length=256)

    b2_first_name = models.CharField(max_length=256, null=True)
    b2_last_name = models.CharField(max_length=256, null=True)

    b1_employer_name = models.CharField(max_length=256, null=True)
    b2_employer_name = models.CharField(max_length=256, null=True)

    b1_hire_date = models.DateField(max_length=256, null=True)
    b2_hire_date = models.DateField(max_length=256, null=True)

    b1_income_amount = models.PositiveIntegerField(null=True)
    b2_income_amount = models.PositiveIntegerField(null=True)

    b1_pay_frequency = models.CharField(max_length=256, null=True)
    b2_pay_frequency = models.CharField(max_length=256, null=True)

    b1_period_end_date = models.CharField(max_length=256, null=True)
    b2_period_end_date = models.CharField(max_length=256, null=True)

    created_at = models.DateTimeField(auto_now=True)

