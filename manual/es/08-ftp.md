<!-- translated from zh-TW at commit 968641f -->

# 8. Recepción FTP (Pro)

Al hacer una foto, la cámara **la envía por sí sola al teléfono mediante FTP**, sin tener que seleccionar fotos en la cámara ni abrir la galería. En pruebas con la Nikon Zf, cada RAW (unos 18 MB) llega al teléfono en aproximadamente 1 segundo.

AeroCam integra su propio servidor FTP, así que **no tienes que instalar ni configurar nada aparte**.

## Ideal para
- Eventos, bodas y deportes: recibir las fotos en el teléfono mientras sigues disparando.
- Revisarlas al instante en el teléfono o subirlas a redes sociales nada más tomarlas.

## Requisitos
- Cámara con función de envío FTP integrada (Nikon Z f, Z 8, Z 9, Z 6III, etc.).
- Activar la **zona Wi‑Fi** del teléfono y conectar la cámara a ella (o conectar ambos al mismo router).
- Tener una tarjeta de memoria en la cámara: el FTP envía los archivos guardados en la tarjeta.

## Configuración (primera vez)
1. Activa la zona Wi‑Fi de tu teléfono.
2. En Inicio de AeroCam → **FTP** → toca arriba **Iniciar recepción**. Verás los datos que debes poner en la cámara; puedes tocar cada uno para copiarlo:
   - Dirección del servidor (por ejemplo, `10.14.29.30`)
   - Puerto: `2121`
   - Usuario: `aerocam`
   - Contraseña: clave de 8 caracteres generada por la app (puedes pulsar «Regenerar»)
   - Modo pasivo (PASV): **Activado**
3. En la cámara: **MENU → Menú de red → Conectar a servidor FTP → Ajustes de red → Crear perfil**:
   - En Wi‑Fi elige la zona Wi‑Fi de tu teléfono.
   - En tipo de servidor elige `FTP`, introduce la dirección, puerto, usuario y contraseña anteriores, y activa el modo pasivo.
4. Activa esa conexión FTP en la cámara. Cuando en AeroCam el estado FTP ponga «Conectado», ya está listo.
5. En el menú FTP de la cámara activa **Envío automático** (Auto send / enviar tras disparar) para que a partir de ahora se manden solas.

Si tienes dudas, toca **ⓘ** junto a la tarjeta FTP para ver la guía con imágenes.

📷 Captura de pantalla: panel FTP desplegado con los datos de ajuste

## Durante el uso
- Indicadores de estado: Apagado, Activo · Esperando cámara, Conectado, Recibiendo, Error.
- La notificación muestra «Recibiendo por FTP · N recibidas» junto con el archivo actual y la velocidad.
- Las fotos se guardan siguiendo las reglas de **Ajustes → Recepción y notificaciones** (carpeta, nombre, solo JPEG, guardar solo JPEG de RAW, etc.) y aparecen en el historial con origen `FTP`.
- Si se corta la transferencia o apagas la cámara a mitad, los archivos incompletos se borran solos para que no queden archivos dañados en la galería.
- Al apagar la cámara pasa a desconectado en ~1 minuto; al volver a encenderla y conectarse, retoma el trabajo automáticamente.
- **Apagado automático por inactividad**: **Ajustes → Recepción y notificaciones → «Apagado automático de FTP por inactividad»** (No apagar, 5, 10, 30 minutos). Cuenta desde la última foto recibida, nunca corta una transferencia en curso y avisa al cerrarse.

## A tener en cuenta
- **Mantén la zona Wi‑Fi encendida**. Algunos teléfonos la apagan solos si no detectan consumo de datos; desactiva «Apagar zona Wi‑Fi automáticamente» en los ajustes de tu teléfono.
- Si apagas y vuelves a encender la zona Wi‑Fi, la IP del teléfono puede cambiar y tendrás que actualizarla en la cámara.
- La recepción FTP y la **recepción automática por Wi‑Fi no pueden estar activas a la vez**; al encender una se detiene la otra.
- Con el FTP activo, la cámara está en modo FTP y **el Carrete y el Disparo remoto no pueden conectar por Wi‑Fi**. Para usarlos conecta un cable USB, o detén la recepción FTP y vuelve a poner la cámara en «Conectar a PC».
- El servidor FTP solo escucha en la red local de la zona Wi‑Fi o del router, nunca queda abierto a Internet.
- «Conexión en un toque» no funciona con FTP (la conexión en un toque crea una red en la cámara, mientras que FTP necesita que la cámara se conecte al teléfono).

## Enviar directo a un NAS
También puedes configurar el FTP de la cámara para enviar directamente a tu NAS de casa sin pasar por el teléfono. Es una función propia de la cámara y no requiere AeroCam.
