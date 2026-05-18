from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """Categorías o etiquetas de los juegos (Horror, Acción, Carreras, etc.)"""
    name        = models.CharField(max_length=80, unique=True, verbose_name='Nombre')
    slug        = models.SlugField(max_length=80, unique=True, verbose_name='Slug')
    description = models.TextField(blank=True, verbose_name='Descripción')
    color       = models.CharField(
        max_length=7, default='#9b59ff',
        verbose_name='Color hex',
        help_text='Color de la etiqueta en la interfaz (ej. #9b59ff)'
    )

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name


class Game(models.Model):
    """Modelo principal — un videojuego del catálogo."""

    RATING_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]

    title       = models.CharField(max_length=200, verbose_name='Título')
    saga        = models.CharField(max_length=100, blank=True, verbose_name='Saga')
    year        = models.PositiveIntegerField(verbose_name='Año de lanzamiento')
    description = models.TextField(verbose_name='Descripción')
    category    = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='games', verbose_name='Categoría'
    )
    developer   = models.CharField(max_length=150, blank=True, verbose_name='Desarrollador')
    rating      = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES, default=3, verbose_name='Calificación'
    )
    # Stats for detail panel (0-100)
    intensity     = models.PositiveSmallIntegerField(default=50, verbose_name='Intensidad')
    difficulty    = models.PositiveSmallIntegerField(default=50, verbose_name='Dificultad')
    story         = models.PositiveSmallIntegerField(default=50, verbose_name='Historia')
    replayability = models.PositiveSmallIntegerField(default=50, verbose_name='Rejugabilidad')

    cover_image = CloudinaryField('image', blank=True, null=True)

    featured    = models.BooleanField(default=False, verbose_name='Destacado')
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Videojuego'
        verbose_name_plural = 'Videojuegos'
        ordering = ['title']

    def __str__(self):
        return self.title

    def cover_url(self):
        """Return the Cloudinary URL or a placeholder."""
        if self.cover_image:
            return self.cover_image.url
        return ''
