from django.contrib import admin
from homepage.models import New, Paper, Author


# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display = ('text_ja', 'text_en', 'date', 'image')

admin.site.register(New, NewAdmin)
admin.site.register(Paper)
admin.site.register(Author)