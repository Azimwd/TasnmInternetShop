from django.contrib import admin

from carts.models import Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product', 'quantity', 'craeted_timestamp']
    list_filter = ['user', 'product', 'craeted_timestamp']

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Аноним'