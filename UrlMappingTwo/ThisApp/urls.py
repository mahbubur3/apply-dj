# from django.urls import path
# from ThisApp import views


# urlpatterns = [
#     path('', views.home, name='output')
# ]


from django.urls import path
from ThisApp import views

urlpatterns = [
    path('', views.home, name='home')
]
