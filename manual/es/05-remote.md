<!-- translated from zh-TW at commit 968641f -->

# 5. Disparo remoto y control

| Método | Conexión | Vista en vivo | Nivel |
|---|---|---|---|
| [Disparo remoto](#disparo-remoto-pro) | Wi‑Fi o USB | ✅ | Pro |
| [Control remoto Bluetooth](#control-remoto-bluetooth-gratis) | Bluetooth | ❌ | Gratis (disparo a intervalos es Pro) |
| [Monitor de vídeo](#monitor-de-vídeo-cine) | USB (Wi‑Fi experimental) | ✅ Específico para vídeo | Cine |

---

## Disparo remoto (Pro)
Ve la imagen en vivo de tu cámara en el teléfono, toca para enfocar, cambia ajustes y haz fotos o vídeos. Funciona **por Wi‑Fi y por USB**, pasando automáticamente a USB al enchufar el cable.

**Requisitos**
1. Modelos con «Tipo de conexión» en su menú — consulta [Cámaras compatibles](README.md#cámaras-compatibles).
2. Por Wi‑Fi, pon el «Tipo de conexión» de la cámara en **Control de la cámara** — consulta [Conectar la cámara](02-connect.md#tipo-de-conexión-connection-type-de-la-cámara). Si sigue en «Transferencia de imágenes», la app muestra los pasos para cambiarlo y reconecta sola después.

El disparo remoto ocupa toda la pantalla ocultando las pestañas inferiores. Toca **←** arriba a la izquierda o el botón Atrás del teléfono para volver a Inicio.

📷 Captura de pantalla: disparo remoto (vertical y horizontal)

### Distribución de la pantalla
| Zona | Contenido |
|---|---|
| Arriba | Ajustes de cámara: Modo, Velocidad, Diafragma, ISO, ISO auto, Compensación de exposición, Balance de blancos, Modo de enfoque, Zona AF, Medición, Picture Control, Calidad. En vertical van en dos filas; en horizontal en una fila desplazable |
| Tercera fila superior | Volver, Grabar vídeo, Vista limpia, Bloquear pantalla, Destino de guardado, Batería |
| Centro | Vista en vivo completa sin recorte, con recuadro de enfoque, nivel, exposímetro y guías superpuestas |
| Abajo | 6 interruptores rápidos (personalizables) + «Más» |
| Abajo del todo | «Disparo» (elegir método), Disparador, botón AF, miniatura de última foto y disparos restantes |

En horizontal, los interruptores pasan a la franja negra izquierda y el disparador queda abajo a la derecha. El **modo zurdo** (**Ajustes → Disparo**) mueve el disparador abajo a la izquierda.

### Ajustar parámetros de la cámara
Toca cualquier valor arriba para abrir abajo una barra de ajuste sin tapar la imagen en vivo.
- El modo de exposición es solo informativo (cambia P / S / A / M en la cámara). La velocidad se ajusta en S y M; el diafragma en A y M.
- Con ISO auto activado, ISO muestra `AUTO`. Junto a compensación de exposición tienes `0` para ponerla a cero al instante.
- Al elegir `K` en balance de blancos puedes ajustar la temperatura de color exacta. Picture Control muestra el nombre activo en la cámara, incluidos los personalizados.
- Si algo **no se puede ajustar**, la app explica el motivo. En cámaras con diales físicos como Zf y Zfc, pon el dial de velocidad en **1/3 STEP** y el dial ISO en **C**.

### Enfoque y disparador
- **Tocar para enfocar**: toca donde quieras en la imagen para enfocar allí. Pon la zona AF de la cámara en un modo con punto desplazable (como AF de punto único); en zona automática decide la cámara.
- Se dibuja el recuadro de enfoque real de la cámara (punto único, zona dinámica, zona automática y seguimiento): verde si enfoca bien, rojo si falla.
- **Disparador**: un toque dispara; **mantener pulsado = pulsar a la mitad para enfocar** (borde verde) y al soltar dispara.
- **Botón AF**: vuelve a enfocar en el punto actual.
- **Enfocar antes de disparar** (activado por defecto): desactívalo para disparar al instante sin esperar al AF (más rápido con enfoque manual o ya enfocado).
- **Tocar pantalla para disparar**: al activarlo, tocar la imagen enfoca en ese punto y hace una foto al momento.
- Los toques en los bordes izquierdo y derecho (zona del gesto Atrás de Android) no mueven el enfoque para evitar fallos al deslizar.

### Interruptores inferiores (personalizables)
Por defecto son Peaking, Cebra, Nivel, Cuadrícula, Zoom y un hueco libre; el último a la derecha es siempre «Más».
- **Un toque** activa o desactiva; **mantener medio segundo** abre opciones detalladas (sensibilidad de peaking, umbral de cebra, tipo de cuadrícula, aumento de zoom).
- **Personalizar**: icono de engranaje arriba a la derecha de «Más». Puedes poner: Peaking, Cebra, Nivel, Cuadrícula, Zoom, Histograma, Exposímetro, Tocar y disparar, Enfocar antes de disparar, Copiar al teléfono, Captura, Modo noche estrellada, Vista previa en vivo y Temporizador.

### Cajón «Más»
«Más» abre un panel semitransparente (desde abajo en vertical, desde un lado en horizontal) manteniendo siempre visible la escena. Tiene tres pestañas:
- **Ayudas**: Vista previa en vivo, Peaking, Aviso de sobreexposición (cebra), Nivel, Líneas de cuadrícula, Histograma, Exposímetro, Lupa de enfoque, Modo noche estrellada.
- **Disparo**: Enfocar antes de disparar, Tocar pantalla para disparar, Zona AF, Copiar cada foto al teléfono, Captura de vista previa.
- **Herramientas**: Superposición fantasma, Lista de comprobación multidisparo, Consejos.

### Ayudas de disparo (solo se ven en el teléfono, no afectan a la foto)
| Ayuda | Descripción |
|---|---|
| Nivel | Lee el sensor de inclinación de la cámara; se pone verde por debajo de 0,5° y muestra inclinación lateral y cabeceo |
| Histograma | Toca para alternar entre «Luminancia + RGB superpuesto» y «RGB separado» |
| Cebra (sobreexposición) | Marca con rayas diagonales las zonas que superan el umbral de brillo: 85 / 90 / 95 / 100 % (95 % por defecto) |
| Focus peaking | Colorea los bordes enfocados (rojo, amarillo, azul, blanco) con sensibilidad baja / media / alta para enfoque manual |
| Exposímetro | Indicador vertical estilo visor Nikon en pasos de 1/3 EV. En modo M muestra la desviación respecto a la medición; en P / A / S la compensación |
| Líneas de cuadrícula | Regla de los tercios, cuadrícula 4×4, Proporción áurea, Espiral áurea, Diagonales, Cruz central |
| Zoom | Si la cámara lo admite (como la Zf), **la propia cámara amplía la imagen** mostrando píxeles reales al 50 % / 100 % / 200 % / 400 %. Toca o usa ◀ ▲ ▼ ▶ para moverte y `Cerca ◀◀ ◀ ▶ ▶▶ Lejos` abajo para ajuste fino de enfoque manual. En otros modelos usa zoom digital de la app (2× / 4× / 8×) |

> La vista previa es una imagen comprimida de la cámara; estas ayudas son orientativas. Para exposición crítica fíate siempre del histograma de la foto final.

### Métodos de disparo
Toca **Disparo** junto al disparador para elegir. Al seleccionarlo, el botón se pone amarillo y sale una barra encima del disparador (por ejemplo, `Disparo a intervalos · Cada 5 s · 10 fotos`). Tócala para ajustar parámetros y pulsar **Iniciar**, o toca × para volver al disparo normal. En marcha muestra el progreso arriba y **Detener** para cancelar cuando quieras.

| Método | Ajustes | Descripción |
|---|---|---|
| Disparo normal | 1–9 fotos | Con temporizador, tras la cuenta atrás dispara una serie de N fotos (con ~1 s entre ellas) |
| **Temporizador** | Desactivado, 2, 5, 10 s | Arriba del todo en «Disparo»; sirve para cualquier método y para vídeo. Muestra números grandes en el centro; vuelve a pulsar el disparador para cancelar |
| Bulb | 1–3600 s | La cámara debe estar en modo M con velocidad en Bulb o Time; termina sola al cumplirse el tiempo |
| Disparo a intervalos (Interval timer shooting) | 2–999 fotos, intervalo 1–3600 s | Dispara a intervalos fijos y muestra el tiempo total; combínalo con «Copiar cada foto al teléfono» para revisar un time-lapse |
| Horquillado de exposición | 3 / 5 / 7 / 9 fotos, paso 0,3–3,0 EV | Varía la exposición alrededor del valor actual y al acabar restaura el original |
| Disparo con desplazamiento de foco (Focus shift shooting) | 2–300 fotos, ancho de paso | Enfoca primero el punto más cercano y va moviendo el enfoque hacia infinito en cada toma. Requiere objetivo AF; el apilado se hace luego en ordenador |
| Panorámica | Rejilla o «Libre» | Haz varias tomas solapadas para unirlas en panorámica — ver más abajo |
| Shake (reducción de ruido) | 4 u 8 fotos | Ráfaga rápida a pulso para fusionarlas en una imagen con menos ruido — ver más abajo |

> Mientras funciona una herramienta multidisparo, el AF y el enfoque táctil se pausan. Al salir del disparo remoto se pide confirmación.

#### Panorámica (unión)
- **Rejilla**: elige tamaño y AeroCam calcula cuántos grados girar en cada casilla mientras mueves la cámara y disparas. Indica si el solapamiento basta («Listo para disparar / Puedes girar más / Puede faltar solapamiento») y superpone semitransparente el borde de la foto anterior para alinear.
- **Libre**: sin rejilla fija; basta con solapar cada foto un 30 % con la anterior en cualquier dirección (hasta 30 fotos).
- Con 2 o más fotos ya puedes tocar **Unir** para crear la panorámica en el teléfono; si das una vuelta completa genera 360°. El resultado sale nivelado gracias al sensor de nivel registrado al disparar.
- Las fotos quedan agrupadas en una pila en Fotos del teléfono para poder volver a unirlas más adelante — consulta el [Capítulo 6](06-edit.md#procesamiento-de-imagen-unión-panorámica-y-reducción-de-ruido-pro).

#### Shake (reducción de ruido)
- Permite lograr «mejora de calidad por multidisparo» en cámaras sin desplazamiento de píxel: haz 4 u 8 fotos a pulso (o trípode) y la app las alinea y promedia reduciendo el ruido a un tercio aprox. (con 8 fotos) sin perder detalle.
- Se procesa automáticamente en segundo plano («Fusionando %») y se guarda como `SHAKE_<hora>.JPG` a tamaño completo y con datos EXIF.
- Los elementos en movimiento (coches, personas, hojas) toman solo la foto más nítida para evitar fantasmas, y las tomas muy movidas se descartan solas.
- Ideal para escenas nocturnas, interiores oscuros e ISO alto.

### Superposición fantasma (Pro)
**Más → Herramientas → Superposición fantasma**: coloca una imagen de referencia en **superposición semitransparente** o **pantalla dividida** sobre la vista en vivo, con control de opacidad y «Capturar pantalla actual». Muy útil para repetir encuadres, reproducciones y alineaciones.

### Otras funciones
- **Copiar cada foto al teléfono**: guarda según tus reglas de recepción, incluido «Guardar solo JPEG de RAW».
- **Última foto**: la miniatura inferior derecha muestra la última toma con su velocidad, diafragma e ISO reales; tócala para ver todas las de esta sesión y guardar originales o JPEG en el teléfono.
- **Vista limpia**: deja solo la vista en vivo; toca el botón tenue de la esquina para recuperar controles. **Bloqueo**: evita toques accidentales; mantén pulsado en cualquier parte para desbloquear.
- **Grabar vídeo**: botón superior de grabación. Cambia la cámara a «modo aplicación» antes de empezar (necesario en Zf) y vuelve al parar; si no puede grabar explica por qué. Por USB conviene usar el [Monitor de vídeo](#monitor-de-vídeo-cine).
- **Captura de vista previa**: guarda el fotograma en `Pictures/AeroCam/Snapshots/` (calidad de vista previa).
- **Disparo remoto USB**: imagen más fluida que Wi‑Fi (30 fps por defecto, ajustable a 60 fps o sin límite), con vista previa de alta resolución opcional y fps reales abajo a la derecha. Configurable en **Ajustes → Disparo**.
- La pantalla se mantiene encendida por defecto durante el disparo remoto.

---

## Control remoto Bluetooth (gratis)
Sin Wi‑Fi y sin vista en vivo. Inicio → tarjeta Bluetooth → **Control remoto Bluetooth**. Requiere [vinculación Bluetooth](02-connect.md#vinculación) previa.
- Un toque en el disparador hace una foto; mantenerlo pulsado usa la ráfaga de la cámara (CL / CH).
- Mantén AF y pulsa el disparador para disparos rápidos seguidos, o usa ráfaga de 3 / 5 fotos.
- Botón AF: mantener para enfocar. La cámara debe permitir enfocar al pulsar el disparador a la mitad (si usas AF‑ON trasero, revisa los ajustes personalizados de la cámara).
- Temporizador (cuenta atrás), iniciar/detener vídeo y contador de fotos restantes.
- El **disparo a intervalos** es Pro.

📷 Captura de pantalla: pantalla de control remoto Bluetooth

---

## Monitor de vídeo (Cine)
Convierte tu teléfono en un monitor de campo para vídeo. Al conectar por USB, la sección USB de Inicio muestra **🎥 Monitor de vídeo** (máxima fluidez, hasta ~60 fps); la versión Wi‑Fi está en la sección Wi‑Fi como función experimental.
- En la Zf pon el selector foto/vídeo en **Vídeo**.
- **Arriba**: tiempo `● REC`, formato de vídeo (por ejemplo, `1080 60p`; toca para cambiar), tipo de archivo (por ejemplo, `H.265 10bit`; N‑Log requiere H.265 de 10 bits), tiempo restante de grabación y batería.
- **Abajo**: velocidad, diafragma, ISO, ISO auto, compensación de exposición, balance de blancos, enfoque y medición propios de vídeo (el ISO de vídeo solo actúa en modo M).
- **Botón de grabación**: grabando hay que **mantenerlo 1 segundo** (hasta completar el anillo rojo) para parar y evitar cortes accidentales. Pulsar Atrás grabando pide confirmación.
- **Herramientas**: exposímetro, histograma, forma de onda / desfile RGB, color falso, cebra (con segundo umbral para tonos de piel), focus peaking, cuadrículas, marcos de seguridad, máscaras de aspecto (`2.39:1`, `1.85:1`, `16:9`, `9:16`, `4:5`), marco rojo Tally y ángulo de obturación.
- **LUT** (Android 13+): aplica un LUT de monitorización a la vista previa (conversión N‑Log integrada o importación de `.cube`) sin grabarlo en el vídeo. Desactiva **Asistencia de visualización** (View assist) en la cámara para no aplicarlo dos veces.
- **Descompresión anamórfica** (`1.33x`–`2.0x`), **enfoque progresivo A/B** (fija dos puntos de enfoque y desplaza el foco suavemente entre ellos) y **superposición fantasma**.
- Por defecto se desactiva tocar para enfocar durante la grabación (para no grabar cambios de foco), aunque puede activarse en el menú.
- **Capturas**: «Captura de vista previa» guarda solo la imagen limpia; «Captura (con ayudas)» incluye LUT, cebra, color falso y máscaras.

📷 Captura de pantalla: pantalla de monitor de vídeo

---

## Modo noche estrellada (gratis)
Al fotografiar estrellas los ojos necesitan adaptarse a la oscuridad y la luz blanca contrae las pupilas. Este modo tiñe toda la app de rojo oscuro.
1. Activar: **Ajustes → Apariencia e idioma → Tema → «Noche estrellada (luz roja)»**, o desde los interruptores inferiores / **Más → Ayudas** en Disparo remoto.
2. Si quieres aún menos brillo: activa **Brillo mínimo de pantalla de la app**.
3. Para ver los colores reales de una foto: **mantén pulsado «Mantener para ver color original»** y suelta para volver al rojo. Disponible en Disparo remoto, Monitor de vídeo y vista en grande.
4. Solo cambia la visualización en pantalla; las fotos no se alteran. Al compartir por código QR vuelve temporalmente a color normal para que puedan escanearlo.
