from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')
def aboutus(request):
    return render(request,'aboutus.html')
def our_services(request):
    return render(request,'Our_Services.html')
def card(request):
    return render(request,'card.html')
def contactus(request):
    return render(request,'contactus.html')
def faq(request):
    return render(request,'FAQ.html')
