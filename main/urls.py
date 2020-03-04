from django.urls import path
from .views import homepage, register, logout_request, login_request, single_slug, search


app_name = 'main'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('logout/', logout_request, name='logout'),
    path('login/', login_request, name='login'),
    path('<single_slug>', single_slug, name='single_slug'),
    path('search/', search, name='search')
]
