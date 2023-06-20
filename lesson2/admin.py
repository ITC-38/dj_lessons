from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline
from django.contrib.auth.models import User, Group

from lesson2.models import (
    Person, PersonProfile, Authors,
    Currency, Books, BooksCurrency,
    BookPhotos
)


class BooksPhotosInline(TabularInline):
    model = BookPhotos
    extra = 1


@admin.register(Books)
class BooksAdmin(ModelAdmin):
    inlines = [BooksPhotosInline]


class PersonAdmin(ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'last_update', 'registration_date']
    list_display_links = ['first_name']
    # list_editable = ['last_name']
    readonly_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'id']
    search_help_text = 'Ля чел ищи чё хочешь'
    list_filter = ['first_name']


admin.site.register(Person, PersonAdmin)
admin.site.register(PersonProfile)
admin.site.register(Authors)
admin.site.register(Currency)
# admin.site.register(Books)
admin.site.register(BooksCurrency)
admin.site.register(BookPhotos)

admin.site.site_title = 'Ёпта'
admin.site.site_header = 'Ёпта'
admin.site.unregister(User)
admin.site.unregister(Group)
