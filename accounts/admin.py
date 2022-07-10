from django.contrib import admin

from accounts.models import CustomUser, Company, Profile, Badges, Technologies

admin.site.register(CustomUser)
admin.site.register(Company)
admin.site.register(Profile)
admin.site.register(Badges)
admin.site.register(Technologies)
