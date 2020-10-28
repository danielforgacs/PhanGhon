from django import urls
from . import views



urlpatterns = [
    urls.path(route='', view=views.index, name='index'),
]
