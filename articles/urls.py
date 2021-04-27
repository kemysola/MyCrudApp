"""blog_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

#from django .contrib.auth import views as auth_views

app_name = 'articles'

urlpatterns = [
    path('',views.article_list, name ='list'),
    url(r'^create/$',views.article_create, name = 'create'),
    #url(r'^(?P<slug>[\w-]+)/$',views.article_details,name ='detail'),
    path('<slug:slug>/',views.article_details,name ='detail'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name ='accounts/password_reset_change.html')),
]

