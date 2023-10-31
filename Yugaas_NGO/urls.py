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
    path('aboutus3',views.aboutus3),
    path('aboutus4',views.aboutus4),
    path('login',views.login),
    path('Causes',views.causes),
    path('Getinvolved', views.Getinvolved),
    path('volunteer', views.volunteer),
    path('support',views.support),
    path('impact',views.impact),
    path('Donate',views.Donate),
    path('foster',views.foster),

    #path('<int:id>/',views.detail)

]
from django.conf.urls.static import static
from Yugaas_NGO import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)