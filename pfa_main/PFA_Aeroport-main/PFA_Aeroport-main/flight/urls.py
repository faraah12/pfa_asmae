from django.urls import path
from . import views

app_name = 'flight'

urlpatterns = [
    path('book/', views.book_flight, name='book_flight'),
]
