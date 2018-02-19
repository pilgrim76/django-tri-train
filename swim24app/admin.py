from django.contrib import admin

# Register your models here.
from .models import tbls24Sportsman, tbls24Distance, tbls24Results, tbls24Counter, tbls24ActionLog

admin.site.register(tbls24Sportsman)
admin.site.register(tbls24Distance)
admin.site.register(tbls24Results)
admin.site.register(tbls24ActionLog)
admin.site.register(tbls24Counter)

