from django.conf.urls import url
from django.contrib import admin
from app_accounts import views

urlpatterns = [
    url(r'^account_details/', views.GetAccountDetails.as_view()),
    url(r'^account_risk_details/', views.GetAccountRiskDetails.as_view()),
]
