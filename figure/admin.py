from django.contrib import admin
from .models import Division

# Register your models here.
class DivisionAdmin(admin.ModelAdmin):
	list_display = ('div_name', 'population', 'area', 'elevation')

admin.site.register(Division, DivisionAdmin)