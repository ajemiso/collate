from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SubmittalSerializer

# from _private.secret import account_sid, auth_token
from .forms import SubmittalForm, PersonForm
from addons.income_calc import IncomeCalc
from addons.messages import SMS_MESSAGES, EMAIL_MESSAGES
from addons.zillow_parser import ZillowParser
from _private.private import GOOGLE_MAPS_API_KEY
from .models import Person, Submittal

from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

import json


# TWILIO SETTINGS
account_sid = 'AC86189c370a1fcca6c3dd11c2fa15ee04'
auth_token = '1769e4656916ec050cdbe4e58d17e6c1'


def index(request):
    """
    landing page
    """
    form = SubmittalForm()
    return render(request, 'index.html', {'form': form})


def login_user(request):
    """
    login function (redirects to submittals)
    """
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/{}/submittals/'.format(request.user.username))
        elif user is None:
           messages.add_message(request, messages.ERROR, 'Your username or password is incorrect. Please try again.')
    return HttpResponseRedirect('/')


@login_required
def logout_user(request):
    """
    logout function
    """
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def dashboard(request, username):
    """
    main dashboard with list of submittals for user
    """
    if request.method == 'GET':
        person = Person.objects.get(user=request.user)
        submittals = person.submittals.all().order_by('-created_at')

        paginator = Paginator(submittals, 5)

        page = request.GET.get('page')
        try:
            submits = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            submits = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            submits = paginator.page(paginator.num_pages)


        loan_list = list(submittals.values_list('loan_number', flat=True))
        loan_strings = list(map(str, loan_list))
        loan_numbers = json.dumps(loan_strings)


    return render(request, 'dashboard.html', {'submittals': submits, 'autolist': loan_numbers })


@login_required
def submittals(request, username):
    """
    submittal form page
    """
    form = SubmittalForm()
    sms_messages = json.dumps(SMS_MESSAGES)
    email_messages = json.dumps(EMAIL_MESSAGES)
    return render(request, 'submittals.html', {'username': username, 'form': form, 'sms_messages': sms_messages, 'email_messages': email_messages })


@login_required
def save_submit(request):
    """
    save user submittal
    """
    if request.method == 'POST':
        loan_number = request.POST['loan_number']
        submittal, created = Submittal.objects.get_or_create(loan_number=loan_number)
        form = SubmittalForm(request.POST, instance=submittal)
        if form.is_valid():
            submittal = form.save(commit=False)
            submittal.loan_processor = request.user.person
            submittal.appraisal_value = request.POST.get('appraisal-value')
            submittal.save()
            pk = submittal.id
            return JsonResponse({'pk': pk})
    return JsonResponse({'errors': 'Dude this didn"t work.'})


@login_required
def load_submit(request, username, pk=None):
    """
    loads user submittal
    """
    if request.method == 'GET':
        submittal = Submittal.objects.get(id=pk)

        b1_first_name = submittal.b1_first_name
        loan_processor = 'Andre'# request.user.username
        loan_officer = submittal.loan_officer

        form = SubmittalForm(instance=submittal)
        fulfilled_sms_messages = {k: v.format(b1_first_name=b1_first_name, loan_processor=loan_processor,
                                              loan_officer=loan_officer) for k, v in SMS_MESSAGES.items()}

        sms_messages = json.dumps(fulfilled_sms_messages)
        email_messages = json.dumps(EMAIL_MESSAGES)
        return render(request, 'submittals.html', {'form': form, 'sms_messages': sms_messages,
                                                   'email_messages': email_messages })

    if request.method == 'POST':
        submittal = Submittal.objects.get(id=pk)

        b1_first_name = submittal.b1_first_name
        loan_processor = request.user.username
        loan_officer = submittal.loan_officer

        form = SubmittalForm(instance=submittal)
        fulfilled_sms_messages = {k: v.format(b1_first_name=b1_first_name, loan_processor=loan_processor, loan_officer=loan_officer) for k, v in
        SMS_MESSAGES.items()}

        sms_messages = json.dumps(fulfilled_sms_messages)
        email_messages = json.dumps(EMAIL_MESSAGES)
        return render(request, 'submittals.html', {'form': form, 'sms_messages': sms_messages,
                                                   'email_messages': email_messages,
                                                   'GOOGLE_MAPS_API_KEY': GOOGLE_MAPS_API_KEY })


