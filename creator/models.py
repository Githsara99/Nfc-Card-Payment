# from django.contrib.auth.models import User
# from django.db import models

# class Creator(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to='uploads/creators')
#     user = models.OneToOneField(User, related_name='creator', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Support(models.Model):
#     creator = models.ForeignKey(Creator, related_name='supports', on_delete=models.CASCADE)
#     amount = models.IntegerField()
#     is_paid = models.BooleanField(default=False)
#     cryptomus_uuid = models.UUIDField(blank=True, null=True)
#     email = models.EmailField()
#     created_at = models.DateTimeField(auto_now_add=True)


# from django.contrib.auth.models import User
# from django.db import models

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     card_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

# class Ticket(models.Model):
#     user = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
#     ticket_type = models.CharField(max_length=100)  # Example: "Bus", "Train"
#     ticket_date = models.DateField()
#     ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)

# class ReloadCard(models.Model):
#     card_number = models.CharField(max_length=16, unique=True)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     user = models.ForeignKey(User, related_name='reload_cards', on_delete=models.CASCADE)

# class BitcoinTransaction(models.Model):
#     user = models.ForeignKey(User, related_name='bitcoin_transactions', on_delete=models.CASCADE)
#     transaction_id = models.CharField(max_length=100, unique=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
#     created_at = models.DateTimeField(auto_now_add=True)


from django.contrib.auth.models import User
from django.db import models

class Creator(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/creators')
    user = models.OneToOneField(User, related_name='creator', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Support(models.Model):
    creator = models.ForeignKey(Creator, related_name='supports', on_delete=models.CASCADE)
    amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    cryptomus_uuid = models.UUIDField(blank=True, null=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Ticket(models.Model):
    user = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=100)  # Example: "Bus", "Train"
    ticket_date = models.DateField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class ReloadCard(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    user = models.ForeignKey(User, related_name='reload_cards', on_delete=models.CASCADE)

class BitcoinTransaction(models.Model):
    user = models.ForeignKey(User, related_name='bitcoin_transactions', on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')])
   # cryptomus_uuid = models.CharField(max_length=100, blank=True, null=True)  # Store Cryptomus UUID
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_id} - {self.status}"
    
    
class Position(models.Model):
    title = models.CharField(max_length=50)

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    card_id = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=15)
    recharge = models.DecimalField(max_digits=10, decimal_places=2)
    famount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


class Passenger_Reg(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
   
    

   