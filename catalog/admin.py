from django.contrib import admin
from .models import Category, Game


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['name', 'slug', 'color']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display   = ['title', 'saga', 'year', 'category', 'rating', 'featured']
    list_filter    = ['category', 'featured', 'year']
    search_fields  = ['title', 'saga', 'developer']
    list_editable  = ['featured']
    fieldsets = (
        ('Información principal', {
            'fields': ('title', 'saga', 'year', 'developer', 'category', 'rating', 'featured')
        }),
        ('Descripción', {
            'fields': ('description',)
        }),
        ('Estadísticas (0-100)', {
            'fields': ('intensity', 'difficulty', 'story', 'replayability')
        }),
        ('Imagen de portada (Cloudinary)', {
            'fields': ('cover_image',)
        }),
    )
