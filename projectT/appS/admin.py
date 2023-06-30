from django.contrib import admin
from .models import User_req

# Register your models here.
class User_reqAdmin(admin.ModelAdmin):
    list_display = ('status', 'fname', 'sname', 'umail')
    list_display_links = ('status', 'fname', 'sname', 'umail')
    search_fields = ('status', 'fname', 'sname', 'umail')

admin.site.register(User_req, User_reqAdmin)

