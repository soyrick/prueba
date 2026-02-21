# Fundamentos de HTML

Este repositorio contiene material y ejemplos básicos para aprender y practicar HTML. El objetivo de este proyecto es servir como base didáctica para crear páginas estáticas sencillas, experimentar con estructura de documentos, y gestionar recursos estáticos como imágenes.

## Contenido y propósito

- **Propósito:** Proveer ejemplos sencillos y notas para quien está empezando con HTML.
- **Audiencia:** Estudiantes, autoaprendizaje y ejercicios prácticos.

## Estructura del proyecto

La carpeta principal para este módulo es la carpeta donde se encuentra este archivo.

- **blog.html**: Página de ejemplo que ilustra estructura básica de un blog (encabezados, párrafos, enlaces, imágenes).
- **notes.txt**: Notas rápidas, recordatorios o apuntes relacionados con los ejercicios.
- **imagenes/**: Carpeta donde se almacenan los recursos gráficos (fotos, iconos, imágenes usadas en `blog.html`).

Ruta del README dentro del proyecto: [html.fundamentos/README.md](html.fundamentos/README.md)

## Cómo ver el proyecto localmente

1. Abrir `blog.html` en un navegador moderno (Chrome, Firefox, Edge, Safari).
   - Doble clic en `blog.html` o usar el menú `Abrir con...`.

2. (Recomendado) Usar un servidor local para evitar problemas con rutas relativas o políticas de seguridad del navegador. Desde PowerShell o CMD, ejecutar:

    cd html.fundamentos
    python -m http.server 8000

Luego abrir `http://localhost:8000/blog.html` en el navegador.

Si no tiene Python instalado, puede instalar la extensión Live Server en Visual Studio Code y usarla para servir la carpeta.

## Convenciones y buenas prácticas

- **Codificación:** Usar UTF-8 para archivos HTML y de texto.
- **Estructura semántica:** Emplear etiquetas semánticas (`header`, `main`, `article`, `footer`) cuando sea posible.
- **Rutas relativas:** Referenciar imágenes y recursos con rutas relativas (ej. `imagenes/mi-foto.jpg`) para mantener portabilidad.
- **Imágenes optimizadas:** Comprimir imágenes antes de añadirlas para reducir tamaño y acelerar carga.

## Edición y flujo de trabajo sugerido

- Abrir la carpeta en Visual Studio Code: `Archivo > Abrir carpeta...` y seleccionar `html.fundamentos`.
- Hacer cambios en `blog.html` y probar en el navegador.
- Mantener las notas en `notes.txt` con ideas, errores encontrados o pendientes.

Comandos útiles (PowerShell):

    # Abrir VS Code en la carpeta actual
    code .

    # Iniciar servidor simple con Python
    python -m http.server 8000

## Cómo contribuir

- Hacer una copia local del repo y editar los archivos en `html.fundamentos`.
- Añadir nuevas páginas o ejemplos dentro de la carpeta `html.fundamentos`.
- Mantener la estructura y documentar cambios en `notes.txt` o creando nuevos archivos `README` en subcarpetas si hace falta.

Si desea que revise o añada ejemplo(s) adicionales (plantillas, CSS básico, o ejemplos de formularios), abra un issue o pídamelo directamente.

## Licencia

Este repositorio no incluye una licencia explícita por defecto. Si desea añadir una licencia (por ejemplo, MIT), puedo generarla. Indique cuál prefiere.

## Autor y contacto

- Autor: propietario del repositorio (local).
- Contacto: puede añadirse aquí si necesita que yo incorpore un bloque con nombre y correo.

## Notas finales

- Este proyecto está diseñado para ser simple y pedagógico. Si quiere que lo amplíe con CSS, JavaScript o una guía de ejercicios paso a paso, dígame y lo añado.
