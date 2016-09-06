from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .models import Person, Submittal
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def login_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/submittals/')
    return redirect('/')


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def submittals(request):
    return render(request, 'submittals.html')