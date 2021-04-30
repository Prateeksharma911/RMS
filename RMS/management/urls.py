from django.urls import path
from . import views
from django.contrib import admin  
from management import views  


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    # path('book', views.book),  
    path('book', views.BookView.as_view()),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  