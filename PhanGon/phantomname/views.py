from django.shortcuts import render




def index(request):
    template = 'phantomname/index.html'
    context = {}
    response = render(
        request=request,
        template_name=template,
        context=context,
    )

    return response
