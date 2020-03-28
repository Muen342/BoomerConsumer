from .views import index_view, boomer_view, nonboomer_view
from django.urls import path

app_name = 'corona'
urlpatterns = [
    path('', index_view.login, name='login'),
    path('index', index_view.index, name='index'),
    path('listings', boomer_view.listing, name='listing'),
]