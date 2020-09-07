from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]