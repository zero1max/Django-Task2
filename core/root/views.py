from django.shortcuts import render
from .models import Contact, Category

# Create your views here.
def home(request):
    users = Contact.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'users': users, 'categories': categories})