@api_view(['DELETE'])
@login_required

def delete_submit(request):
    submittal = Submittal.objects.get(loan_number=request.DELETE['loan_number'])
    submittal.delete()
    return JsonResponse({'success': 'File {} has been deleted'.format(submittal.loan_number)})


@api_view(['POST'])
@login_required
def auto_save(request):
    submittal = Submittal.objects.get(loan_number=request.POST['loan_number'])
    if submittal is not None:
        return Response()


@login_required
def sms_message(request):
    """ Sends SMS message to client upon request """
    if request.method == 'POST':
        client = TwilioRestClient(account_sid, auth_token)

        if request.POST['loan_number'] != '':
            recipient_data = request.POST.getlist('recipients[]')
            recipients = list(map(str.strip, recipient_data))
            recipients = ['+1{}'.format(number) for number in recipients if number != '']

            try:
                for number in recipients:
                    message = client.messages.create(body=request.POST.get('sms_message'),
                                                     to=number,
                                                     from_=request.POST['sender']
                                                     )
            except TwilioRestException as e:
                print(e)
                return JsonResponse({'error': 'error'})
        return JsonResponse({'success': '204'})



@login_required
def calculate_income(request):
    """
    calculates income for a borrower
    """

    borrower = request.POST['borrower']

    if request.method == 'POST':
        data = request.POST.copy()

        # change pay frequency value
        if 'b1_pay_frequency' in data:
            pay_type = data['b1_pay_frequency']

            if pay_type == 'SM':
                new_pay = 'semi-monthly'
                data['b1_pay_frequency'] = new_pay
            elif pay_type == 'BW':
                new_pay = 'bi-weekly'
                data['b1_pay_frequency'] = new_pay
            elif pay_type == 'MO':
                new_pay = 'monthly'
                data['b1_pay_frequency'] = new_pay
            elif pay_type =='WK':
                new_pay = 'weekly'
                data['b1_pay_frequency'] = new_pay
            else:
                raise ValueError('You did it wrong!')

        elif 'b2_pay_frequency' in data:
            pay_type = data['b2_pay_frequency']

            if pay_type == 'SM':
                new_pay = 'semi-monthly'
                data['b2_pay_frequency'] = new_pay
            elif pay_type == 'BW':
                new_pay = 'bi-weekly'
                data['b2_pay_frequency'] = new_pay
            elif pay_type == 'MO':
                new_pay = 'monthly'
                data['b2_pay_frequency'] = pay_type
            elif pay_type =='WK':
                new_pay = 'weekly'
                data['b2_pay_frequency'] = pay_type
            else:
                raise ValueError('You did it wrong!')

        calculator = IncomeCalc(**data)
        result = calculator.create_string()

    if borrower == '1':
        return JsonResponse({'b1_income_output': result})
    elif borrower == '2':
        return JsonResponse({'b2_income_output': result})
    else:
        return JsonResponse({'output': 'error'})


@login_required()
def get_zestimate(request):
    if request.method == 'POST':
       address = {'address': request.POST.get('address'),
                  'city': request.POST.get('city'),
                  'state': request.POST.get('state'),
                  'zip': request.POST.get('zip')
                  }
       zillow = ZillowParser(**address)
       zillow.get_zestimate()
       zestimate = zillow.zestimate
       latitude = zillow.lat
       longitude = zillow.long

       return JsonResponse({'zestimate': zestimate, 'latt': latitude, 'long': longitude})

