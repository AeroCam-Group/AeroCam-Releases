<!-- translated from zh-TW at commit 968641f -->

# 10. Privacidad y estadísticas anónimas

AeroCam no tiene cuentas de usuario; las fotos viajan únicamente entre tu cámara y tu teléfono y **no se suben a ningún servidor**. Solo salen del teléfono los pocos datos indicados a continuación.

## Cuándo se conecta a Internet
| Función | Qué envía | ¿Se puede desactivar? |
|---|---|---|
| Buscar actualizaciones (Beta) | Solo consulta en GitHub cuál es la última versión | Automático una vez al día |
| Estadísticas de uso anónimas | Ver más abajo | Sí, en Ajustes → Soporte |
| Compartir por código QR | Solo dentro de tu red local (mismo Wi‑Fi o zona Wi‑Fi del teléfono) para que quien escanee vea las fotos elegidas | Termina cuando pulsas Detener o se agota el tiempo |

## Estadísticas de uso anónimas
Sirven para saber aproximadamente cuánta gente usa la app, qué cámaras y funciones se utilizan y dónde surgen problemas para decidir qué mejorar primero. **Nunca se venden a terceros ni se usan para publicidad.**

- **Interruptor**: **Ajustes → Soporte → «Enviar estadísticas de uso anónimas»**, activado por defecto.
- Se explica una vez tras conectar por primera vez una cámara, pudiendo elegir «Aceptar» o «Desactivar». **Antes de responder no se envía nada.**
- **Al desactivarlo**: deja de enviar y borra el ID aleatorio mencionado abajo junto con cualquier dato pendiente de envío. Si vuelves a activarlo se crea un ID nuevo.
- Si no hay Internet (por ejemplo, estando conectado al Wi‑Fi de la cámara), los datos se guardan en el teléfono y se envían cuando vuelva la conexión.
- La versión de desarrollo (Dev) no registra ni envía nada.

### Datos que se envían
- **ID aleatorio generado por la propia app**: no se obtiene del teléfono ni de la cámara; cambia si reinstalas la app o desactivas las estadísticas.
- Modelo de cámara (por ejemplo, Nikon Z f), solo el modelo.
- Método de conexión (Bluetooth, Wi‑Fi, USB, FTP) y tipo de Wi‑Fi (Wi‑Fi de la cámara, zona Wi‑Fi del teléfono, router).
- Qué funciones se han usado cada día (solo el nombre de la función, una vez al día), incluidas las funciones bloqueadas que se hayan tocado.
- Número de conexiones correctas o fallidas; en caso de fallo solo se envía un código de categoría (por ejemplo, «tiempo agotado»), nunca el mensaje de error.
- Pasos al añadir cámara: inicio, éxito, cámara no encontrada y motivo de fallo.
- Cuántas fotos se reciben al día (cantidad de JPEG, RAW y vídeos, solo cifras).
- Si los permisos se han concedido o denegado.
- Plan actual (Gratis, clave Beta…), versión de la app, idioma de la app y versión principal de Android.
- País: deducido de la conexión; solo se guarda el código de país.

### Nunca se envía
Número de serie de la cámara, nombre de propietario o copyright configurado en la cámara, ubicación (GPS), fotos ni vídeos, nombres de archivo, metadatos de disparo (EXIF), nombres ni contraseñas de Wi‑Fi, identificadores del teléfono (IMEI, Android ID, ID de publicidad), nombre, correo electrónico, cuentas ni texto de mensajes de error.

### Conservación
- El detalle diario por dispositivo se conserva 90 días; después solo quedan los totales diarios agregados.
- Los ID aleatorios sin actividad durante unos 13 meses se eliminan.
- Al procesar la conexión, el servidor ve necesariamente la IP, pero solo se usa para determinar el país y evitar abusos; **nunca se guarda en los datos estadísticos**.

## Información de ubicación
- **Enviar ubicación a la cámara (Bluetooth)**: el teléfono pasa su ubicación a la cámara para que ella la grabe en las fotos.
- **Añadir ubicación a los JPEG recibidos (teléfono)**: desactivado por defecto. Al activarlo, las ubicaciones registradas durante la recepción se guardan solo en este teléfono y se borran a las 24 horas.
- Ambos interruptores están en **Ajustes → Recepción y notificaciones → Ubicación de fotos** — consulta el [Capítulo 3](03-receive.md#ubicación-de-fotos-gps).
- La ubicación guardada en la foto viaja con el archivo al compartir el original. **Al compartir por código QR se elimina la ubicación por defecto.**

## Uso de permisos
| Permiso | Uso |
|---|---|
| Bluetooth, Dispositivos cercanos | Vincular la cámara, pasar fotos por Bluetooth, control remoto Bluetooth, buscar cámaras Wi‑Fi |
| Ubicación | Enviar ubicación a la cámara o añadirla a las fotos; Android también lo requiere para leer el nombre del Wi‑Fi |
| Notificaciones | Progreso de recepción, fotos recibidas, problemas de transferencia, aviso de batería baja de la cámara |
| Fotos y vídeos | Mostrar y organizar fotos en Fotos del teléfono |

## Información de diagnóstico
**Ajustes → Soporte → «Copiar información de diagnóstico»** solo copia texto al portapapeles; **tú decides** si quieres pegárnoslo. Incluye versión de la app, estado del teléfono y red, capacidades de la cámara y registros recientes de conexión, conservando solo los 4 últimos dígitos del número de serie de la cámara. Antes de pegarlo en un Issue público de GitHub, revísalo para asegurarte de no incluir nada que prefieras mantener privado.
