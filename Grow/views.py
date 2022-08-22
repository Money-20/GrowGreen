from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.views.decorators.http import require_http_methods

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404

# Create your views here.
from .forms import CreateUserForm

#from .models import User

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
mail = ""

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string



def success(request):
    template = render_to_string('base/email_template.html', {'name': request.user})
    mail = request.user.profile.user.email

    email = EmailMessage(
        'Thanks for registering in Grow-Green Website. Happy Gardening :)',
        template,
        'manikantaanumalla@gmail.com',
        'manikantaanumalla@gmail.com',
    )

    email.fail_silently=False
    email.send()

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                success(request)
                user = form.cleaned_data.get('username')
                mail = form.cleaned_data.get('email')
                messages.success(request, 'Account was created for ' + user)
                success(request)
                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        success(request)
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
          #  email = request.POST.get('email')

            user = authenticate(request, username=username, password=password)


            if user is not None:
                login(request, user)
                success(request)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


#def logoutUser(request):
 #   logout(request)
  #  return redirect('home')
def logoutUser(request):
    logout(request)
    return render(request, 'logout.html', context={})

@login_required(login_url='login')
def home(request):
    context = {}

    return render(request, 'home.html', context)

def landing(request):
    context = {}
    return render(request, 'landing.html', context)

@login_required(login_url='login')
@require_http_methods(["GET"])
def index(request):
    context = {}
    return render(request, 'index.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)

def bonsai(request):
    context = {}
    return render(request, 'bonsai.html', context)

def hf(request):
    context  = {}
    return render(request, 'hf.html', context)

def tr(request):
    context = {}
    return render(request, 'trc.html', context)


from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def success(request):
    template = render_to_string('base/email_template.html', {'name': request.user})


    email = EmailMessage(
        'Thanks for registering in Grow-Green Website. Happy Gardening :)',
        template,
        settings.EMAIL_HOST_USER,
        mail
    )

    email.fail_silently=False
    email.send()








