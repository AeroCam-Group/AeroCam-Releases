<!-- translated from zh-TW at commit 968641f -->

# 1. Instalación y primeros pasos

## Instalación
1. Descarga el último APK Beta (`…-Beta-xx.xx.xx.apk`) desde [Releases](https://github.com/AeroCam-Group/AeroCam-Releases/releases/latest).
2. Abre el APK en tu teléfono. La primera vez, Android te pedirá permitir «Instalar aplicaciones desconocidas» — acéptalo.
3. Cuando salga una versión nueva, simplemente descárgala e instálala encima de la anterior. Tus cámaras vinculadas y ajustes se conservarán.

> Descarga la app únicamente desde AeroCam-Releases. Los APK de otros sitios pueden haber sido modificados. Si al abrir la app aparece «Esta no es una versión oficial», significa que alguien la ha reempaquetado: no aceptará claves de prueba y podría contener código malicioso. Desinstálala y vuelve a descargarla desde AeroCam-Releases.

> Si usabas una **Beta anterior a la 92.03.09**: las versiones nuevas se instalan como una app aparte. Vuelve a vincular tu cámara e introduce la clave de prueba; cuando compruebes que todo funciona, desinstala la versión antigua.

📷 Captura de pantalla: pantalla del sistema «Instalar aplicaciones desconocidas»

## Permisos
La app solo pide cada permiso cuando utilizas una función que lo necesita. Puedes rechazar los que no necesites:

| Permiso | Uso |
|---|---|
| Bluetooth, Dispositivos cercanos | Vinculación Bluetooth, transferencia de fotos por Bluetooth, control remoto Bluetooth; también necesario en Android 13+ para buscar cámaras Wi‑Fi |
| Ubicación | Enviar la ubicación del teléfono a la cámara para guardarla en las fotos, o añadir ubicación a los JPEG recibidos; Android también lo exige para leer el nombre del Wi‑Fi |
| Notificaciones | Progreso de recepción, fotos recibidas, problemas de transferencia, avisos de batería baja de la cámara |
| Fotos y vídeos | Mostrar y organizar las fotos en tu teléfono |

Consulta la explicación detallada de cada permiso en [Privacidad y estadísticas anónimas](10-privacy.md).

## Recorrido por la pantalla
En la parte inferior hay cuatro pestañas:

| Pestaña | Contenido |
|---|---|
| **Inicio** | Panel de la cámara (batería, objetivo, tarjetas de memoria, estado de conexión), cuatro métodos de conexión (Wi‑Fi, USB, Bluetooth, FTP), estado e historial de transferencias, estilos de cámara, gestionar cámaras |
| **Carrete** | Dos subpestañas: «Fotos del teléfono» y «Tarjeta SD de la cámara» — consulta el [Capítulo 4](04-gallery.md) |
| **Disparo remoto** | Ver la imagen en vivo de la cámara en el teléfono, cambiar ajustes y hacer fotos o vídeos — consulta el [Capítulo 5](05-remote.md) |
| **Ajustes** | Cinco categorías — consulta el [Capítulo 7](07-settings.md) |

Si no sabes cómo conectar la cámara, toca **ⓘ** junto al estado de conexión en Inicio, o arriba a la derecha en cada paso de «Añadir cámara», para abrir una guía visual paso a paso.

📷 Captura de pantalla: pantalla de inicio

## Clave de prueba (desbloquear Pro y Cine)
La Beta empieza en la versión gratuita.
1. Copia la clave de prueba actual desde la [página principal de AeroCam-Releases](https://github.com/AeroCam-Group/AeroCam-Releases). En la app, **Ajustes → Soporte → «Obtener clave gratuita»** abre esa página directamente.
2. Ve a **Ajustes → Soporte → «Introducir clave de prueba»**, pega el texto completo y toca «Aplicar». Al tocar una función bloqueada también aparece «Introducir clave de prueba» en el diálogo.
3. Cada clave dura 14 días y se renueva cada semana. Cuando caduque, la app volverá a la versión gratuita — simplemente pega la clave nueva.

> Tanto la Beta como las claves de prueba son **gratuitas** y se publican únicamente en GitHub, en AeroCam-Releases. Si alguien te pide dinero por ellas, no es un canal oficial.

## Buscar actualizaciones
La Beta comprueba automáticamente si hay actualizaciones una vez al día al abrirla por primera vez. También puedes hacerlo manualmente en **Ajustes → Soporte → «Buscar actualizaciones»**.

## Idioma
La interfaz es compatible con chino tradicional, chino simplificado, japonés, inglés, 한국어, Deutsch, Français, Español, Tiếng Việt, ไทย y Bahasa Indonesia. Por defecto sigue el idioma del sistema de tu teléfono, o puedes cambiarlo en **Ajustes → Apariencia e idioma → Idioma**.

El inglés, el chino tradicional y el japonés están siempre completos al 100 %. En los demás idiomas, las funciones nuevas pueden mostrarse primero en inglés y traducirse más adelante. Si ves algún fallo de traducción, avísanos mediante el formulario «Error de traducción» en [Informar de un problema](12-report.md).

## Estadísticas de uso anónimas
La primera vez que conectes una cámara, la app te explicará una vez el envío de estadísticas de uso anónimas. Puedes elegir «Aceptar» o «Desactivar» — no se envía nada antes de que respondas. Puedes desactivarlo en cualquier momento en **Ajustes → Soporte**. Consulta qué datos se envían y cuáles nunca se envían en [Privacidad y estadísticas anónimas](10-privacy.md).
