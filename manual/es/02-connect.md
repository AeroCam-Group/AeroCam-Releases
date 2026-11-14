<!-- translated from zh-TW at commit 968641f -->

# 2. Conectar la cámara

AeroCam ofrece cuatro formas de conexión. Puedes configurar varias a la vez y la app usará automáticamente la que esté disponible. Los cuatro botones de Inicio (Wi‑Fi, USB, Bluetooth, FTP) muestran su estado.

> ¿No sabes cómo conectar? Toca **ⓘ** junto al estado de conexión en Inicio, o arriba a la derecha en cada paso de «Añadir cámara», para abrir una guía visual (una página para zona Wi‑Fi del teléfono, mismo Wi‑Fi, conexión en un toque, USB, Bluetooth y FTP) con capturas del teléfono y de la cámara, además de una lista de comprobación si no conecta.

## Cómo elegir

| Lo que buscas | Opción recomendada |
|---|---|
| Recibir fotos incluso con la cámara apagada, sin preocuparte | **Bluetooth** (JPEG reducidos, gratis) |
| En exteriores, sin activar zona Wi‑Fi, para archivos originales, galería y disparo remoto | **Conexión en un toque** (Pro) |
| Transferencia automática al instante tras cada foto, máxima velocidad inalámbrica | **[Recepción FTP](08-ftp.md)** (Pro, requiere zona Wi‑Fi) |
| Máxima estabilidad, monitor de vídeo, sesiones remotas largas | **Cable USB** (selección y descarga manual gratis) |
| En casa o en el estudio | **Mismo Wi‑Fi** (Pro) |

## Referencia de velocidad (probado con Nikon Zf y Pixel 10 Pro)

| Método | Un archivo RAW (aprox. 18 MB) |
|---|---|
| Recepción FTP | aprox. 1 s (aprox. 17 MB/s) |
| Descarga de galería Wi‑Fi | aprox. 1,3 s (aprox. 13 MB/s) |
| USB | Suele ser más rápido que el Wi‑Fi, según el cable (aprox. 35 MB/s con cable USB 2.0) |
| Bluetooth | JPEG reducido (aprox. 2 MB), 15–20 s por foto |

## Luces de estado en Inicio
Los botones Wi‑Fi, USB, Bluetooth y FTP cambian de color según su estado (gris cuando no están conectados):

| Color | Significado |
|---|---|
| 🟢 Verde | Conectado o listo (verde claro en Bluetooth = en espera, listo para enviar estando apagada) |
| 🔵 Azul | Transfiriendo |
| 🟠 Naranja | Conectando (parpadeando), o requiere atención (permisos, bloqueo, error) |
| 🔴 Rojo | El Wi‑Fi o el Bluetooth del teléfono está apagado |

---

## Bluetooth (gratis, sustituye a SnapBridge)

### Vinculación
1. En la cámara: **MENU → Menú de red → Conectar a dispositivo inteligente → Emparejamiento (Bluetooth) → Iniciar emparejamiento**.
2. Si la cámara ya estaba vinculada con SnapBridge, borra primero la vinculación en SnapBridge y olvida la cámara en los ajustes Bluetooth del teléfono (dos apps no pueden estar vinculadas a la vez a la misma cámara).
3. En AeroCam: Inicio «Bluetooth» → **Vincular cámara** → Iniciar. En el teléfono y en la cámara aparecerá el mismo código; confirma en ambos. En la cámara aparecerá tu teléfono como `AeroCam_<modelo de teléfono>`.

📷 Captura de pantalla: tarjeta Bluetooth

### Después de vincular
Una vez vinculada, la conexión Bluetooth permanece activa hasta que la desvincules (te pedirá confirmación).
- Normalmente AeroCam solo **escucha** la señal Bluetooth en segundo plano sin despertar la cámara si está en reposo.
- **Al encender la cámara**: AeroCam se conecta un momento para sincronizar la hora y la ubicación GPS del teléfono (para que la cámara la guarde en las fotos nuevas) y luego se desconecta.
- **Cuando la cámara tiene fotos para enviar**: activa **Enviar si está apagada** (Send while off) en el menú «Conectar a dispositivo inteligente» de la cámara. La cámara se conectará sola por Bluetooth para enviar las fotos, incluso después de apagarla.
- Lo que recibes son archivos JPEG de unos 2 MB generados por la cámara (si disparas en RAW, la cámara los convierte antes a JPEG), tardando unos 15–20 segundos por foto. Para archivos originales usa Wi‑Fi, USB o FTP.
- Si quieres recibir al instante, toca **Recibir ahora** en la tarjeta Bluetooth.
- El servicio se reanuda solo tras apagar/encender el Bluetooth, reiniciar el teléfono o actualizar la app. Mientras espera, Android muestra una notificación fija de baja prioridad que puedes ocultar desde los ajustes del sistema.

