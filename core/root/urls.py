from django.urls import path
from .views import home, delete_contact

urlpatterns = [
    path('', home, name='home'),
    path('delete/<int:contact_id>/', delete_contact, name='delete_contact'),
]
