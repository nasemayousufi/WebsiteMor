"""
Definition of urls for TextWebsiteDjango.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from home import forms, views
from datetime import datetime
from django.urls import path,include






urlpatterns = [
    #path('items/', views.item_list, name='item_list'),  
    #path('item/<int:item_id>/', views.item_detail, name='item_detail'),  # URL for the item detail page
    path('', views.home,name='home'),
    path('', include('home.urls')),
    path('about/', views.about, name='about'),

    path('admin/', admin.site.urls),
    path('login/',
     LoginView.as_view
     (
         template_name='home/login.html',
         authentication_form=forms.BootstrapAuthenticationForm,
         extra_context=
         {
             'title': 'Log in',
             'year' : datetime.now().year,
         }
     ),
     name='login'),
path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

