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
