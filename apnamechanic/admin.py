from django.contrib import admin
from .models import Car 
from .models import MODEL
from .models import Services

admin.site.register(Car)
# Register your models here.
admin.site.register(MODEL)
admin.site.register(Services)