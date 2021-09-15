from django.urls import path
from .views import about, contact, home, post, publicity

urlpatterns = [
    path('', home , name = 'index'),
    path('publicity/', publicity , name = 'publicity'),
    path('contact/', contact , name = 'contact'),
    path('about/', about , name = 'about'),
    path('<slug:slug>/', post, name ='post')
]

