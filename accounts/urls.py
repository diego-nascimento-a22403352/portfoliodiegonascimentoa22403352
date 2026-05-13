from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registo/', views.registo_view, name='registo'),
    # Rotas do Magic Link
    path('magic-login/', views.magic_link_request_view, name='magic_request'),
    path('verify/<str:uidb64>/<str:token>/', views.magic_link_verify_view, name='magic_verify'),
]