### Estados de la tarjeta Bluetooth
🟢 Cámara cerca · Encendida / 🟢 Verde claro: En espera (listo para enviar apagada) / ⚪ Cámara no visible (muestra cuándo se vio por última vez) / 🔵 Transfiriendo / 🟠 Parece atascado / 🔴 Bluetooth del teléfono apagado.

Como el Bluetooth no está conectado de forma continua, esta tarjeta indica si se detecta la cámara cerca y qué está haciendo ahora mismo.

### Si se atasca la transferencia
- Si no llegan datos durante 30 segundos en plena transferencia, la app se desconecta sola y la cámara reintentará más tarde; tras 20 segundos sin actividad, la tarjeta se pone amarilla («Parece atascado»).
- **Desconectar y reconectar**: corta solo la transferencia actual.
- **⋮ → Reiniciar servicio Bluetooth**: reinicia todo el servicio Bluetooth en segundo plano manteniendo la vinculación.
- Al disparar en RAW, la cámara debe convertir cada archivo a JPEG antes de enviarlo. Si manejas la cámara durante el envío (pulsar el disparador hasta la mitad, hacer fotos), la cámara cancelará la transferencia. Lo mejor es apagar la cámara tras disparar y dejar que envíe en segundo plano.

---

## Wi‑Fi (Pro): tres formas de conectar

| Método | Cómo funciona | Cuándo usarlo |
|---|---|---|
| **Conexión en un toque** (recomendado) | Usa Bluetooth para pedir a la cámara que active su propio Wi‑Fi y conecta el teléfono automáticamente | En exteriores, cuando no quieres activar la zona Wi‑Fi |
| **Zona Wi‑Fi del teléfono** (recomendado en la guía) | La cámara se conecta al punto de acceso móvil de tu teléfono | Si la conexión en un toque es inestable, o para usar FTP o disparar sin tarjeta |
| **Mismo Wi‑Fi** | El teléfono y la cámara se conectan al mismo router | En casa o en el estudio |

### Conexión en un toque
1. Completa primero la **vinculación Bluetooth**.
2. En Inicio, toca Wi‑Fi → «Conexión en un toque».
3. La primera vez, introduce la **contraseña** del Wi‑Fi de la cámara (el nombre de red, tipo `NIKON_…`, se rellena solo). Se guarda únicamente en tu teléfono.
4. Cuando Android pida permiso para conectarse a esa red Wi‑Fi, acepta.
5. Cuando aparezca «Conectado al Wi‑Fi de la cámara», la galería, el disparo remoto y la recepción automática usarán esta conexión. Toca «Desconectar» para volver a tu Wi‑Fi normal.

Si la galería o el disparo remoto aún no están conectados, también verás directamente en pantalla el botón «Conectar con el Wi‑Fi de la cámara».

> - Mientras estés conectado al Wi‑Fi de la cámara, tu teléfono usará datos móviles para navegar por Internet.
> - La conexión en un toque **no se puede usar con FTP** y **no admite disparar sin tarjeta** (usa zona Wi‑Fi del teléfono o mismo Wi‑Fi si no hay tarjeta en la cámara).

📷 Captura de pantalla: tarjeta de conexión en un toque y estado conectado

### Zona Wi‑Fi del teléfono / Mismo Wi‑Fi (primera vinculación)
1. En la cámara: **MENU → Menú de red → Conectar a PC**, y crea un perfil de red (conectado a la zona Wi‑Fi de tu teléfono o al Wi‑Fi de tu casa).
   - Modelos recientes (con «Tipo de conexión» en el menú): pon «Tipo de conexión» en **Transferencia de imágenes**.
   - Modelos anteriores: selecciona simplemente **Conectar a PC**.
2. En AeroCam: **Inicio → «＋» Añadir cámara**, y elige el método (Mismo Wi‑Fi o Zona Wi‑Fi del teléfono). La app comprobará la red y buscará la cámara automáticamente; también puedes introducir su IP a mano.
3. En la pantalla de la cámara aparecerá un **PIN de 4 dígitos**. Introdúcelo en el teléfono y pulsa OK en la cámara.
4. Al terminar se guarda como «perfil de cámara» para conectar directamente la próxima vez. Puedes guardar varias cámaras y varias redes; tras actualizar la app **no hace falta volver a vincular**, y AeroCam encontrará la cámara aunque cambie su dirección IP.

