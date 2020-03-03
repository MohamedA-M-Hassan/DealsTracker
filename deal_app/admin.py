from django.contrib import admin
from deal_app.models import Customer,Deal,Deal_Items_Price_Lookup,Deal_Items

# Register your models here.

admin.site.register(Customer)
admin.site.register(Deal)
admin.site.register(Deal_Items)
admin.site.register(Deal_Items_Price_Lookup)
