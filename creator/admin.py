# from django.contrib import admin

# from .models import Creator, Support

# admin.site.register(Creator)
# admin.site.register(Support)


from django.contrib import admin
from .models import Creator, Support, Ticket, ReloadCard, BitcoinTransaction, UserProfile

admin.site.register(Creator)
admin.site.register(Support)
admin.site.register(Ticket)
admin.site.register(ReloadCard)
admin.site.register(BitcoinTransaction)
admin.site.register(UserProfile)
