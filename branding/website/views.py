from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def index(request):

    return render(request,
                  'website/index.html')

def about(request):

    return render(request,
                  'website/about.html')

def contact(request):

    form = ContactForm
    
    context = {    
    'form': form    
    }

    return render(request,
                  'website/contact.html', 
                  context)