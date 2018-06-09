
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
# from myapp.models import Users
# from myapp.serializers import UsersSerializer 
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from serializers import AccountSerializer, AccountRiskSerializer
from app_accounts.models import Account, Account_Risk

obj_len=0

class GetAccountDetails(generics.ListAPIView):
    global obj_len
    queryset = Account.objects.values()
    obj_len = len(queryset)
    serializer_class = AccountSerializer

    

class GetAccountRiskDetails(generics.ListAPIView):
    queryset = Account_Risk.objects.all()
    serializer_class = AccountRiskSerializer

