
""" FOOTBALL ADMIN """


from django.contrib import admin
from .models import Match, Team, Player, Banner


class BannerAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'name',
        'is_active',
        'banner_file'
    )
    list_filter: list[str] = (
        'name',
    )   



admin.site.register(Match),
admin.site.register(Team),
admin.site.register(Player)
admin.site.register(Banner, BannerAdmin)