from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .models import Person, Submittal
from .forms import SubmittalForm, PersonForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from addons.income_calc import IncomeCalc


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
        #import pdb; pdb.set_trace()
        person = Person.objects.get(user=request.user)
        submittals = person.submittals.all()
    return render(request, 'dashboard.html', {'submittals': submittals})


@login_required
def submittals(request, username):
    """
    submittal form page
    """
    form = SubmittalForm()
    return render(request, 'submittals.html', {'username': username, 'form': form})


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
            submittal.save()
            messages.add_message(request, messages.SUCCESS, 'Your file has been saved!')
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
        form = SubmittalForm(instance=submittal)
        return render(request, 'submittals.html', {'form': form})

    if request.method == 'POST':
        submittal = Submittal.objects.get(id=pk)
        form = SubmittalForm(instance=submittal)
        return render(request, 'submittals.html', {'form': form})
    """submittal = Submittal.objects.get(loan_number=request.POST['loan_number'])
    form = SubmittalForm(instance=submittal)
    return redirect(submittal.get_absolute_url())"""

@api_view(['POST'])
def calculate(request):
    return Response()
