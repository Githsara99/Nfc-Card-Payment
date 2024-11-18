# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from cryptomus import Client
# from .forms import CreateForm
# from .models import Creator, Support
# import pyrebase

# MERCHANT_UUID = '621379c1-acca-4252-bd66-2e86bfcff04'
# PAYMENT_KEY = '1P9521ebLUosz8zANZEOlFTNreI6DkI8qKefuQaDWGzug8r3Wz7k3N2CEdIzj5OjgiaqUfVxismOqPND'

# config = {
#   "apiKey": "AIzaSyDB0fpsVB3K54VG56VNY1oNaGvCopY-yuc",
#   "authDomain": "nfcdetails.firebaseapp.com",
#   "databaseURL": "https://nfcdetails-default-rtdb.firebaseio.com",
#   "projectId": "nfcdetails",
#   "storageBucket": "nfcdetails.firebasestorage.app",
#   "messagingSenderId": "1024977911201",
#   "appId": "1:1024977911201:web:266a0f80919b3b07325fe0",
# }

# firebase = pyrebase.initialize_app(config)
# authe = firebase.auth()
# database = firebase.database()


# @login_required

# def firebase(request):
#     try:
#         # Attempt to fetch data
#         channel_name = database.child('Data').child('Name').get().val()
#         print(f"Retrieved data: {channel_name}")  # Debug log
#     except Exception as e:
#         # Log any errors
#         print(f"Error retrieving data: {e}")
#         channel_name = None

#     return render(request, 'creator/mypage.html', {
#         "channel_name": channel_name,
#     })


# def mypage(request):
#     creator = request.user.creator
#     supports = creator.supports.filter(is_paid=True)
#     total = 0
    
#     for support in supports:
#         total += support.amount
    
#     return render(request, 'creator/mypage.html', {
#         'creator': creator,
#         'supports': supports,
#         'total': total
#     })

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             return redirect('creator:login')
#         else:
#             print(form.errors)
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'creator/signup.html',{
#         'form': form
#     })
    

# def creators(request):
        
#     creators = Creator.objects.all()
        
#     return  render(request, 'creator/creators.html', {
#         'creators': creators
#     })
    
# def creator(request, pk):
        
#     creator = Creator.objects.get(pk=pk)
        
#     return  render(request, 'creator/creator.html', {
#         'creator': creator
#     })
    
# def support_success(request, creator_id, support_id):
#     # print('Support success')
#     # print(request)
#     # print(creator_id)
#     # print(support_id)
    
#     support = Support.objects.get(pk=support_id)
    
#     payment = Client.payment(PAYMENT_KEY, MERCHANT_UUID)
    
#     # print(support, support.cryptomus_uuid)
    
#     result = payment.info({
#         "uuid": f"{support.cryptomus_uuid}",
#         "order_id" : f"{support.id}"
#     })
    
#     print(result)
    
#     if result['payment_status'] == 'paid':
#         support.is_paid = True
#         support.save()
    
#     return  render(request, 'creator/success.html')

# def edit(request):
#     try:
#         creator = request.user.creator
        
#         if request.method == 'POST':
#             form = CreateForm(request.POST, request.FILES, instance=creator)
            
#             if form.is_valid():
#                 form.save()
                
#                 return redirect('core:index')
#         else:
#             form = CreateForm(instance=creator)        
#     except Exception:
#         if request.method == 'POST':
#             form = CreateForm(request.POST, request.FILES)
            
#             if form.is_valid():
#                 creator = form.save(commit=False)
#                 creator.user = request.user
#                 creator.save()
                
#                 return redirect('core:index')
#         else:
#             form = CreateForm()
    
#     return render(request, 'creator/edit.html', {
#         'form': form
#     })


# from django.shortcuts import render, redirect
# from .forms import TicketPurchaseForm, ReloadCardForm
# from .models import Ticket, ReloadCard, UserProfile
# from creator.models import Creator

# def reload_card_view(request):
#     if request.method == 'POST':
#         form = ReloadCardForm(request.POST)
#         if form.is_valid():
#             card_number = form.cleaned_data['card_number']
#             amount = form.cleaned_data['amount']
#             try:
#                 card = ReloadCard.objects.get(card_number=card_number)
#                 card.balance += amount
#                 card.save()
#                 return render(request, 'success.html', {'message': 'Card reloaded successfully!'})
#             except ReloadCard.DoesNotExist:
#                 return render(request, 'error.html', {'message': 'Card not found!'})
#     else:
#         form = ReloadCardForm()
#     return render(request, 'reload_card.html', {'form': form})

# def purchase_ticket_view(request):
#     if request.method == 'POST':
#         form = TicketPurchaseForm(request.POST)
#         if form.is_valid():
#             ticket_type = form.cleaned_data['ticket_type']
#             ticket_price = form.cleaned_data['ticket_price']
#             if request.user.userprofile.card_balance >= ticket_price:
#                 request.user.userprofile.card_balance -= ticket_price
#                 request.user.userprofile.save()
#                 Ticket.objects.create(user=request.user, ticket_type=ticket_type, ticket_price=ticket_price)
#                 return render(request, 'success.html', {'message': 'Ticket purchased successfully!'})
#             else:
#                 return render(request, 'error.html', {'message': 'Insufficient balance!'})
#     else:
#         form = TicketPurchaseForm()
#     return render(request, 'purchase_ticket.html', {'form': form})



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from cryptomus import Client
from .forms import CreateForm
from .models import Creator, Support, UserProfile, Ticket, ReloadCard, BitcoinTransaction
import pyrebase
import uuid

MERCHANT_UUID = '621379c1-acca-4252-bd66-2e86bfcff04'
PAYMENT_KEY = '1P9521ebLUosz8zANZEOlFTNreI6DkI8qKefuQaDWGzug8r3Wz7k3N2CEdIzj5OjgiaqUfVxismOqPND'

payment_client = Client.payment(PAYMENT_KEY, MERCHANT_UUID)

config = {
  "apiKey": "AIzaSyDB0fpsVB3K54VG56VNY1oNaGvCopY-yuc",
  "authDomain": "nfcdetails.firebaseapp.com",
  "databaseURL": "https://nfcdetails-default-rtdb.firebaseio.com",
  "projectId": "nfcdetails",
  "storageBucket": "nfcdetails.firebasestorage.app",
  "messagingSenderId": "1024977911201",
  "appId": "1:1024977911201:web:266a0f80919b3b07325fe0",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


@login_required
def create_bitcoin_transaction(request):
    """Creates a Bitcoin transaction and generates a payment link using Cryptomus."""
    if request.method == "POST":
        try:
            amount = float(request.POST.get('amount', 0))
            if amount <= 0:
                return JsonResponse({'success': False, 'error': 'Invalid amount'})

            # Create a Bitcoin transaction in the database
            transaction = BitcoinTransaction.objects.create(
                user=request.user,
                transaction_id=str(uuid.uuid4()),
                amount=amount,
                status='Pending'
            )

            # Create a payment link using Cryptomus API
            cryptomus_response = payment_client.create({
                "order_id": transaction.transaction_id,
                "amount": str(amount),
                "currency": "BTC",  # Supported currencies include BTC, USDT, etc.
                "callback_url": "http://127.0.0.1:8000/api/cryptomus_callback/",  # Update with your callback URL
                "success_url": "http://127.0.0.1:8000/bitcoin_transactions/",
                "fail_url": "http://127.0.0.1:8000/bitcoin_transactions/",
            })

            if 'url' in cryptomus_response:
                payment_url = cryptomus_response['url']

                # Save the Cryptomus UUID in the transaction
                transaction.cryptomus_uuid = cryptomus_response['uuid']
                transaction.save()

                return JsonResponse({'success': True, 'transaction_id': transaction.transaction_id, 'payment_url': payment_url})

            return JsonResponse({'success': False, 'error': 'Failed to generate payment link.'})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})


