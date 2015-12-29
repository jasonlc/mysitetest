from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from models import Book,Publisher,Author
from django.core.mail import send_mail
from forms import ContactForm

def search(request):
    errors=[]
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q)>20:
            errors.append('Please enter at most 20 characters.')
        else:
            books=Book.objects.filter(title__icontains=q)
            print(books)
            return render_to_response('search_results.html',{'books':books,'query':q})
    return render_to_response('search_from.html',{'errors':errors})

def contact(request):
    if request.method=='POST':
       form=ContactForm(request.POST)
       if form.is_valid():
           cd =form.cleaned_data
           send_mail(
               cd['subject'],
               cd['message'],
               cd.get('email','noreply@example.com'),
               ['siteowner@example.com'],
           )
           return HttpResponseRedirect('/contact/thanks/')
    else:
       form=ContactForm()
    return render_to_response('contact_form.html',{'form':form})

