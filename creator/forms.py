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
from .models import Creator
 
 
class CreateForm(ModelForm):
    class Meta:
        model = Creator
        fields = ('title', 'description', 'image',)