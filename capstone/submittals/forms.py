from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Person, Submittal

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        exclude = ['joined_at']


class SubmittalForm(forms.ModelForm):


    class Meta:
        model = Submittal
        fields = '__all__'
        widgets = {
            'b1_first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First'}),
            'b1_last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last'}),
            'loan_officer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name Only'}),
            'loan_story': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Loan Story',
                                                                                        'rows': 5}),
            'account_type': forms.Select(attrs={'class': 'form-control'}),
            'loan_number': forms.TextInput(attrs={'name': 'loan_number', 'class': 'form-control', 'id': 'loan_number_field', 'placeholder': 'Digits only'}),
            'b2_first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First'}),
            'b2_last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last'}),

            'b1_employer_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'b1_employer_name','placeholder': 'Employer'}),
            'b1_hire_date': forms.TextInput(attrs={'class': 'form-control', 'id': 'b1_hire_date', 'placeholder': 'mm/dd/yy'}),
            'b1_period_end_date': forms.TextInput(attrs={'class': 'form-control', 'id': 'b1_period_end_date', 'placeholder': 'mm/dd/yy'}),
            'b1_income_amount': forms.TextInput(attrs={'class': 'form-control', 'id': 'b1_income_amount', 'placeholder': '$'}),
            'b1_pay_frequency': forms.Select(attrs={'class': 'form-control', 'id': 'b1_pay_frequency'}),
            'b1_income_output': forms.Textarea(attrs={'class': 'form-control',
                                                      'id': 'b1_income_output',
                                                      'placeholder': 'All income fields must be completed',
                                                      'rows': 5,
                                                      }),

            'b2_employer_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'b2_employer_name', 'placeholder': 'Employer'}),
            'b2_hire_date': forms.TextInput(attrs={'class': 'form-control', 'id': 'b2_hire_date', 'placeholder': 'mm/dd/yy'}),
            'b2_period_end_date': forms.TextInput(attrs={'class': 'form-control', 'id': 'b2_period_end_date', 'placeholder': 'mm/dd/yy'}),
            'b2_income_amount': forms.TextInput(attrs={'class': 'form-control', 'id': 'b2_income_amount', 'placeholder': '$'}),
            'b2_pay_frequency': forms.Select(attrs={'class': 'form-control', 'id': 'b2_pay_frequency'}),
            'b2_income_output': forms.Textarea(attrs={'class': 'form-control',
                                                      'placeholder': 'All income fields must be completed',
                                                      'id': 'b2_income_output',
                                                      'rows': 5,
                                                      }),
        }
        labels = {
            'b1_first_name': 'First Name', # custom labels for field names
        }