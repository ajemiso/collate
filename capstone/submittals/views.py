from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .models import Person, Submittal
from .forms import SubmittalForm, PersonForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
                return redirect('/{}/submittals/'.format(request.user.username))
        elif user is None:
           messages.add_message(request, messages.ERROR, 'Your username or password is incorrect. Please try again.')
    return HttpResponseRedirect('/')


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def submittals(request, username):

    form = SubmittalForm()
    return render(request, 'submittals.html', {'username': username, 'form': form})

@login_required
def save_submit(request):
    if request.method == 'POST':
        form = SubmittalForm(request.POST or None)
        if form.is_valid():
            submittal = form.save(commit=False)
            submittal.save()
            messages.add_message(request, messages.SUCCESS, 'Your file has been saved!')
            submittal = Submittal.objects.get()
            return JsonResponse({'success': 'It worked!'})
    return JsonResponse({'errors': 'Dude this didn"t work.'})

@login_required
def load_submit(request, username, pk):
    #import pdb; pdb.set_trace()
    submittal = Submittal.objects.get(id=pk)
    form = SubmittalForm(instance=submittal)
    return render(request, 'submittals.html', {'form': form})


