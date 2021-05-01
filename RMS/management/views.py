from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.views import View

from management.forms import BookingForm  
from management.models import Booking  

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Acount Created for {username}!')
            return render(request, 'index.html')

    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


class RegisterView(View):
    def get(self,request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Acount Created for {username}!')
            return render(request, 'index.html')
        return render(request, 'register.html', {'form': form})

    def post(self,request):
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})


class BookView(View):
    
    def get(self,request):
        form = BookingForm()  
        return render(request,'front.html',{'form':form})  

    def post(self,request):
        form = BookingForm(request.POST, request.FILES) 
        if form.is_valid():
            try:
                form.save()
                print(form.errors)
                return redirect('/show')  
            except:
                print(form.errors)
        else:
            print(form.errors)
        return render(request,'front.html',{'form':form})  

def show(request):  
    bookings = Booking.objects.all()  
    return render(request,"show.html",{'bookings':bookings})  

class ShowView(View):
    def get(self,request):
        bookings = Booking.objects.all()  
        return render(request,"show.html",{'bookings':bookings})  


def edit(request, id):  
    booking = Booking.objects.get(id=id)  
    return render(request,'edit.html', {'booking':booking})  

class EditView(View):
    def get(self,request,id):
        booking = Booking.objects.get(id=id)  
        return render(request,'edit.html', {'booking':booking})  

# class UpdateView(View):
#     def get(self,request,id):
#         booking = Booking.objects.get(id=id)  
#         return render(request, 'edit.html', {'booking': booking})  


#     def post(self,request,id):
#         booking = Booking.objects.get(id=id)  
#         # form = BookingForm(request.POST, instance = booking)  
#         form = BookingForm(data=request.POST, files=request.FILES, instance=booking)  
#         if form.is_valid():
#             print("ajbfb")
#             form.save()  
#             return redirect("/show")
#         else:
#             print("abc")
#             print(form.errors)
#         return render(request, 'edit.html', {'booking': booking})  


def update(request, id):  
    booking = Booking.objects.get(id=id)  
    form = BookingForm(request.POST, request.FILES ,instance = booking)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")
    else:
        print(form.errors)
    return render(request, 'edit.html', {'booking': booking})  
def destroy(request, id):  
    booking = Booking.objects.get(id=id)  
    booking.delete()  
    return redirect("/show")  
