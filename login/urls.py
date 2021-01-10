from django.urls import path,include
from .import views
urlpatterns = [
    path ('',views.login, name = 'login'),
    path('send/',views.send, name = 'send'),
    path('logout/',views.logout, name = 'logout'),
    path('home/',views.home, name = 'home')
]