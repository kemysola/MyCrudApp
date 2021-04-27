from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django. urls import reverse_lazy

# Create your views here.
class MyPasswordChangeView(PasswordChangeView):
    template_name ='users/password_change.html'
    success_url =reverse_lazy('users:password_change_done_view')
    
class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name ='users/password_reset_done.html'