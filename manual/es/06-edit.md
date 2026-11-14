<!-- translated from zh-TW at commit 968641f -->

# 6. Edición de fotos y estilos

## Editor de fotos (gratis)
Abre una foto en grande en **Fotos del teléfono** → **Editar**. Abajo hay tres pestañas: **Recortar**, **Ajustar** y **.np3**.

📷 Captura de pantalla: editor (Recortar, Ajustar, .np3)

### Recortar
- Proporciones: Original, Libre, 1:1, 4:5, 3:2, 16:9 y formatos de cine 1.66, 1.85, 2, 2.20 y 2.39. Las fotos verticales usan orientación vertical automáticamente.
- Arrastra dentro del marco para moverlo y tira de las esquinas para cambiar su tamaño.
- Enderezar ±45° y girar 90° (`↺`).

### Ajustar
Una fila de herramientas; toca una para ajustarla con la regla graduada y pulsa «Listo» para volver (las modificadas muestran un puntito):
- **Luz**: Exposición, Contraste, Altas luces, Sombras, Blancos, Negros.
- **Color**: Temperatura, Tinte, Saturación, Intensidad.
- **Detalle**: Claridad, Nitidez, Viñeta.

Regla graduada: al deslizar se detiene en pasos enteros (0,1 EV en exposición, 1° en enderezar, 1 en el resto) con una leve vibración; mantén pulsados los extremos para subir o bajar continuo; toca el número para escribirlo; toca dos veces o pulsa `↺` para volver a cero.

### Controles comunes
- **↶ ↷** Deshacer / Rehacer.
- Mantén pulsado **Original** para ver la foto sin editar.
- **◧ Comparar**: línea divisoria izquierda/derecha entre original y editada; el zoom con dos dedos va sincronizado en ambos lados.
- Abajo a la derecha puedes desplegar «Histograma».

### Guardado
- Originales de cámara (que siguen en la tarjeta): **al guardar se reemplaza la foto del teléfono**, pero la app conserva una copia del original durante 7 días con la opción «Restaurar original» en la vista en grande. Si la cámara no está conectada, pregunta antes si quieres «Reemplazar» o «Guardar como copia».
- Las fotos que solo están en el teléfono (sin tarjeta, panorámicas, fusiones Shake) se guardan siempre como archivo nuevo acabado en `_E`.
- Conserva los metadatos EXIF con calidad 95. Si el guardado se interrumpe, se completa solo la próxima vez que abras la app.
- El filtro **Editadas** en Fotos del teléfono muestra las fotos editadas, con un pequeño `✎` abajo a la izquierda de la miniatura.
- Al editar una copia comprimida (`JPEG.S`), recuerda que es mejor editar el original de cámara para lograr mayor calidad.
- Los vídeos no se pueden editar.

---

## Editar RAW en el teléfono (experimental)
Los archivos NEF también se abren en este editor y se guardan al lado como `DSC_xxxx_E.JPG` (al volver a guardar se actualiza ese mismo archivo); **el NEF original nunca se modifica** y conserva sus datos EXIF.
- **NEF con compresión sin pérdidas**: se revela directamente en el teléfono usando el balance de blancos de la cámara.
- **NEF Alta eficiencia / Alta eficiencia★**: el teléfono no puede decodificar esa compresión, así que edita el JPEG a tamaño completo incrustado dentro del NEF. Arriba verás «JPEG incrustado 8 bits» y «Estilo de cámara aplicado: xxx».
- Los archivos que solo tienen una miniatura pequeña sin JPEG completo no se pueden editar (la app explica por qué).

### RAW editable en el teléfono (cambiar compresión RAW de la cámara)
Para que los próximos NEF puedan revelarse completos en el teléfono, puedes cambiar la cámara a «Compresión sin pérdidas» desde el móvil:
- Acceso: «Hacer RAW sin pérdidas la próxima vez» en el aviso de Alta eficiencia del editor, o tocando la etiqueta de calidad arriba a la derecha de la tarjeta de memoria en Inicio (disponible cuando la cámara dispara en RAW).
- Siempre pide confirmación antes; escribe en la cámara, vuelve a leer para comprobar y muestra cómo cambian los disparos restantes (al ocupar más el RAW sin pérdidas, caben algo menos).
- La app recuerda el ajuste anterior de esa cámara para poder restaurarlo después; si ya lo cambiaste tú en la cámara, no lo sobrescribe.

---

