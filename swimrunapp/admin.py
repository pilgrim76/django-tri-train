from django.contrib import admin

# Register your models here.

from .models import tblDistance, tblDistanceType, tblDistanceSplits, tblSportsman, tblResult, tblSplitsResult

admin.site.register(tblDistance)
admin.site.register(tblDistanceType)
admin.site.register(tblDistanceSplits)
admin.site.register(tblSportsman)
admin.site.register(tblResult)
admin.site.register(tblSplitsResult)
