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
            'account_type': forms.Select(attrs={'class': 'form-control'}),
            'b2_first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First'}),
            'b2_last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last'}),

            'b1_employer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employer'}),
            'b1_hire_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mm/dd/yy'}),
        }
        labels = {
            'b1_first_name': 'First Name', # custom labels for field names
        }