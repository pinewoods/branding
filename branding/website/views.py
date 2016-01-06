from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

# Create your views here.
def index(request):

    return render(request,
                  'website/index.html')

def about(request):

    return render(request,
                  'website/about.html')

def services(request):

    return render(request,
                  'website/services.html')

def education(request):

    return render(request,
                  'website/education.html')

def products(request):

    return render(request,
                  'website/products.html')

def contact(request):

    message = ''

    if request.method == 'GET':
        form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            contact = Contact(name=name, phone=phone, email=email, message=message)
            contact.save()

            message = 'your message was successfully sent'

    context = {    
    'form': form,
    'message': message
    }

    return render(request,
                  'website/contact.html', 
                  context)