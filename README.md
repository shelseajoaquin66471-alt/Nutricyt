# NUTRICYT — sitio web

Sitio estático (HTML/CSS/JS puro, sin frameworks ni build step) para el consultorio de
nutrición de Shelsea García. Listo para subir por FTP/drag-and-drop a Hostinger o
cualquier hosting estático.

## Antes de publicar — edita esto

1. **Fotos reales.** Las imágenes en `assets/img/` son *placeholders* generados
   (fondo gris con silueta, o gráficos ilustrativos) para que el diseño se vea completo
   mientras tanto. Reemplaza cada archivo por la foto real **con el mismo nombre**:
   - `hero-frente-estetoscopio.jpg` → Foto 1 (cuerpo completo, frente, estetoscopio) — Hero
   - `closeup-lateral.jpg` → Foto 2 (close-up, mirando de lado) — Sobre mí
   - `retrato-bata-manos.jpg` → Foto 3 (sonrisa amplia de frente) — Contacto (avatar)
   - `mirada-lateral.jpg` → Foto 4 (mirando arriba/lado) — banda "¿Lista para empezar?"
   - `banquito-sentada.jpg` → Foto 5 (sentada en banquito) — Sobre mí
   - `servicio-*.jpg`, `blog-*.jpg`, `informe-isak.jpg` → opcional, puedes sustituirlas
     por fotografía real de cada servicio/receta o dejar las ilustraciones actuales.

2. **Enlaces de Cal.com.** Abre `lib/manifest.js` (o busca `[CAL_LINK_` en `index.html`)
   y reemplaza cada `[CAL_LINK_...]` por la URL real de reserva de ese servicio.

3. **Precios.** Busca `[PRECIO]` en `index.html` (una vez por tarjeta de servicio) y
   escribe el precio real de cada consulta.

4. **Correo de contacto.** En `lib/manifest.js`, cambia `contactEmail`. El formulario de
   contacto no tiene backend (sitio estático): al enviarlo, se abre el cliente de correo
   del visitante con el mensaje ya redactado. Si más adelante quieres que el formulario
   envíe sin abrir el correo, se puede conectar a un servicio como Formspree.

5. **Dirección y mapa.** En la sección Contacto y en el footer, busca
   `[DIRECCIÓN DEL CONSULTORIO]` y el comentario `EDITA AQUÍ` sobre el `<iframe>` del
   mapa: reemplaza el `bbox`/`marker` por la ubicación real (openstreetmap.org permite
   copiar ese enlace desde su propio botón "Compartir").

6. **WhatsApp.** El número (`18097499916`) está centralizado en `lib/manifest.js`
   (`whatsappNumber`) y se usa tanto en el widget flotante como en los botones de
   servicio.

## Estructura

```
index.html          página única (todas las secciones son anclas: #sobre-mi, #servicios…)
styles.css           todos los estilos
main.js              toda la lógica (sin dependencias externas)
lib/manifest.js       datos editables (WhatsApp, Cal.com, correo)
assets/img/           imágenes (placeholders a sustituir, ver arriba)
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
