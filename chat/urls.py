from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dash/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout-view'),
]
