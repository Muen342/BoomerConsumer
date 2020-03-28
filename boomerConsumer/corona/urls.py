from .views import index_view, boomer_view, nonboomer_view
from django.urls import path

app_name = 'corona'
urlpatterns = [
    path('', index_view.login, name='login'),
    path('index', index_view.index, name='index'),
    path('index/show_requests', nonboomer_view.show_requests, name='show_requests'),
    path('listings', boomer_view.listing, name='listing'),
    path('listings/take/<str:id>', boomer_view.requestTake, name='requestTake'),
    path('index/show_requests/complete/<str:id>', nonboomer_view.requestComplete, name='requestComplete'),
]