# import json
# from django.http import JsonResponse
# from cryptomus import Client
# from .models import Creator, Support

# MERCHANT_UUID = '621379c1-acca-4252-bd66-2e86bfcff04'
# PAYMENT_KEY = '1P9521ebLUosz8zANZEOlFTNreI6DkI8qKefuQaDWGzug8r3Wz7k3N2CEdIzj5OjgiaqUfVxismOqPND'

# def create_support(request):
#     print('request', request.POST)
    
#     if request.method == 'POST':
#         creator = request.POST
#         amount = request.POST.get('amount', '')
#         email = request.POST.get('email', '')
#         creator_id = request.POST.get('creator_id', '')
        
#         #Create support
        
#         support = Support.objects.create(
#             creator_id = creator_id,
#             amount = amount,
#             email = email,
#         )
        
        
#         # Talk to cryptomus
        
#         data = {
#             'amount': str(amount),
#             'currency': 'USD',
#             'network': 'Tron',
#             'order_id': str(support.id),
#             # change below after deploying
#             'url_return': f'https://127.0.0.1:8000/creators/{creator_id}/',
#             'url_success': f'https://127.0.0.1:8000/creators/{creator_id}/success/{str(support.id)}/',
#             'url_callback': f'https://127.0.0.1:8000/creators/{creator_id}/callback',
#             'to_currency': 'USDT',
            
#         }
        
       
        
#         payment = Client.payment(PAYMENT_KEY, MERCHANT_UUID)
        
#         result = payment.create(data)
        
#         jsondata = json.loads(data)
         
#         # print(result)
#         # print(result['uuid'])
#         # print(result['url'])
        
#         uuid = result['uuid']
#         url = result['url']
        
#         support.cryptomus_uuid = uuid
#         support.save()
     
#         return JsonResponse({'uuid': uuid, 'url': url})
#     else:
#         return JsonResponse({'success': False})


# from django.http import JsonResponse
# from .models import ReloadCard, Ticket, BitcoinTransaction

# def reload_card(request):
#     if request.method == 'POST':
#         card_number = request.POST.get('card_number')
#         amount = float(request.POST.get('amount'))

#         try:
#             card = ReloadCard.objects.get(card_number=card_number)
#             card.balance += amount
#             card.save()
#             return JsonResponse({'success': True, 'message': 'Card reloaded successfully!', 'balance': card.balance})
#         except ReloadCard.DoesNotExist:
#             return JsonResponse({'success': False, 'message': 'Card not found!'})

# def purchase_ticket(request):
#     if request.method == 'POST':
#         user = request.user
#         ticket_type = request.POST.get('ticket_type')
#         ticket_price = float(request.POST.get('ticket_price'))

#         if user.userprofile.card_balance >= ticket_price:
#             user.userprofile.card_balance -= ticket_price
#             user.userprofile.save()

#             Ticket.objects.create(user=user, ticket_type=ticket_type, ticket_price=ticket_price)
#             return JsonResponse({'success': True, 'message': 'Ticket purchased successfully!'})
#         else:
#             return JsonResponse({'success': False, 'message': 'Insufficient balance!'})

# def bitcoin_payment(request):
#     if request.method == 'POST':
#         user = request.user
#         amount = float(request.POST.get('amount'))

#         # Placeholder for Bitcoin API call
#         transaction_id = 'BITCOIN_TX_' + str(user.id)  # Replace with actual Bitcoin API integration
#         transaction = BitcoinTransaction.objects.create(user=user, transaction_id=transaction_id, amount=amount, status='Pending')
#         return JsonResponse({'success': True, 'message': 'Bitcoin payment initiated!', 'transaction_id': transaction.transaction_id})


import json
from django.http import JsonResponse
from cryptomus import Client
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Creator, Support, BitcoinTransaction, ReloadCard

MERCHANT_UUID = '621379c1-acca-4252-bd66-2e86bfcff04'
PAYMENT_KEY = '1P9521ebLUosz8zANZEOlFTNreI6DkI8qKefuQaDWGzug8r3Wz7k3N2CEdIzj5OjgiaqUfVxismOqPND'

@csrf_exempt
@login_required

def create_support(request):
    print('request', request.POST)
    
    if request.method == 'POST':
        creator = request.POST
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        creator_id = request.POST.get('creator_id', '')
        
        #Create support
        
        support = Support.objects.create(
            creator_id = creator_id,
            amount = amount,
            email = email,
        )
        
        
        # Talk to cryptomus
        
        data = {
            'amount': str(amount),
            'currency': 'USD',
            'network': 'Tron',
            'order_id': str(support.id),
            # change below after deploying
            'url_return': f'https://127.0.0.1:8000/creators/{creator_id}/',
            'url_success': f'https://127.0.0.1:8000/creators/{creator_id}/success/{str(support.id)}/',
            'url_callback': f'https://127.0.0.1:8000/creators/{creator_id}/callback',
            'to_currency': 'USDT',
            
        }
        
       
        
        payment = Client.payment(PAYMENT_KEY, MERCHANT_UUID)
        
        result = payment.create(data)
        
        jsondata = json.loads(data)
         
        # print(result)
        # print(result['uuid'])
        # print(result['url'])
        
        uuid = result['uuid']
        url = result['url']
        
        support.cryptomus_uuid = uuid
        support.save()
     
        return JsonResponse({'uuid': uuid, 'url': url})
    else:
        return JsonResponse({'success': False})
    
def create_bitcoin_transaction(request):
    if request.method == "POST":
        try:
            amount = float(request.POST.get('amount', 0))
            if amount <= 0:
                return JsonResponse({'success': False, 'error': 'Invalid amount'})

            transaction = BitcoinTransaction.objects.create(
                user=request.user,
                transaction_id=str(uuid.uuid4()),
                amount=amount,
                status='Pending'
            )

            return JsonResponse({'success': True, 'transaction_id': transaction.transaction_id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})    