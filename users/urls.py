from django.urls import path, include
from django.conf.urls import url 
from django.conf import settings
from articles import views as article_views
from .views import MyPasswordChangeView, MyPasswordResetDoneView
from django. urls import reverse_lazy
#from django .contrib.auth import views as auth_views


from . import views

app_name ='users'

urlpatterns = [
    path('change_password/',MyPasswordChangeView.as_view(),name='password_change_view'),
    path('change_password/done/',MyPasswordResetDoneView.as_view(),name='password_change_done_view'),
]

