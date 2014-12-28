from django.contrib import admin

# Register your models here.
from vexere.models import User

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'firstname', 'lastname']
    list_display = ('username', 'email', 'firstname', 'lastname')
    list_filter = ['username', 'email', 'firstname', 'lastname']
    search_fields = ['username']

admin.site.register(User, UserAdmin)