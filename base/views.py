from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')
def aboutus(request):
    return render(request,'aboutus.html')
def aboutus1(request): 
    return render(request, 'aboutus1.html')
def aboutus2(request):
    return render(request, 'aboutus2.html')
def aboutus3(request):
    return render(request, 'aboutus3.html')
def aboutus4(request):
    return render(request, 'aboutus4.html')
def our_services(request):
    return render(request,'Our_Services.html')
def card(request):
    return render(request,'card.html')
def contactus(request):
    return render(request,'contactus.html')
def faq(request):
    return render(request,'FAQ.html')
def login(request):
    return render(request,'login.html')
def causes(request):
    return render ( request , "causes.html" )
def Getinvolved(request):
    return render(request,'Get_invloved.html')  
def volunteer(request):
    return render(request,'get1.html')
def support(request):
    return render(request,'support.html')  
def foster(request):
    return render(request,'foster.html')
def impact(request):
    return render(request,'impact.html') 
def Donate(request):
    return render(request,'Donate.html')
def exception(request, exception):
    return render(request, '404.html')