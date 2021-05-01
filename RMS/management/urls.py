from django.urls import path
from . import views
from django.contrib import admin  
from management import views  


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterView.as_view()),
    # path('book', views.book),  
    path('book', views.BookView.as_view()),  
    path('show',views.ShowView.as_view()),  
    path('edit/<int:id>', views.EditView.as_view()),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  