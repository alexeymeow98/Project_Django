from django.contrib import admin
from .models import Post, Contact

admin.site.register(Post)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass