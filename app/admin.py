from django.contrib import admin
from .models import Trainers, Education, WayWork, Experience
from .models import Games, Offers, Feeds, Timetables


class EducationAdmin(admin.TabularInline):
    model = Education


class ExperienceAdmin(admin.TabularInline):
    model = Experience


class WayWorkAdmin(admin.TabularInline):
    model = WayWork


@admin.register(Trainers)
class TrainersAdmin(admin.ModelAdmin):
    """

    """
    list_display = ('title', )
    list_filter = ('title', )
    fieldsets = (
        ('Коучер', {
            'fields': ('img', ('title', 'description'))
        }),
    )
    inlines = [
        EducationAdmin,
        ExperienceAdmin,
        WayWorkAdmin
    ]


admin.site.register(Feeds)
admin.site.register(Games)
admin.site.register(Timetables)
