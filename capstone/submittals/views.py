from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .models import Person, Submittal
from .forms import SubmittalForm, PersonForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    form = SubmittalForm()
    return render(request, 'index.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/submittals/')
        elif user is None:
           messages.add_message(request, messages.ERROR, 'Your username or password is incorrect. Please try again.')
    return redirect('/')


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def submittals(request):
    form = SubmittalForm()
    return render(request, 'submittals.html', {'form': form})

@login_required
def save_submit(request):
    if request.method == 'POST':
        form = SubmittalForm(request.POST or None)
        if form.is_valid():
            submittal = form.save(commit=False)
            submittal.save()
            return HttpResponseRedirect('/submittals/', {'form': form})