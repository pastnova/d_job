from django.contrib import admin

from core.models import UserProfile, Application, Conference

admin.site.register(UserProfile)
admin.site.register(Application)
admin.site.register(Conference)
