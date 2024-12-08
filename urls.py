from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('apply-loan/', views.apply_loan, name='apply_loan'),
    path('loan-success/', views.loan_success, name='loan_success'),
    path('login-success/', views.login_success, name='login_success'),
    path('document', views.document, name='doucment'),
    path('loan-application/', views.loan_application, name='loan_application'),
    path('terms', views.terms, name='terms'),
    path('policy',views.policy, name='policy'),
    path('personal', views.personal, name='personal'),
    path('apna', views.apna, name='apna'),
    path('eduction', views.eduction, name='eduction'),
    path('car', views.car, name='car'),
    path('nikl', views.nikl, name='nikl'),
    

]