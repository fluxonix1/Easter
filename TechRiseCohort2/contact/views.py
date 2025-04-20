from django.shortcuts import render, redirect
from .models import Contact_Message

def contact_views(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            Contact_Message.objects.create(name= name, email=email, message=message)
    # return redirect('contact:contact_view')
    return render(request, 'contact/contact.html')


# Create your views here.
