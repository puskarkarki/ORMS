from django.contrib import admin
from .models import *

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Payment)
