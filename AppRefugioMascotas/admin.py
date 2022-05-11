from django.contrib import admin
from .models import User
from .models import Pets
from .models import Adoption
from .models import FailedLogin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin
from simple_history import register

class displayFailedLogin(SimpleHistoryAdmin,ImportExportModelAdmin,admin.ModelAdmin):
    list_display =('user','times')
    
class displayUser(SimpleHistoryAdmin,ImportExportModelAdmin,admin.ModelAdmin):
    list_display =('username','is_active','is_staff','is_superuser')

class PetsAdmin(SimpleHistoryAdmin,ImportExportModelAdmin, admin.ModelAdmin):
    pass
class AdoptionAdmin(SimpleHistoryAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(User, displayUser)
admin.site.register(Pets, PetsAdmin)
admin.site.register(Adoption, AdoptionAdmin)
admin.site.register(FailedLogin,displayFailedLogin)
