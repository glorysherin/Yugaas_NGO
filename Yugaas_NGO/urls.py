from django.contrib import admin
from django.urls import path
from base import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home),
    path('',views.base),
    path('base',views.base),
    path('aboutus',views.aboutus),
    path('services',views.our_services),
    path('card',views.card),
    path('contactus',views.contactus),
    path('faq',views.faq),
    path('aboutus1',views.aboutus1),
    path('aboutus2',views.aboutus2),
    path('login',views.login),
    path('Causes',views.causes),
    path('Getinvolved', views.Getinvolved),

    #path('<int:id>/',views.detail)

]
