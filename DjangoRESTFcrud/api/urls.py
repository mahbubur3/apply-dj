from django.urls import path

from .import views


urlpatterns = [
    path('', views.student_list),
    path('detail/<str:pk>/', views.student_detail),
    path('create/', views.create_student),
    path('update/<str:pk>/', views.update_student),
    path('delete/<str:pk>/', views.delete_student),
]
