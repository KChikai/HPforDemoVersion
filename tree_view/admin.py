from django.contrib import admin
from tree_view.models import New


# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display = ('text_ja', 'text_en', 'date', 'image')

admin.site.register(New, NewAdmin)