from django.urls import path
from . import views
    
urlpatterns = [
    # path('',views.home),
    path('', views.student_list, name='student-list'), # List students
    path('add/', views.student_add, name='student-add'), # Add a student
    path('<int:pk>/edit/', views.student_edit, name='student-edit'), # Edit a student
    path('<int:pk>/delete/', views.student_delete, name='student-delete'), # Delete a
]