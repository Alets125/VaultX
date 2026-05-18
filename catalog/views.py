import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Game, Category


def welcome_view(request):
    """Vista de bienvenida o splash screen."""
    return render(request, 'catalog/welcome.html')


def catalog_view(request):
    """Vista principal — cuadrícula de juegos + panel de detalle."""
    categories = Category.objects.all()
    category_slug = request.GET.get('cat', '')

    if category_slug:
        games = Game.objects.filter(category__slug=category_slug).select_related('category')
    else:
        games = Game.objects.all().select_related('category')

    # Serialize games to JSON for the JS detail panel
    games_data = []
    for g in games:
        games_data.append({
            'id':           g.id,
            'title':        g.title,
            'saga':         g.saga,
            'year':         g.year,
            'description':  g.description,
            'developer':    g.developer,
            'rating':       g.rating,
            'strength':     g.strength,
            'speed':        g.speed,
            'horror':       g.horror,
            'replayability': g.replayability,
            'cover_url':    g.cover_url(),
            'category':     g.category.name if g.category else '',
            'cat_color':    g.category.color if g.category else '#9b59ff',
        })

    context = {
        'games':       games,
        'categories':  categories,
        'active_cat':  category_slug,
        'games_json':  json.dumps(games_data, ensure_ascii=False),
    }
    return render(request, 'catalog/index.html', context)


def login_view(request):
    """Vista de inicio de sesión."""
    if request.user.is_authenticated:
        return redirect('catalog')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('catalog')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'catalog/login.html')


def logout_view(request):
    """Cierra sesión y redirige al login."""
    logout(request)
    return redirect('login')
