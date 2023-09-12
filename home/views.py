from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact
# Create your views here.
def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def blog(request):
    return render(request, 'blog.html')


def contact_view(request):
    if request.method=="POST":

        Name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        enquiry = request.POST.get('enquiry')
        en = contact(name=Name,email=email,phone=phone,date= datetime.today(),enquiry=enquiry)
        en.save()
        return HttpResponse('Thanks for contact  with us..')

    return render(request, 'contact.html')


def intro(request):
    return render(request, 'intro.html')


