<div style="display:flex;align-items:center;gap:12px">
    <h1 style="margin:0">🚀 Fundamentos de HTML</h1>
    <img alt="HTML5" src="https://img.shields.io/badge/HTML-%3E%3D5-orange" />
    <img alt="Learning" src="https://img.shields.io/badge/Level-Básico-brightgreen" />
</div>

Bienvenido a un conjunto de recursos y ejemplos pensados para aprender HTML creando páginas limpias, semánticas y visualmente atractivas.

**Vista previa rápida**

<div style="background:linear-gradient(135deg,#f8f4ff,#e3f7ff);border-radius:12px;padding:14px;margin:12px 0;box-shadow:0 6px 20px rgba(16,24,40,.08)">
    <strong>Archivo principal:</strong> <a href="blog.html">`blog.html`</a> — abre en el navegador o sirve localmente para ver el contenido.
</div>

**Índice**

- Descripción
- Estructura del proyecto
- Rápido inicio (local)
- Estética y recursos (tips)
- Ejemplos de uso y fragmentos
- Contribuir
- Licencia y contacto

## Descripción

Este proyecto es una base didáctica: páginas estáticas, ejemplos de marcado semántico y un sitio pequeño tipo blog para practicar. Ideal para estudiantes y proyectos personales.

## Estructura del proyecto

- `blog.html` — ejemplo de página (estructura, artículos, imágenes).
- `notes.txt` — apuntes, ideas y checklist de mejoras.
- `imagenes/` — recursos gráficos usados en `blog.html`.
- `style.css` — (opcional) archivo de estilos que puedes enlazar desde `blog.html`.

Ruta: [html.fundamentos/README.md](html.fundamentos/README.md)

## Rápido inicio (local)

1) Abrir `blog.html` directamente (doble clic) para una vista rápida.

2) Servir localmente (recomendado):

```powershell
cd html.fundamentos
python -m http.server 8000

# Luego abrir http://localhost:8000/blog.html
```

O usar la extensión Live Server en Visual Studio Code para recarga automática.

## Estética y recursos (hazlo llamativo)

- Paleta recomendada: un fondo suave con acentos vibrantes (#6C63FF, #00C2FF, #FF6B6B).
- Tipografía sugerida: `Inter`, `Poppins` o `Roboto` para un look moderno.
- Sombra y microinteracciones: usa `box-shadow` ligero y transiciones `all .2s ease`.

Ejemplo para enlazar `style.css` desde `blog.html`:

```html
<link rel="stylesheet" href="style.css">
```

Ejemplo CSS minimal para banner (añádelo a `style.css`):

```css
.hero{
    background: linear-gradient(90deg,#6C63FF 0%, #00C2FF 100%);
    color: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 8px 30px rgba(44, 64, 124, .15);
}
```

## Fragmentos útiles

- Botón con efecto hover:

```html
<button class="btn">Leer más</button>
```

```css
.btn{background:#FF6B6B;color:#fff;padding:.6rem 1rem;border-radius:8px;border:0;transition:transform .18s}
.btn:hover{transform:translateY(-3px)}
```

## Cómo contribuir

- Editar o añadir nuevas páginas dentro de la carpeta `html.fundamentos`.
- Añadir ejemplos de CSS o pequeños scripts y documentarlos en `notes.txt`.
- Si quieres puedo generar un `starter.css` o mejorar `blog.html` con un layout responsivo.

## Licencia

No hay licencia por defecto. Si deseas una, te puedo añadir una (por ejemplo MIT).

## Autor y contacto

- Propietario local del repositorio. Si quieres, indícame el nombre y correo y lo añado aquí.

---

¿Quieres que además genere un `style.css` de ejemplo con la paleta sugerida y un header `hero` listo para usar? Responde "sí" y lo creo en `html.fundamentos/style.css`.
