from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render,redirect
import random
import string
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def hello1(request):
    return HttpResponse("<center>WELCOME TO TTM HOMEPAGE</center>")
def hello(request):
    return render(request,'hello.html')
def newhomepage(request):
    return render(request,'newhomepage.html')
def travelpackage(request):
    return render(request,'travelpackage.html')

def print1(request):
    return render(request,'printtoconsole.html')
def printtoconsole(request):
    if request.method=="POST":
        userinput=request.POST['userinput']
        print(f'userinput:{userinput}')
    # return HttpResponse('Form Submitted Successfully')
    a1={'userinput':userinput}
    return render(request,'printtoconsole.html',a1)
def random123(request):
    if request.method=='POST':
        input1=request.POST['userinput']
        input2=int(input1)
        result=''.join(random.sample(string.digits,input2))
        # print(result)
        context={'result':result}
    return render(request,'random123.html',context)
def random1(request):
    return render(request,'random123.html')
def getdate1(request):
    return render(request,'get_date.html')
import datetime
from.forms import *
from django.shortcuts import render
def get_date(request):
    if request.method=='POST':
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'get_date.html',{'form':form})
from .models import *
def tzcall(request):
    return render(request,'pytz.html')
def database(request):
    return render(request,'myregisterpage.html')
def registerloginfunction(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            message1="Email already register,choose different mail "
            return render(request,'myregisterpage.html',{'message1':message1})
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'myregisterpage.html')

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart images
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'piechart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'piechart.html', {'form': form})
def piecal(request):
    return render(request, 'piechart.html')
def my(request):
    return render(request,'tourimages.html')
import requests
from django.shortcuts import render

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '11bea47fb8035443d4699f0047978d00'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)

            return render(request, 'weather.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weather.html', {'error_message': error_message})

class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')

def weathe(request):
    return render(request,'weather.html')

def login(request):
    return render(request,'login.html')
def sinup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,"Newhomepage.html")
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def sinup1(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully')
                return render(request,'login.html')
        else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render(request,'Newhomepage.html')

def ca(request):
    return render(request,'feed.html')

def contactmail(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        comment=request.POST['comment']
        tosend=comment+'______'
        data=contactus(firstname=firstname,lastname=lastname,email=email)
        data.save()
        return HttpResponse("<h1> <center>Thanks for giving Feedback </center> </h1>")

import re
import smtplib
import random
from django.shortcuts import render
def sentmail(request):
    if request.method == 'POST':
        fullname = request.POST.get("name1")
        email = request.POST.get("email")

        if not is_valid_email(email):
            return render(request, "invalid_email.html")

        # Setting up SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        password = "wgkdfzapygmzqakm"  # Assuming this is the password for manojkadambala2005@gmail.com
        server.login("manojkadambala2005@gmail.com", password)

        body = "You have to attend the orientation session on python at KL R&D theater"
        subject = "Hello KLUIn"
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail("manojkadambala2005@gmail.com", email, message)
    return render(request, "mm.html")

def is_valid_email(email):
    # Using regular expression to validate email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

from django.shortcuts import render,redirect
from .models import URL
import string
import random
# Create your views here.

def url_shortener(request):
    if request.method=='POST':
        long_url=request.POST['long_url']
        short_url=generate_short_url()
        URL.objects.create(long_url=long_url,short_url=short_url)
        return render(request,'url_shortener.html',{'short_url':short_url})
    return render(request,'url_shortener.html')

def redirect_to_original(request,short_url):
    url=URL.objects.get(short_url=short_url)
    return redirect(url.long_url)

def generate_short_url():
    characters=string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for i in range(6))
    complete_url = f'www.{short_url}.com'
    return complete_url
