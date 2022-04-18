from django.contrib import admin
from .models import User
from .models import Pets
from .models import Adoption

# Register your models here.
admin.site.register(User)
admin.site.register(Pets)
admin.site.register(Adoption)

