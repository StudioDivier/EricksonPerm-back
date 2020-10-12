from django.contrib import admin
from .models import Trainers, Education, WayWork, Experience
from .models import Games, Offers, Feeds, Timetables


admin.site.register(Feeds)
admin.site.register(Trainers)
admin.site.register(Education)
admin.site.register(WayWork)
admin.site.register(Experience)
admin.site.register(Games)
admin.site.register(Timetables)