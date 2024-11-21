# from django.contrib.auth import views as auth_views
# from django.urls import path
# from . import api
# from . import views

# app_name = 'creator'

# urlpatterns = [
#     path('api/create_support', api.create_support, name='api_create_support'),
#     path('mypage/', views.mypage, name="mypage"),
#     path('creators/', views.creators, name='creators'),
#     path('creators/<int:pk>', views.creator, name='creator'),
#     path('creators/<int:creator_id>/success/<int:support_id>', views.support_success, name='success'),
#     path('edit/', views.edit, name='edit'),
#     path('signup/', views.signup, name='signup'),
#     path('login/', auth_views.LoginView.as_view(template_name='creator/login.html'), name='login'),
# ]


# from django.urls import path
# from . import views, api

# urlpatterns = [
#     path('reload-card/', views.reload_card_view, name='reload_card'),
#     path('purchase-ticket/', views.purchase_ticket_view, name='purchase_ticket'),
#     path('api/reload-card/', api.reload_card, name='api_reload_card'),
#     path('api/purchase-ticket/', api.purchase_ticket, name='api_purchase_ticket'),
#     path('api/bitcoin-payment/', api.bitcoin_payment, name='api_bitcoin_payment'),
# ]


from django.contrib.auth import views as auth_views
from django.urls import path
from . import api
from . import views

app_name = 'creator'

urlpatterns = [
    #sample
    path('create/', views.passenger_form, name="passenger_insert"),
    path('list/', views.passenger_list, name="passenger_list"),
    path('<int:id>/', views.passenger_form, name="passenger_update"),
    path('delete/<int:id>', views.passenger_delete, name="passenger_delete"),
    
    path('createReg/', views.reg_passenger_form, name="reg_passenger_insert"),
    path('listReg/', views.reg_passenger_list, name="reg_passenger_list"),
    path('<int:id>/', views.reg_passenger_form, name="reg_passenger_update"),
    path('deleteReg/<int:id>', views.passenger_delete, name="reg_passenger_delete"),
    # Existing paths
    path('api/create_support', api.create_support, name='api_create_support'),
    path('mypage/', views.mypage, name="mypage"),
    path('mypage/', views.creators, name='creators'),
    path('creators/<int:pk>', views.creator, name='creator'),
    path('creators/<int:creator_id>/success/<int:support_id>', views.support_success, name='success'),
    path('edit/', views.edit, name='edit'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='creator/login.html'), name='login'),
    # Change `bitcoin/` to `bitcoin_transactions/`
    path('bitcoin_transactions/', views.bitcoin_transactions, name='bitcoin_transactions'),
    path('api/create_bitcoin_transaction/', views.create_bitcoin_transaction, name='create_bitcoin_transaction'),
    path('api/cryptomus_callback/', views.cryptomus_callback, name='cryptomus_callback'),
]

