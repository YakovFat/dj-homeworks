from django.contrib import admin
from .models import Phone, Apple, Samsung


# Register your models here.
class PhoneAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Samsung, PhoneAdmin)
admin.site.register(Apple, PhoneAdmin)

