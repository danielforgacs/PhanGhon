import random
import logging
from django import shortcuts
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import decorators
from . import forms
from . import models


logging.config.dictConfig(settings.LOG_CONFIG)
logger = logging.getLogger(__name__)



def index(request):
    template = 'phantomname/index.html'
    userform = forms.UserForm()
    ghostnames = models.GhostName.objects.all()
    context = {
        'userform': userform,
        'ghostnames': ghostnames,
    }
    response = shortcuts.render(
        request=request,
        template_name=template,
        context=context,
    )

    return response




def register(request):
    is_open = models.User.objects.count() <= models.GhostName.objects.count()
    template = 'phantomname/register.html'
    userform = forms.UserForm(request.POST or None)
    context = {
        'userform': userform,
        'is_open': is_open,
    }

    if userform.is_valid():
        username = userform.data.get('username')
        password = userform.data.get('password')
        user = models.User.objects.create_user(
            username=username,
            password=password,
        )
        auth.login(request, user)
        response = shortcuts.redirect(to=index)

    else:
        response = shortcuts.render(
            request=request,
            template_name=template,
            context=context,
        )

    return response




def login(request):
    template = 'phantomname/login.html'
    response = shortcuts.render(
        request=request,
        template_name=template,
    )

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(
            request=request,
            username=username,
            password=password,
        )
        if user:
            auth.login(request, user)
            response = shortcuts.redirect(to='index')
        else:
            response = shortcuts.redirect(to='register')

    return response





def logout(request):
    auth.logout(request=request)
    response = shortcuts.redirect(to='index')

    return response




@decorators.login_required(login_url='login')
def get_name(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        user = request.user
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        response = shortcuts.redirect(to='choose_name')

    else:
        template = 'phantomname/get_name.html'
        response = shortcuts.render(
            request=request,
            template_name=template,
        )

    return response




@decorators.login_required(login_url='login')
def choose_name(request):
    # print('ajsdfh')
    available = models.GhostName.objects.query_free_names()
    choicecount = min(available.count(), 3)
    choices = []
    # print(choicecount)

    for _ in range(choicecount):
        # This part makes sure no 3 choices have
        # duplicate ghost names selected.
        candidate = random.choice(available)
        looplimit = 100
        counter = 0

        while candidate in choices:
            counter += 1
            # print(counter)

            if counter == looplimit:
                break

            candidate = random.choice(available)

        choices.append(candidate)

    template = 'phantomname/choose_name.html'
    context = {
        'choices': choices,
    }
    response = shortcuts.render(
        request=request,
        template_name=template,
        context=context,
    )

    return response




def save_choice(request):
    ghostnameid = request.GET.get('choice')
    ghostname = models.GhostName.objects.get(id=ghostnameid)
    query_phantomname = models.PhantomName.objects.filter(
        user=request.user,
    )

    if query_phantomname:
        phantomname = query_phantomname[0]
        phantomname.ghostname = ghostname
        phantomname.save()

    else:
        phantomname = models.PhantomName.objects.create(
            user=request.user,
            ghostname=ghostname,
        )

    response = shortcuts.redirect(to='index')

    return response
