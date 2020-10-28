from django.shortcuts import render
from . import forms




def index(request):
    template = 'phantomname/index.html'
    userform = forms.UserForm()
    context = {
        'userform': userform,
    }
    response = render(
        request=request,
        template_name=template,
        context=context,
    )

    return response
