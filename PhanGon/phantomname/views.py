from django import shortcuts
from django.contrib import auth
from . import forms
from . import models




def index(request):
    template = 'phantomname/index.html'
    userform = forms.UserForm()
    context = {
        'userform': userform,
    }
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

    return response





def logout(request):
    auth.logout(request=request)
    response = shortcuts.redirect(to='index')

    return response
