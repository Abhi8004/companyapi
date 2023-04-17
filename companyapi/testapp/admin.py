from django.contrib import admin
from testapp.models import Company,Employee,User

# Register your models here.
#class UserManagerAdmin(admin.ModelAdmin):
    #list_display=('email','password')

class UserAdmin(admin.ModelAdmin):
    list_display=('email', 'phone', 'is_verified')

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    list_filter=('company',)
    search_fields=('name',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
#admin.site.register(UserManager,UserManagerAdmin)
admin.site.register(User,UserAdmin)
