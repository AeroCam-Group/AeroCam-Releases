<!-- translated from zh-TW at commit 968641f -->

# 3. Recepción automática y guardado

## Panel de la cámara
Al conectar la cámara, la tarjeta superior de Inicio muestra su estado en tiempo real:

| Elemento | Contenido |
|---|---|
| Modelo, objetivo | Por ejemplo, «Nikon Z f» y «NIKKOR Z 24–120 mm f/4» |
| Batería | Porcentaje (se pone rojo al 20 % o menos) |
| Conexión | Zona Wi‑Fi del teléfono, Mismo Wi‑Fi, Wi‑Fi de la cámara o USB |
| Tarjetas de memoria | Espacio usado/total y fotos restantes por tarjeta; las dos ranuras se muestran por separado |
| Calidad | Por ejemplo, `RAW` o `JPEG buena★ L`; se actualiza al instante si cambias la calidad o sacas/metes tarjetas |
| Destino de guardado | Por ejemplo, «Guardando en: tarjeta ✓» — consulta [Destino de guardado y disparar sin tarjeta](#destino-de-guardado-y-disparar-sin-tarjeta) más abajo |
| Transferencia | Estado actual, con «Historial ›» arriba a la derecha |
| Estilos de cámara | Últimas ranuras C1–C9 leídas — consulta el [Capítulo 6](06-edit.md#estilos-de-cámara-c1c9-pro) |

Los datos que la cámara no ofrece en su modo actual se ocultan. Al cambiar a «Control de la cámara» y entrar en Disparo remoto suelen leerse más parámetros.

### Gestionar cámaras
Despliega **Gestionar cámaras (n)** debajo del panel para editar, eliminar o añadir cámaras. La página «Detalles» de cada cámara muestra:
- Modelo, número de serie (cifras centrales ocultas; toca para ver completo), versión de firmware, **contador de disparos** y fecha de lectura.
- **Disparos mensuales**: gráfico de barras de los últimos 6 meses (con datos desde que empezaste a usar la app).
- Fecha, método, objetivo, batería y espacio libre en tarjeta de la última conexión.
- Número de archivos transferidos al teléfono, fecha de primera conexión y perfiles de red guardados.

El contador de disparos se lee de los metadatos de la foto más reciente en la tarjeta, así que debe haber al menos una foto en ella.

### Aviso de batería baja
Envía una notificación cuando la batería de la cámara baja del umbral (15 % por defecto). No volverá a avisar hasta que la batería suba al menos un 5 % por encima del umbral. Ajustable en **Ajustes → Recepción y notificaciones**.

📷 Captura de pantalla: panel de la cámara

---

## Recepción automática (Pro)
1. En Inicio, toca Wi‑Fi → **Iniciar recepción**. La app mantiene la conexión en segundo plano (visible en la barra de notificaciones).
2. Al reproducir fotos en la cámara, pulsa **i → Enviar a PC / Seleccionar para enviar** (Send to PC / Select to send; el nombre varía según el modelo) y las fotos pasarán al teléfono.

Si quieres que las fotos lleguen solas en el mismo instante en que disparas, usa [Recepción FTP](08-ftp.md). Con un cable USB enchufado, la recepción pasa automáticamente a USB.

### Pausar la recepción
Con la recepción automática Wi‑Fi activa, toca **⏸ Pausar** arriba a la derecha de la tarjeta «Transferencia» (o «Pausar» en la notificación) para pausar temporalmente:
- El Wi‑Fi sigue conectado; el Carrete y el Disparo remoto funcionan con normalidad.
- Las fotos pendientes se quedan en la cámara y se transferirán en orden en cuanto toques **Reanudar recepción**. La foto que esté a medias termina de transferirse primero.
- La recepción se reanuda sola si tocas Reanudar, detienes la recepción, cierras la app desde aplicaciones recientes, se corta el Wi‑Fi, apagas la cámara o enchufas un cable USB.

### Si se corta la conexión
- Si se pierde la conexión, AeroCam reconecta automáticamente. Tras varios intentos fallidos, vuelve a buscar por identificador de cámara para encontrarla aunque haya cambiado de IP.
- **La cámara pasa a enviar por Bluetooth**: como solo tiene un chip inalámbrico, apaga el Wi‑Fi mientras envía por Bluetooth. Inicio mostrará «La cámara está enviando fotos por Bluetooth… El Wi‑Fi se reconectará solo al terminar» y no lo cuenta como fallo.
- **El Carrete o el Disparo remoto toman prestada la cámara**: la cámara solo admite una conexión a la vez. Al abrir Carrete o Disparo remoto, la recepción automática cede la conexión y la retoma sola al salir.
- **Si no se encuentra la cámara por Wi‑Fi**: pasado el tiempo configurado (3 minutos por defecto), la recepción se detiene sola y te avisa para no gastar batería. Puedes cambiar el tiempo en **Ajustes → Recepción y notificaciones**.

---

## Reglas de recepción
Se configuran en **Ajustes → Recepción y notificaciones**. Wi‑Fi, USB y FTP siguen estas mismas reglas.

### Tipos de archivo a recibir
Elige qué guardar: Todos los archivos, Solo JPG, JPG + RAW, Fotos + vídeos o Personalizado (JPEG, RAW, HEIF, TIFF, Vídeo, Otros).

Además hay tres interruptores extra (Pro):

| Interruptor | Función |
|---|---|
| **Guardar solo JPEG de RAW** | Al recibir un RAW, extrae únicamente el JPEG a tamaño completo incrustado en el archivo (unos 2–5 MB en lugar de 20–50 MB de RAW) sin perder resolución y conservando todos los datos EXIF, guardado como `DSC_1234_S.JPG`. Ideal para redes sociales y revisión rápida |
| **Guardar JPEG comprimido** | Recomprime en el teléfono los JPEG que llegan de la cámara (`_S.JPG`, mismos píxeles, calidad según los ajustes de Galería) |
| **Reemplazar copia comprimida al llegar el original** | Borra la copia `_S.JPG` del teléfono en cuanto se guarda el JPEG original |

> Para recibir archivos RAW, pon la calidad de imagen de la cámara en RAW o RAW+JPEG y selecciona RAW+JPEG (no «Solo JPEG») en las opciones de envío de «Conectar a PC» de la cámara. El nombre del menú depende del modelo.

### Otras reglas
| Regla | Detalles |
|---|---|
| Modo de recepción | Continuo, o detenerse tras recibir un archivo |
| Vídeos grandes | Los vídeos que superen el límite (1024 MB por defecto) se omiten en la recepción automática, se marcan como «Filtrado» y se descargan a mano |
| Carpeta de guardado | Por cámara, Por fecha, Por cámara y fecha o Por tipo de archivo |
| Nombre de archivo | Nombre original (`DSC_1234.NEF`), con prefijo de fecha (`20261011_DSC_1234.NEF`) o prefijo de fecha y hora (`20261011_153012_DSC_1234.NEF`, útil para ordenar cronológicamente fotos de varias cámaras). Se aplica solo a archivos nuevos |

### Dónde se guardan los archivos
- Fotos: `Pictures/AeroCam/…`
- Vídeos: `Movies/AeroCam/…`
- Otros archivos: `Download/AeroCam/…`

Otras apps como Google Fotos los ven al momento. Si desinstalas y vuelves a instalar AeroCam, usa **Ajustes → Almacenamiento y batería → «Volver a escanear fotos del teléfono»** para recuperar en la galería las fotos guardadas antes.

### Detección de duplicados
- Comprueba número de serie de la cámara, nombre, tamaño, hora de captura y contenido del archivo. Los duplicados no se guardan dos veces y aparecen como «Duplicado» en el historial.
- Si borras una foto en el teléfono (incluso enviándola a la papelera) y la vuelves a pasar, AeroCam la guardará de nuevo.
- No hace falta detener y reiniciar la recepción para reenviar una misma foto.

### Cuando llega la misma foto por Bluetooth y por Wi‑Fi
Como el Wi‑Fi transfiere el archivo completo, tiene prioridad:
- Si llega primero por Wi‑Fi y luego por Bluetooth: la copia Bluetooth se descarta.
- Si llega primero por Bluetooth y después por Wi‑Fi, se aplica **Ajustes → Recepción y notificaciones → «Fotos ya recibidas por Bluetooth»**:
  - **Reemplazar por original al recibir por Wi‑Fi** (recomendado): guarda el archivo completo y borra la versión reducida de Bluetooth.
  - **No volver a descargar por Wi‑Fi**.
  - **Conservar ambas copias**.
- Los archivos RAW originales se guardan siempre.

---

## Destino de guardado y disparar sin tarjeta
Decide dónde van las fotos al pulsar el disparador. AeroCam detecta si hay tarjeta en la cámara y elige automáticamente:
- **Con tarjeta**: aplica **Ajustes → Disparo → Destino de guardado**:
  - **Tarjeta de memoria**: guarda en la tarjeta de la cámara.
  - **Tarjeta + teléfono** (Pro): guarda en la tarjeta y copia a la vez en el teléfono.
- **Sin tarjeta** (Pro): cambia solo a **Solo teléfono (captura sin tarjeta)**. Puedes disparar con normalidad y las fotos pasan directo al teléfono con la hora como nombre (por ejemplo, `AC_20261025_193805.JPG`). Al meter una tarjeta vuelve solo al modo anterior.

Funciona desde Inicio, Carrete y Disparo remoto, tanto por Wi‑Fi como por USB.

**Configuración inicial:**
1. En el menú Configuración personalizada de la cámara, pon **Bloqueo disparo ranura vacía** (Slot empty release lock) en **Habilitar disparo** (Enable release); si no, la cámara bloquea el disparador sin tarjeta.
2. En Wi‑Fi, pon el Tipo de conexión de la cámara en **Control de la cámara** (Camera control). Si está en «Transferencia de imágenes», AeroCam te avisará unos 3 segundos después del primer disparo; la foto queda en la memoria de la cámara y pasa sola al cambiarlo. Por USB no existe esta limitación.
3. La conexión en un toque no admite disparar sin tarjeta — usa zona Wi‑Fi del teléfono o mismo Wi‑Fi.

**Entender la barra de estado** (arriba en Inicio y Carrete):

| Mensaje | Significado |
|---|---|
| Guardando en: tarjeta ✓ | Guarda en la tarjeta de memoria de la cámara |
| Guardando en: tarjeta + teléfono ✓ | Guarda en la tarjeta y también en el teléfono |
| Guardando en: solo teléfono (sin tarjeta en la cámara) | Las fotos pasan directamente al teléfono |
| La cámara está en modo «Transferencia de imágenes»… (rojo) | Cambia el Tipo de conexión a «Control de la cámara» |
| Wi‑Fi en un toque: sin tarjeta de memoria, no se puede disparar (rojo) | Mete una tarjeta o cambia a zona Wi‑Fi / mismo Wi‑Fi |
| Tarjeta de memoria llena (rojo) | Cambia de tarjeta o libera espacio (no pasa automáticamente a solo teléfono) |
| Sin tarjeta de memoria en la cámara, no se puede disparar (rojo) | Versión gratuita o menos de 1 GB libre en el teléfono |

> Sin tarjeta la cámara no puede grabar vídeo, y la ráfaga va más lenta porque cada foto debe transferirse al teléfono.

---

## Ubicación de fotos (GPS)
En **Ajustes → Recepción y notificaciones → Ubicación de fotos** hay dos interruptores:
- **Enviar ubicación a la cámara (Bluetooth)** (activado por defecto): al encender la cámara o enviar por Bluetooth, el teléfono manda su ubicación GPS a la cámara para que la escriba en las fotos.
- **Añadir ubicación a los JPEG recibidos (teléfono)**: añade la ubicación del teléfono según la hora de captura a los JPEG recibidos por Wi‑Fi, USB, FTP, descarga de galería o disparo remoto. Pregunta una vez al iniciar la primera recepción.
  - Los archivos RAW nunca se modifican y las fotos que ya traen GPS conservan sus coordenadas.
  - El historial de ubicación registrado durante la sesión se guarda solo en este teléfono y se borra a las 24 horas.
  - Si la hora de captura no coincide con ningún punto registrado, no se escribe nada (mejor sin ubicación que una ubicación errónea).
  - AeroCam debe estar abierto al iniciar la recepción para poder registrar la ubicación.

> Las coordenadas GPS incrustadas viajan con el archivo original al compartirlo. Al compartir por código QR se elimina la ubicación por defecto — consulta el [Capítulo 4](04-gallery.md#compartir-por-código-qr).

---

## Historial
Toca **Historial ›** arriba a la derecha de la tarjeta «Transferencia» en Inicio. Muestra el resultado de todas las recepciones, descargas de galería y capturas remotas (Correcto, Duplicado, Omitido, Fallido) con miniaturas.
- Toca cualquier elemento para verlo a pantalla completa dentro de la app.
- Puedes buscar, filtrar por cámara o borrar el historial. Borrar el historial no elimina los archivos del teléfono.
