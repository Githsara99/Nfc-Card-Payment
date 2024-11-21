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
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from cryptomus import Client
from .forms import CreateForm, PassengerForm, PassengerRegForm
from .models import Creator, Support, UserProfile, Ticket, ReloadCard, BitcoinTransaction, Passenger, Passenger_Reg
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

@csrf_exempt
@login_required
def create_bitcoin_transaction(request):
    """Handles the submission of a new Bitcoin transaction."""
    if request.method == "POST":
        try:
            user = request.user
            transaction_id = request.POST.get('transaction_id', '').strip()
            amount = float(request.POST.get('amount', 0))
            status = request.POST.get('status', '').strip()

            if not transaction_id or amount <= 0 or status not in ['Pending', 'Completed', 'Failed']:
                return JsonResponse({'success': False, 'error': 'Invalid input values'})

            # Create the Bitcoin transaction
            BitcoinTransaction.objects.create(
                user=user,
                transaction_id=transaction_id,
                amount=amount,
                status=status
            )

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    elif request.method == "GET":
        # Return an appropriate message or redirect for GET requests
        return JsonResponse({'success': False, 'error': 'GET method is not allowed for this endpoint'})
    else:
        # Return HTTP 405 Method Not Allowed for unsupported methods
        return HttpResponseNotAllowed(['POST'])



@login_required
def bitcoin_transactions(request):
    """Displays Bitcoin transactions for the logged-in user."""
    return render(request, 'creator/bitcoin.html', {
        'user': request.user,
    })


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
    


def passenger_list(request):
    context = {'passenger_list': Passenger.objects.all()}
    return render(request, 'creator/passenger_list.html', context)

def passenger_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = PassengerForm()
        else:
            passenger = Passenger.objects.get(pk=id)
            form = PassengerForm(instance=passenger)
        return render(request, 'creator/passenger_form.html', {"form": form})  # Handles both GET and POST
     
    else:
        if id == 0:
            form = PassengerForm(request.POST)
        else:
            passenger = Passenger.objects.get(pk=id)
            form = PassengerForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('creator:passenger_list')
    return render(request, 'creator/passenger_form.html', {"form": form})  # Handles both GET and POST
 

def passenger_delete(request, id):
    passenger = Passenger.objects.get(pk=id)
    passenger.delete()
    return redirect('creator:passenger_list')


def reg_passenger_list(request):
    context = {'reg_passenger_list': Passenger_Reg.objects.all()}
    return render(request, 'creator/reg_passenger_list.html', context)

def reg_passenger_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = PassengerRegForm()
        else:
            passenger = Passenger_Reg.objects.get(pk=id)
            form = PassengerRegForm(instance=passenger)
        return render(request, 'creator/passenger_reg.html', {"form": form})  # Handles both GET and POST
     
    else:
        if id == 0:
            form = PassengerRegForm(request.POST)
        else:
            passenger = Passenger_Reg.objects.get(pk=id)
            form = PassengerRegForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('creator:reg_passenger_list')
    return render(request, 'creator/passenger_reg.html', {"form": form})  # Handles both GET and POST
 

def reg_passenger_delete(request, id):
    passenger = Passenger_Reg.objects.get(pk=id)
    passenger.delete()
    return redirect('creator:reg_passenger_list')