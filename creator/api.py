from django.http import JsonResponse
from cryptomus import Client
from .models import Creator, Support

MERCHANT_UUID = '621379c1-acca-4252-bd66-2e86bfcff04'
PAYMENT_KEY = '1P9521ebLUosz8zANZEOlFTNreI6DkI8qKefuQaDWGzug8r3Wz7k3N2CEdIzj5OjgiaqUfVxismOqPND'

def create_support(request):
    print('request', request.POST)
    
    if request.method == 'POST':
        email = request.POST.get('email', '')
        
        print('email',email)
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
