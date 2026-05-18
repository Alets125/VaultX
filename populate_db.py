import os
import django
from django.utils.text import slugify

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videogame_catalog.settings')
django.setup()

from catalog.models import Category, Game

def populate():
    # Define primary categories without emojis
    cat_data = {
        "Survival Horror": "#5b2c6f",
        "Mundo Abierto": "#117864",
        "Hack and Slash": "#922b21",
        "Shooter": "#d35400",
        "Carreras": "#2874a6",
        "RPG": "#b7950b",
        "Lucha": "#b03a2e"
    }

    categories = {}
    for name, color in cat_data.items():
        cat, created = Category.objects.get_or_create(
            name=name,
            defaults={'slug': slugify(name), 'color': color, 'description': f'Juegos de la categoría {name}'}
        )
        categories[name] = cat
        print(f"Categoría '{name}' lista.")

    # Games list
    games_list = [
        # Survival Horror & Terror
        {"title": "Resident Evil 2 Remake", "saga": "Resident Evil", "cat": "Survival Horror", "dev": "Capcom"},
        {"title": "Resident Evil 4 Remake", "saga": "Resident Evil", "cat": "Survival Horror", "dev": "Capcom"},
        {"title": "Resident Evil 7: Biohazard", "saga": "Resident Evil", "cat": "Survival Horror", "dev": "Capcom"},
        {"title": "The Evil Within", "saga": "The Evil Within", "cat": "Survival Horror", "dev": "Tango Gameworks"},
        {"title": "The Evil Within 2", "saga": "The Evil Within", "cat": "Survival Horror", "dev": "Tango Gameworks"},
        {"title": "Silent Hill 2", "saga": "Silent Hill", "cat": "Survival Horror", "dev": "Konami"},
        {"title": "Dead Space Remake", "saga": "Dead Space", "cat": "Survival Horror", "dev": "Motive Studio"},
        {"title": "Alan Wake 2", "saga": "Alan Wake", "cat": "Survival Horror", "dev": "Remedy"},

        # Mundo Abierto, Sandbox & Supervivencia
        {"title": "Grand Theft Auto V", "saga": "Grand Theft Auto", "cat": "Mundo Abierto", "dev": "Rockstar Games"},
        {"title": "Grand Theft Auto: San Andreas", "saga": "Grand Theft Auto", "cat": "Mundo Abierto", "dev": "Rockstar Games"},
        {"title": "DayZ", "saga": "DayZ", "cat": "Mundo Abierto", "dev": "Bohemia Interactive"},
        {"title": "State of Decay 2", "saga": "State of Decay", "cat": "Mundo Abierto", "dev": "Undead Labs"},
        {"title": "Rust", "saga": "Rust", "cat": "Mundo Abierto", "dev": "Facepunch Studios"},
        {"title": "7 Days to Die", "saga": "7 Days to Die", "cat": "Mundo Abierto", "dev": "The Fun Pimps"},
        {"title": "Minecraft", "saga": "Minecraft", "cat": "Mundo Abierto", "dev": "Mojang"},

        # Hack and Slash & Acción
        {"title": "Devil May Cry 3: Dante's Awakening", "saga": "Devil May Cry", "cat": "Hack and Slash", "dev": "Capcom"},
        {"title": "Devil May Cry 4", "saga": "Devil May Cry", "cat": "Hack and Slash", "dev": "Capcom"},
        {"title": "Prince of Persia: The Sands of Time", "saga": "Prince of Persia", "cat": "Hack and Slash", "dev": "Ubisoft"},
        {"title": "Prince of Persia: Warrior Within", "saga": "Prince of Persia", "cat": "Hack and Slash", "dev": "Ubisoft"},
        {"title": "Bayonetta", "saga": "Bayonetta", "cat": "Hack and Slash", "dev": "PlatinumGames"},
        {"title": "God of War (2018)", "saga": "God of War", "cat": "Hack and Slash", "dev": "Santa Monica Studio"},
        {"title": "NieR: Automata", "saga": "NieR", "cat": "Hack and Slash", "dev": "PlatinumGames"},

        # Shooter (FPS / TPS)
        {"title": "Left 4 Dead", "saga": "Left 4 Dead", "cat": "Shooter", "dev": "Valve"},
        {"title": "Back 4 Blood", "saga": "Back 4 Blood", "cat": "Shooter", "dev": "Turtle Rock"},
        {"title": "Max Payne", "saga": "Max Payne", "cat": "Shooter", "dev": "Remedy"},
        {"title": "Max Payne 2: The Fall of Max Payne", "saga": "Max Payne", "cat": "Shooter", "dev": "Remedy"},
        {"title": "Doom Eternal", "saga": "Doom", "cat": "Shooter", "dev": "id Software"},
        {"title": "Gears of War 3", "saga": "Gears of War", "cat": "Shooter", "dev": "Epic Games"},
        {"title": "Cyberpunk 2077", "saga": "Cyberpunk", "cat": "Shooter", "dev": "CD Projekt RED"},

        # Carreras & Simulación
        {"title": "Gran Turismo 4", "saga": "Gran Turismo", "cat": "Carreras", "dev": "Polyphony Digital"},
        {"title": "Gran Turismo Sport", "saga": "Gran Turismo", "cat": "Carreras", "dev": "Polyphony Digital"},
        {"title": "Night-Runners", "saga": "Night-Runners", "cat": "Carreras", "dev": "PLANET JUPITER"},
        {"title": "Forza Horizon 5", "saga": "Forza", "cat": "Carreras", "dev": "Playground Games"},
        {"title": "Need for Speed: Most Wanted", "saga": "Need for Speed", "cat": "Carreras", "dev": "EA Black Box"},
        {"title": "Assetto Corsa", "saga": "Assetto Corsa", "cat": "Carreras", "dev": "Kunos Simulazioni"},

        # RPG (Role-Playing Game)
        {"title": "Persona 3 Reload", "saga": "Persona", "cat": "RPG", "dev": "Atlus"},
        {"title": "Persona 4 Golden", "saga": "Persona", "cat": "RPG", "dev": "Atlus"},
        {"title": "The Witcher 3: Wild Hunt", "saga": "The Witcher", "cat": "RPG", "dev": "CD Projekt RED"},
        {"title": "Final Fantasy VII Remake", "saga": "Final Fantasy", "cat": "RPG", "dev": "Square Enix"},
        {"title": "Elden Ring", "saga": "Stand-alone", "cat": "RPG", "dev": "FromSoftware"},
        {"title": "Fallout: New Vegas", "saga": "Fallout", "cat": "RPG", "dev": "Obsidian"},

        # Lucha / Arcade
        {"title": "Tekken 7", "saga": "Tekken", "cat": "Lucha", "dev": "Bandai Namco"},
        {"title": "Tekken 3", "saga": "Tekken", "cat": "Lucha", "dev": "Namco"},
        {"title": "Street Fighter 6", "saga": "Street Fighter", "cat": "Lucha", "dev": "Capcom"},
        {"title": "Mortal Kombat 1", "saga": "Mortal Kombat", "cat": "Lucha", "dev": "NetherRealm"},
        {"title": "Super Smash Bros. Ultimate", "saga": "Super Smash Bros.", "cat": "Lucha", "dev": "Nintendo"},
        {"title": "Dragon Ball FighterZ", "saga": "Dragon Ball", "cat": "Lucha", "dev": "Arc System Works"}
    ]

    count = 0
    for g in games_list:
        game, created = Game.objects.get_or_create(
            title=g["title"],
            defaults={
                'saga': g["saga"],
                'category': categories[g["cat"]],
                'developer': g["dev"],
                'year': 2020,  # Placeholder year
                'description': f"Una increíble entrega en la saga de {g['saga']}. Explora niveles fascinantes en este título de {g['cat']}."
            }
        )
        if created:
            count += 1
            print(f"Juego agregado: {g['title']}")

    print(f"¡Base de datos poblada exitosamente! Se agregaron {count} juegos.")

if __name__ == '__main__':
    populate()
