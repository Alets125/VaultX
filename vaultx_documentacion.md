# ◈ VaultX — Catálogo de Videojuegos

![VaultX Banner](./docs/banner.png) *(Reemplazar con captura real)*

## 🎯 Objetivo del Proyecto
VaultX es una aplicación web dinámica diseñada para servir como un catálogo interactivo y moderno de videojuegos. Su objetivo principal es ofrecer una experiencia de usuario altamente visual, inspirada en interfaces futuristas y cyberpunk (estilo "Selección de Personajes" de Valorant). Permite a los usuarios explorar, filtrar y visualizar detalles técnicos y estadísticas de una colección curada de videojuegos.

## ✨ Descripción de Funcionalidades
- **Pantalla de Bienvenida (Splash Screen):** Interfaz inmersiva tipo "Press Start" antes de acceder al contenido principal.
- **Catálogo Interactivo:** Cuadrícula inferior de juegos con *scroll* horizontal fluido.
- **Panel de Detalles Dinámico:** Al seleccionar un juego, la información (título animado tipo "Decode", estadísticas de intensidad/velocidad en barras de progreso, descripción y portada) se actualiza instantáneamente en el panel superior sin recargar la página.
- **Filtros por Categoría:** Navegación optimizada mediante categorías dinámicas (RPG, Shooter, Survival Horror, etc.).
- **Panel de Administración:** Acceso seguro para administradores para gestionar (Añadir/Editar/Eliminar) el catálogo de juegos de forma remota.
- **Almacenamiento en la Nube:** Las portadas de los juegos se optimizan y sirven directamente desde *Cloudinary*.

## 🛠️ Tecnologías Utilizadas
### Backend
- **Python 3.11**
- **Django 5.x** (Framework web principal)
- **PostgreSQL** (Base de datos de producción vía Neon)
- **SQLite** (Base de datos local)
- **dj-database-url** (Manejo dinámico de conexiones a bases de datos)

### Frontend
- **HTML5 & CSS3 Vanilla** (Diseño Glassmorphism, animaciones *Matrix Rain*, Flexbox).
- **JavaScript (ES6)** (Manipulación del DOM y lógica de animaciones asíncronas).
- **WhiteNoise** (Gestión ultrarrápida de archivos estáticos en producción).

### Despliegue & Nube
- **Vercel** (Hosting Serverless y CI/CD)
- **Neon** (Base de Datos PostgreSQL en la nube)
- **Cloudinary** (Hosting de archivos multimedia / Media Storage)

## 🔗 Rutas y "Endpoints" Principales

| Ruta | Descripción |
|------|-------------|
| `/` | **Splash Screen:** Pantalla de bienvenida interactiva. |
| `/catalog/` | **Catálogo:** Vista principal con la cuadrícula de juegos y el panel de detalle. Acepta el parámetro `?cat=slug` para filtrar. |
| `/login/` | **Acceso:** Interfaz de inicio de sesión segura para administradores. |
| `/admin/` | **Panel de Control:** Gestor interno de Django para administrar la base de datos (Juegos y Categorías). |

## 🚀 Instrucciones de Instalación y Ejecución (Local)

### Requisitos Previos
- Python 3.10+
- Git

### Pasos
1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Alets125/VaultX.git
   cd VaultX
   ```

2. **Crear y activar el entorno virtual**
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Mac/Linux:
   source .venv/bin/activate
   ```

3. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar las Variables de Entorno**
   Crea un archivo llamado `.env` en la raíz del proyecto y añade:
   ```env
   DEBUG=True
   SECRET_KEY=tu_clave_secreta_local
   CLOUDINARY_CLOUD_NAME=tu_cloud
   CLOUDINARY_API_KEY=tu_api_key
   CLOUDINARY_API_SECRET=tu_api_secret
   ```

5. **Aplicar Migraciones**
   ```bash
   python manage.py migrate
   ```

6. **Poblar la base de datos base (Opcional)**
   ```bash
   python populate_db.py
   ```

7. **Ejecutar el Servidor**
   ```bash
   python manage.py runserver
   ```

## 🌐 URL Pública del Proyecto
**👉 [https://vaultx.vercel.app](https://vaultx.vercel.app) 👈** *(Reemplazar con tu URL exacta de Vercel)*

## 📸 Capturas de Pantalla del Sistema

### Pantalla de Bienvenida
![Welcome Screen](./docs/welcome.png)

### Catálogo Principal
![Main Catalog](./docs/catalog.png)

### Acceso de Administrador
![Login](./docs/login.png)
