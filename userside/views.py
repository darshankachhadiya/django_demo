from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return  render(request,'home.html')

def about(request):
    return  render(request,'about.html')

def contact(request):
    return  render(request,'contact.html')

def form(request):
    return render(request,'form.html')

def process(request):
    print('welcome')
    print(request.method)
    print(request.POST)
    a = int(request.POST['txt1'])
    b = int(request.POST['txt2'])
    c=a+b
    print(c)
    return render(request,'ans.html',{'mya':a,'myb':b,'mysum':c})

def Contactprocess(request):
    print(request.method)
    print(request.POST)
    nameF = request.POST['txt1']
    nameM = request.POST['txt2']
    nameL = request.POST['txt3']
    sex   =  request.POST['Gender']
    Gmail = request.POST['txt4']
    Pno   = request.POST['txt5']

    return render(request,'ContactAns.html',{'Fname':nameF,'Mname':nameM,'Lname':nameL,'gender':sex,'letter':Gmail,'pnu':Pno})