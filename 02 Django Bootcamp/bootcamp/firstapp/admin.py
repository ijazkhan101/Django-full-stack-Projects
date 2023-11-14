from django.contrib import admin
from firstapp.models import AccessRecord, Topic, Webpage
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
