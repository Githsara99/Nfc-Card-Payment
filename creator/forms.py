# from django.forms import ModelForm
# from .models import Creator
 
 
# class CreateForm(ModelForm):
#     class Meta:
#         model = Creator
#         fields = ('title', 'description', 'image',)
 


# from django import forms

# class TicketPurchaseForm(forms.Form):
#     ticket_type = forms.CharField(max_length=100)
#     ticket_price = forms.DecimalField(max_digits=10, decimal_places=2)

# class ReloadCardForm(forms.Form):
#     card_number = forms.CharField(max_length=16)
#     amount = forms.DecimalField(max_digits=10, decimal_places=2)


from django.forms import ModelForm
from .models import Creator, Passenger
from django import forms 
 
class CreateForm(ModelForm):
    class Meta:
        model = Creator
        fields = ('title', 'description', 'image',)

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ('name', 'card_id', 'mobile', 'recharge', 'famount', 'balance',)
        labels ={
            'name':'Name',
            'card_id':'Card ID',
            'mobile':'Mobile',
            'recharge':'Recharge',
            'famount':'Final Amount',
            'balance':'Balance',   
        }
    
    def __init__(self, *args, **kwargs):
        super(PassengerForm,self).__init__(*args, **kwargs)
        self.fields['card_id'].required = False