from django.contrib import admin

# Register your models here.

from .models import tblSportsman, tblDistance, tblResults, tblActionLog

admin.site.register(tblSportsman)
admin.site.register(tblDistance)
admin.site.register(tblResults)
admin.site.register(tblActionLog)