## Vista previa de estilos .np3 (gratis)
En la pestaña **.np3** del editor puedes aplicar archivos Nikon Picture Control (`.np3`, `.ncp`) a una foto para ver el efecto en el teléfono.
- Toca un estilo para aplicarlo, ajusta la intensidad del 0 al 100 % y afina luego en «Ajustar».
- Desliza a izquierda/derecha sobre la foto para cambiar de estilo y mantén pulsado para ver el original. Debajo tienes `★` Favoritos y Recientes.
- **Todos N ▴** despliega la biblioteca completa de estilos (ver abajo) con búsqueda y filtros.
- Simula curvas y saturación: los archivos con curva usan su propia curva; los creados con controles deslizantes Flexible Color (marcados como «Tono por deslizadores») usan curvas calculadas a partir de mediciones reales en NX Studio. **El mezclador de color y la gradación de color aún no se simulan**, por lo que el resultado es aproximado.
- Funciona mejor en NEF; si el JPEG ya llevaba un Picture Control aplicado al disparar, los efectos se suman y la app te avisa.

📷 Captura de pantalla: pestaña .np3

---

## Estilos de cámara C1–C9 (Pro)
Gestiona desde el teléfono los Picture Control personalizados C1–C9 de la cámara. Entra desde la tarjeta **Estilos de cámara** en Inicio (requiere conexión Wi‑Fi o USB).
- Cada ranura muestra vista previa, nombre e indicadores de activo, con curva o Flexible Color.
- **Toca una ranura** para elegir un estilo de la biblioteca y grabarlo en la cámara; tras escribirlo lo vuelve a leer para comprobarlo y marca `✓` si coincide. **Mantén pulsado** o toca `⋮` para vaciarla. Si se está recibiendo una foto, espera a que termine antes de grabar.
- Solo se comunica con la cámara al abrir esta pantalla, tocar `↻`, grabar o vaciar; Inicio muestra lo último leído y la hora.
- Abajo aparecen en solo lectura las 9 recetas de Nikon Imaging Cloud (se añaden desde Nikon Imaging Cloud).

### Qué se graba en la cámara
Las ranuras personalizadas de la cámara admiten **Picture Control base + valores de ajuste**, no el archivo `.np3` completo:
- Con **＋ Nuevo estilo** en la biblioteca eliges base (Estándar, Plano, Creative Picture Control…) y ajustas Nitidez, Claridad, Contraste, Brillo, Saturación y Tono.
- **Grabar `.np3` / `.ncp` en la cámara (aproximado)**: los archivos con curva y los de «Tono por deslizadores» (convertidos a curva) graban **Nombre + Curva + Enfoque (Nitidez, Nitidez de rango medio, Claridad)** en la ranura C con la base que elijas. **Saturación, mezclador de color y gradación de color no se pueden enviar por conexión**; antes de grabar verás todos los valores del archivo y qué partes no se transferirán.
- Para lograr el efecto completo, copia el `.np3` a una tarjeta de memoria e impórtalo desde el menú de la cámara.

### Biblioteca de estilos
- Hasta 256 estilos, compatible con `.np3` y `.ncp`.
- Búsqueda `🔍`, filtros (Todos, `★`, Recientes, Con curva, En cámara, Grabables) y **＋ Nuevo**.
- Cada estilo muestra una miniatura usando la imagen de referencia que importes (`＋ → «Imagen de referencia de vista previa…»`) o una carta de color si aún no has puesto ninguna.

📷 Captura de pantalla: estilos de cámara C1–C9 y biblioteca

---

## Procesamiento de imagen: unión panorámica y reducción de ruido (Pro)
En Fotos del teléfono selecciona varias fotos y **desliza hacia arriba** la barra inferior (o toca el tirador) para abrir «Procesamiento de imagen».

### Unión (panorámica)
- Si seleccionas dentro de una pila «Panorámica»: las une según la posición de rejilla con la que se tomaron y guarda el resultado en esa misma pila como «Panorámica».
- Si eliges varias fotos solapadas en la galería normal: la app detecta sola cómo encajan y guarda el resultado en una pila nueva.
- Las fotos que no encajen no hacen fallar todo el grupo: une el bloque más grande posible y te indica qué archivos quedaron fuera. En panorámicas de rejilla, si falta una casilla no genera resultado para evitar huecos.
- Si completas una vuelta entera genera 360°; el resultado queda nivelado (gracias al nivel guardado al disparar), sin fantasmas y con datos EXIF.
- Consulta cómo dispararlas en el [Capítulo 5 Panorámica](05-remote.md#panorámica-unión).

### Reducción de ruido (Shake)
- Alinea y promedia las fotos elegidas reduciendo el ruido sin perder detalle; en zonas con movimiento usa una sola toma para evitar fantasmas.
- Si seleccionas dentro de una pila «Shake», guarda el resultado allí mismo («Fusionada»), o puedes tocar **Fusionar** / **Volver a fusionar** encima de la pila.
- Consulta cómo dispararlas en el [Capítulo 5 Shake](05-remote.md#shake-reducción-de-ruido).

> Solo se ejecuta una unión o fusión a la vez; verás el progreso en pantalla y al acabar podrás abrirla con un toque.
