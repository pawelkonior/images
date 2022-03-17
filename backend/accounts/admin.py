from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()


class CustomUserDashboard(UserAdmin):
    list_display = ('id', 'username', 'tier')
    list_editable = ('tier',)
    list_display_links = ('id', 'username')
    ordering = ('-id',)


admin.site.register(CustomUser, CustomUserDashboard)

admin.site.site_header = 'Admin Panel'
admin.site.site_title = 'Image Resizer'
admin.site.index_title = 'Administration'
