from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse

from .models import Contact, Category

# Create your views here.
def home(request):
    users = Contact.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'users': users, 'categories': categories})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    
    return redirect('home') 