from django.contrib import admin
from f1app.models import Analysis, Driver, Constructor, Circuit, Races, Result, Analysis
# Register your models here.

admin.site.register(Driver)
admin.site.register(Constructor)
admin.site.register(Circuit)
admin.site.register(Races)
admin.site.register(Result)
admin.site.register(Analysis)