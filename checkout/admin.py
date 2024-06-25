from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'first_name', 'last_name',
              'email', 'mobile_number','address_line1',
              'address_line2', 'town_or_city', 'county', 
              'country', 'postcode', 'date',
              'delivery_cost', 'order_total', 
              'grand_total', 'original_bag',
              'stripe_pid')

    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'email', 'mobile_number',
                    'order_total', 'delivery_cost', 
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)