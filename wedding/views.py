from django.shortcuts import render_to_response
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from wedding.forms import ContactForm



# Create your views here.
def home_list(request):
	return render_to_response('wedding/index.html')

def contact_list(request):
	return render_to_response('wedding/contact.html')

def index_list(request):
	return render_to_response('wedding/index.html')
def index_li(request):
	return render_to_response('wedding/gallery.html')

def about(request):
	return render(request, 'wedding/about.html')

def blog(request):
	return render(request, 'wedding/blog.html')
	

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['']
            phone = form.cleaned_data['']
            email = form.cleaned_data['']
            message = form.cleaned_data['']
            try:
                send_mail(name, message, email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "wedding/contact.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')