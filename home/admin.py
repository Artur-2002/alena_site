from django.contrib import admin
from .models import Product, Makeup_img, Wedding_img, Hair_img

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']

	def has_delete_permission(self, request, obj=None):
		return False

admin.site.register(Product, ProductAdmin)

admin.site.register(Makeup_img)
admin.site.register(Wedding_img)
admin.site.register(Hair_img)