> Si la cámara indica «Ya emparejado con otro dispositivo», ese perfil de red lo está usando otra app. Crea un perfil nuevo en la cámara y vuelve a vincular.

📷 Captura de pantalla: asistente para añadir cámara y entrada de PIN

### Comprobaciones previas a la conexión
- Al tocar «Iniciar recepción» o entrar en Carrete / Disparo remoto, AeroCam comprueba primero la red. Si el perfil es «Zona Wi‑Fi del teléfono» pero está apagada, o «Mismo Wi‑Fi» pero el teléfono no está conectado a esa red, aparecerá un aviso amarillo (por ejemplo, «Activa primero la zona Wi‑Fi del teléfono») con accesos directos a «Ajustes de zona Wi‑Fi» y «Ajustes de Wi‑Fi». Al activarlo y volver a AeroCam, el aviso desaparece.
- Si no encuentra la cámara ni por Wi‑Fi ni por zona Wi‑Fi, Inicio mostrará «Cámara no encontrada en la red» (normalmente porque «Conectar a PC» no está activo en la cámara) junto al botón «Ver guía de conexión».

### «Tipo de conexión» (Connection type) de la cámara
En modelos recientes (Z9, Z8, Z6III, Zf, Z5II, Z50II…): **MENU → Menú de red → Conectar a PC → Tipo de conexión**
- **Transferencia de imágenes** (Image transfer): para recepción automática y explorar la tarjeta de memoria.
- **Control de la cámara** (Camera control): para disparo remoto y disparar sin tarjeta.

Al cambiarlo, el Wi‑Fi de la cámara se corta un instante y AeroCam se reconecta solo sin volver a vincular. Si entras en Disparo remoto cuando la cámara sigue en «Transferencia de imágenes», la app te mostrará los pasos para cambiarlo.

---

## Cable USB
Más rápido y estable que el Wi‑Fi. **No requiere vinculación** ni añadir la cámara antes.
1. Pon el ajuste USB de la cámara en **MTP/PTP** (no «iPhone» ni «UVC/UAC»).
2. Usa un cable USB‑C **de datos** (algunos cables solo sirven para cargar). Un cable USB 3 de 5 Gbps / 10 Gbps da mejor velocidad.
3. En Inicio, la tarjeta USB mostrará «Z f detectada · Se requiere permiso de acceso» → toca «Permitir acceso» y acepta el aviso de Android una vez.

### Colores de la tarjeta USB
| Color | Significado |
|---|---|
| ⚪ Gris | No se detecta cámara (o el cable es solo de carga) |
| 🟠 Naranja | Cámara detectada; requiere permiso de acceso |
| 🔴 Rojo | El ajuste USB no es MTP/PTP, permiso denegado o fallo en la prueba (muestra el motivo) |
| 🟢 Verde | Conectado por cable USB |

### Mientras está conectada por USB
- El Carrete, el Disparo remoto y la recepción automática **cambian automáticamente a USB**; al desenchufar vuelven a Wi‑Fi. Si enchufas el cable en medio de un disparo remoto por Wi‑Fi, también pasa a USB sin cortes (salvo durante disparo a intervalos, horquillado o exposición Bulb en curso).
- **Recepción USB** (Pro): toca «Iniciar recepción» en la tarjeta USB para guardar en el teléfono las fotos recién tomadas y las que envíes con «Enviar a PC» desde la cámara. Por defecto empieza sola al enchufar el cable (**Ajustes → Disparo → «Iniciar recepción automáticamente al conectar cable USB»**).
- **Sincronización de hora**: sincroniza el reloj de la cámara al conectar (solo corrige si hay más de 2 s de diferencia; pregunta antes si pasa de 1 día).
- **Mantener activa**: envía una pequeña señal cada 10 segundos mientras el Carrete o el Disparo remoto están abiertos para que la cámara no se suspenda; se detiene tras 30 minutos de inactividad o si queda poca batería.
- El teléfono puede alimentar la cámara por USB — en sesiones largas conviene usar una batería externa.
- **Prueba USB** (⋮ arriba a la derecha de la tarjeta USB): comprueba conexión, datos de la cámara, tarjetas, fotogramas por segundo de vista en vivo y velocidad de lectura.

📷 Captura de pantalla: tarjeta USB

---

## FTP
La cámara envía las fotos por sí sola al teléfono nada más disparar — consulta el [Capítulo 8](08-ftp.md).
