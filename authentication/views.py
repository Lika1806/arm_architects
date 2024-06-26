from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
# Create your views here.

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        #checkin username is valid or no
        if not str(username).isalnum():
            return JsonResponse({'username_error':'Username should only contain alphanumeric charecters'},status=400)
        
        #checkin wheather username is taken
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'The username is already in use, please choose another one'}, status=409)
        return JsonResponse({'username_valid':True})
    
class EmailValidationView(View):
    def post(self,request):
        data =  json.loads(request.body)
        email = data['email']

        #check email_validation
        if not validate_email(email):
            return JsonResponse({'email_error':'Email is invallid'},status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'The email is already in use, log-in or choose another one'}, status=409)
        return JsonResponse({'email_valid':True})