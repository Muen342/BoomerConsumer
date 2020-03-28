from .views import index_view, boomer_view, nonboomer_view
from django.urls import path

app_name = 'corona'
urlpatterns = [
    path('', index_view.login, name='login'),
    path('index', index_view.index, name='index'),
    path('listings', boomer_view.listing, name='listing'),
    path('listings/take/<str:id>', boomer_view.requestTake, name='requestTake'),
    path('signupBoomer', index_view.signupB, name='boomerSignup'),
    path('signupZoomer', index_view.signupZ, name='zoomerSignup')
]