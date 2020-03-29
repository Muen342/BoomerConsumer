from .views import index_view, boomer_view, nonboomer_view
from django.urls import path
from django.conf.urls import url

app_name = 'corona'
urlpatterns = [
    path('', index_view.login, name='login'),
    path('login', index_view.loginSubmit, name='loginSubmit'),
    path('index', index_view.index, name='index'),
    path('index2/', index_view.boomerIndex, name='index2'),
    path('index2/add', boomer_view.add, name='add'),
    path('index2/add/confirm', boomer_view.addListing, name='addListing'),
    path('index2/request/edit/<str:id>', boomer_view.editListing, name='editListing'),
    path('index2/request/delete/<str:id>', boomer_view.deleteListing, name='deleteListing'),
    path('index2/request/edit/<str:id>/confirm', boomer_view.confirmEditListing, name='confirmEditListing'),
    path('index/show_requests', nonboomer_view.show_requests, name='show_requests'),
    path('listings', boomer_view.listing, name='listing'),
    path('listings/take/<str:id>', boomer_view.requestTake, name='requestTake'),
    path('signupBoomer', index_view.signupB, name='boomerSignup'),
    path('signupZoomer', index_view.signupZ, name='zoomerSignup'),
    path('signupZoomerConfirm', index_view.signupZoomerConfirm, name='signupZoomerConfirm'),
    path('index/show_requests/complete/<str:id>', nonboomer_view.requestComplete, name='requestComplete'),
    path('index2/myrequests', nonboomer_view.show_requests, name='myrequests'),

]

