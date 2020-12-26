from django.contrib import admin
from .models import CardInfo

# Register your models here.
admin.site.site_header = 'Proxima Centauri Admin'
admin.site.site_title = 'Holiday Greetings Card Generator Admin Area'


admin.site.register(CardInfo)