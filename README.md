# NUTRICYT — sitio web

Sitio estático (HTML/CSS/JS puro, sin frameworks ni build step) para el consultorio de
nutrición de Shelsea García. Listo para subir por FTP/drag-and-drop a Hostinger o
cualquier hosting estático.

## Antes de publicar — edita esto

1. **Fotos.** Las fotos principales (hero, Sobre mí ×2, banda "¿Lista para empezar?",
   avatar de Contacto) ya son las reales. Las de `blog-*.jpg` siguen siendo ilustraciones
   genéricas — opcional sustituirlas por fotografía real de cada receta si quieres.

2. **Precios.** Busca `[PRECIO]` en `index.html` (una vez por tarjeta de servicio) y
   escribe el precio real de cada consulta, o quítalo si prefieres no mostrar precio.

3. **Correo de contacto.** En `lib/manifest.js`, cambia `contactEmail`. El formulario de
   contacto no tiene backend (sitio estático): al enviarlo, se abre el cliente de correo
   del visitante con el mensaje ya redactado. Si más adelante quieres que el formulario
   envíe sin abrir el correo, se puede conectar a un servicio como Formspree.

4. **Dirección y mapa.** En la sección Contacto y en el footer, busca
   `[DIRECCIÓN DEL CONSULTORIO]` y el comentario `EDITA AQUÍ` sobre el `<iframe>` del
   mapa: reemplaza el `bbox`/`marker` por la ubicación real (openstreetmap.org permite
   copiar ese enlace desde su propio botón "Compartir").

5. **WhatsApp.** El número (`18097499916`) está centralizado en `lib/manifest.js`
   (`whatsappNumber`) y se usa en el widget flotante, en los tres botones "Reservar
   consulta" (menú, portada) y en el botón de la sección Servicios. La reserva es 100%
   manual: el visitante escribe por WhatsApp y tú coordinas y confirmas la cita
   directamente con cada paciente (no hay Cal.com ni calendario en línea conectado).

## Estructura

```
index.html          página única (todas las secciones son anclas: #sobre-mi, #servicios…)
styles.css           todos los estilos
main.js              toda la lógica (sin dependencias externas)
lib/manifest.js       datos editables (WhatsApp, correo)
assets/img/           imágenes (las 5 principales ya son reales, ver arriba)
tools/gen_placeholders.py   script que generó los placeholders — no se usa en producción, puedes borrarlo
.htaccess             cache-control para Hostinger/Apache
```

## Vista previa local

```
python3 -m http.server 8765
```

y abre `http://localhost:8765/`.

## Notas técnicas

- Sin dependencias externas en tiempo de ejecución (no GSAP/Lenis): las animaciones de
  scroll usan `IntersectionObserver` nativo, con un timeout de seguridad de 6s por si
  algo falla.
- El sitio funciona con JavaScript desactivado: todo el contenido, precios, servicios y
  datos de contacto son visibles; solo se pierden las animaciones y el widget de chat.
- El widget de WhatsApp es una simulación 100% en el navegador (sin IA ni llamadas
  externas): detecta saludos por palabra clave y siempre ofrece un botón para continuar
  la conversación por WhatsApp real.