@csrf_exempt
def cryptomus_callback(request):
    """Handles Cryptomus callbacks and updates transaction status."""
    if request.method == "POST":
        try:
            data = request.POST
            transaction_uuid = data.get('uuid')
            payment_status = data.get('payment_status')

            transaction = BitcoinTransaction.objects.get(cryptomus_uuid=transaction_uuid)

            if payment_status == 'paid':
                transaction.status = 'Completed'
            elif payment_status == 'failed':
                transaction.status = 'Failed'

            transaction.save()
            return JsonResponse({'success': True})
        except BitcoinTransaction.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Transaction not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})


@login_required
def bitcoin_transactions(request):
    """Displays Bitcoin transactions for the logged-in user."""
    return render(request, 'creator/bitcoin.html', {'user': request.user})



def firebase(request):
    try:
        # Attempt to fetch data
        channel_name = database.child('Data').child('Name').get().val()
        print(f"Retrieved data: {channel_name}")  # Debug log
    except Exception as e:
        # Log any errors
        print(f"Error retrieving data: {e}")
        channel_name = None

    return render(request, 'creator/mypage.html', {
        "channel_name": channel_name,
    })


def mypage(request):
    creator = request.user.creator
    supports = creator.supports.filter(is_paid=True)
    total = 0
    
    for support in supports:
        total += support.amount
    
    return render(request, 'creator/mypage.html', {
        'creator': creator,
        'supports': supports,
        'total': total
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('creator:login')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    
    return render(request, 'creator/signup.html',{
        'form': form
    })
    

def creators(request):
        
    creators = Creator.objects.all()
        
    return  render(request, 'creator/creators.html', {
        'creators': creators
    })
    
def creator(request, pk):
        
    creator = Creator.objects.get(pk=pk)
        
    return  render(request, 'creator/creator.html', {
        'creator': creator
    })
    
def support_success(request, creator_id, support_id):
    # print('Support success')
    # print(request)
    # print(creator_id)
    # print(support_id)
    
    support = Support.objects.get(pk=support_id)
    
    payment = Client.payment(PAYMENT_KEY, MERCHANT_UUID)
    
    # print(support, support.cryptomus_uuid)
    
    result = payment.info({
        "uuid": f"{support.cryptomus_uuid}",
        "order_id" : f"{support.id}"
    })
    
    print(result)
    
    if result['payment_status'] == 'paid':
        support.is_paid = True
        support.save()
    
    return  render(request, 'creator/success.html')

def edit(request):
    try:
        creator = request.user.creator
        
        if request.method == 'POST':
            form = CreateForm(request.POST, request.FILES, instance=creator)
            
            if form.is_valid():
                form.save()
                
                return redirect('core:index')
        else:
            form = CreateForm(instance=creator)        
    except Exception:
        if request.method == 'POST':
            form = CreateForm(request.POST, request.FILES)
            
            if form.is_valid():
                creator = form.save(commit=False)
                creator.user = request.user
                creator.save()
                
                return redirect('core:index')
        else:
            form = CreateForm()
    
    return render(request, 'creator/edit.html', {
        'form': form
    })
    
