from django import urls
from . import views



urlpatterns = [
    urls.path(route='', view=views.index, name='index'),
    urls.path(route='register', view=views.register, name='register'),
    urls.path(route='login', view=views.login, name='login'),
    urls.path(route='logout', view=views.logout, name='logout'),
    urls.path(route='get_name', view=views.get_name, name='get_name'),
]
