### Descripción del Proyecto

Este proyecto es un sitio E-commerce funcional construido con Django. El sitio, llamado "Aiwbrify", es una tienda de vinilos que permite a los usuarios visualizar productos, navegar por categorías de artistas y ver los detalles de cada producto.

El panel de administración de Django se utiliza para toda la gestión de productos (CRUD).

---

### Instrucciones de Instalación y Ejecución

Para ejecutar este proyecto en un entorno local, sigue estos pasos:

1.  **Clonar el repositorio:**

    ```bash
    git clone [https://github.com/Ewniah/Evaluacion2-Backend-BryanAlegria.git]
    ```

2.  **Navegar a la carpeta del proyecto:**

    ```bash
    cd Evaluacion2-Backend-BryanAlegria
    ```

3.  **Crear y activar un entorno virtual:**

    ```bash
    # Crear el entorno
    python -m venv venv

    # Activar en Windows (CMD)
    .\venv\Scripts\Activate.bat
    ```

4.  **Instalar las dependencias:**
    Todas las librerías necesarias (Django, Pillow, etc.) se instalarán con este comando.

    ```bash
    pip install -r requirements.txt
    ```

5.  **Ejecutar las migraciones:**
    Este comando creará la base de datos `db.sqlite3` con la estructura de tablas correcta.

    ```bash
    python manage.py migrate
    ```

6.  **Ejecutar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

El sitio estará disponible en `http://127.0.0.1:8000/`.

---

### Acceso y Credenciales Obligatorias

- **Página de Inicio:** `http://127.0.0.1:8000/`
- **Panel de Administración:** `http://127.0.0.1:8000/admin/`

Las credenciales para acceder al panel de administración:

- **Usuario:** `ES02`
- **Contraseña:** `pbe-es-02`

---

### Requerimientos Funcionales Implementados

- **Estructura de Datos:** El modelo `Producto` incluye nombre, precio, stock, descripción e imagen.
- **Página Principal y Navegación:** El sitio muestra todos los productos y permite la navegación por categorías a través de un menú.
- **Páginas por Categoría:** Al seleccionar un artista, se muestran únicamente los productos de esa categoría.
- **Página de Detalle:** Cada producto tiene una página de detalle individual con toda su información.
- **Gestión desde el Administrador:** Se permite insertar, modificar o eliminar productos desde el panel de Django. Los modelos se visualizan en columnas por sus atributos.
