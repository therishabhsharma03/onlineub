from django.contrib import admin

# Register your models here.
from ecommerceapp.models import Contact,Menu,Orders,OrderUpdate

admin.site.register(Contact)
admin.site.register(Menu)
admin.site.register(Orders)
admin.site.register(OrderUpdate)


