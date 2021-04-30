from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from management.models import Booking  

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    age=forms.IntegerField()
    class Meta:
        model = User
        fields =  ['username','email','age','password1','password2']


class BookingForm(forms.ModelForm):  
    class Meta:  
        model = Booking
        fields = "__all__"  