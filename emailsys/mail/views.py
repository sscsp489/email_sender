from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here
from .forms import mailForm
from .forms import messForm
from .models import emails,mess
from django.core.mail import send_mail

def f():
    elist = emails.objects.all()
    m = mess.objects.all()

    for i in m:
        me = i.message
        su = i.subject
    eelist = []
    for i in elist:
        eelist.append(i.mail)
    send_mail(me,su,'sscsp489@gmail.com',eelist)

def end_mail(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = messForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            mes = form.save(commit=False)
            mes.save()
            f()
            form = messForm()            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = messForm()
    title = "Send-email"
    return render(request, 'sendmail.html', {'form': form,'t':title})    

def get_mail(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = mailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            email = form.save(commit=False)
            email.save()
            form = mailForm()            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = mailForm()
    title = "Add-email"
    return render(request, 'mail.html', {'form': form,'t':title})
def mail(request):
    emaillist = emails.objects.all()
    title = "Email-sender"
    return render(request,'main.html',{'list':emaillist,'t':title})

