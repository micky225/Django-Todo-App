from django.contrib import admin
from .models import Todo


admin.site.site_title = "Todo Admin"
admin.site.site_header = "Todo Admin"


admin.site.register(Todo)