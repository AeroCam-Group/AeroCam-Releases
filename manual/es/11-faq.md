<!-- translated from zh-TW at commit 968641f -->

# 11. Preguntas frecuentes y solución de problemas

## General
**¿Puedo pasar fotos de la cámara al teléfono sin pagar Pro?**
Sí. En la versión gratuita puedes recibir automáticamente por Bluetooth copias JPEG reducidas de unos 2 megapíxeles, o explorar la tarjeta de la cámara por cable USB para elegir y descargar originales a mano.

**¿Hay que pagar por la Beta o las claves de prueba?**
No. Todo se publica gratis únicamente en GitHub, en AeroCam-Releases. Si alguien te pide dinero, no es un canal oficial.

**Al abrir la app aparece «Esta no es una versión oficial»**
Alguien ha reempaquetado la app por su cuenta; no aceptará claves de prueba y puede llevar código añadido. Desinstálala y vuelve a bajarla de AeroCam-Releases.

**Tras actualizar han desaparecido mi cámara y la clave de prueba**
Desde la versión 92.03.09 las versiones nuevas se instalan como una app independiente y no importan los datos de las anteriores. Vuelve a vincular la cámara y pega de nuevo la clave de prueba.

**¿Dónde se guardan las fotos?**
Las fotos van a `Pictures/AeroCam`, los vídeos a `Movies/AeroCam` y otros archivos a `Download/AeroCam`. Google Fotos y otras galerías los ven directamente. Lo guardado por versiones anteriores a la 92.03.09 sigue en su carpeta original sin moverse.

**He borrado una foto del teléfono y quiero volver a pasarla**
Simplemente envíala de nuevo desde la cámara; la app detectará que ya no está en el teléfono y la guardará.

**Tras restaurar fotos de la papelera o reinstalar la app, no aparecen en la galería**
Ve a **Ajustes → Almacenamiento y batería → «Volver a escanear fotos del teléfono»**.

---

## Conexión
**No consigo conectar la cámara por Wi‑Fi**
1. Asegúrate de que la cámara esté en la pantalla «Conectar a PC» con el icono Wi‑Fi visible; si se apagó la pantalla, pulsa el disparador hasta la mitad para despertarla.
2. Comprueba el Tipo de conexión: recepción automática y galería = Transferencia de imágenes; disparo remoto y sin tarjeta = Control de la cámara.
3. Modo zona Wi‑Fi del teléfono: verifica que la zona Wi‑Fi esté encendida y la cámara conectada a ella.
4. Modo mismo Wi‑Fi: verifica que teléfono y cámara estén en exactamente la misma red (a veces el móvil cambia solo a otro Wi‑Fi o a datos móviles).
5. Prueba **Conexión en un toque**, sin necesidad de zona Wi‑Fi ni router.
6. Toca **ⓘ** y sigue paso a paso la guía de conexión.

**En el Wi‑Fi de hoteles o ferias nunca encuentra la cámara**
Las redes Wi‑Fi públicas suelen bloquear la comunicación entre dispositivos. Usa la zona Wi‑Fi de tu teléfono o la conexión en un toque.

**La cámara dice «Ya emparejado con otro dispositivo»**
Ese perfil de red de la cámara lo está usando otra app. Crea un perfil nuevo en la cámara y vuelve a vincular.

**Conexión en un toque no encuentra el Wi‑Fi de la cámara**
Tras recibir la orden por Bluetooth, la cámara tarda 10–30 segundos en encender su Wi‑Fi y la app reintenta sola. Si sigue fallando, comprueba que la contraseña sea correcta.

**La zona Wi‑Fi del teléfono se apaga sola**
Algunos teléfonos apagan su zona Wi‑Fi si ningún dispositivo conectado consume Internet. Desactiva «Apagar zona Wi‑Fi automáticamente» en los ajustes del móvil o usa Conexión en un toque.

**Tras reiniciar la zona Wi‑Fi, la cámara no vuelve a conectar**
Puede haber cambiado la dirección IP del teléfono. En recepción automática Wi‑Fi la app la busca sola, pero en FTP debes actualizar la dirección en la cámara.

**Al enchufar el USB no pasa nada**
1. Comprueba que el ajuste USB de la cámara esté en **MTP/PTP**.
2. El cable debe permitir datos (hay cables que solo cargan).
3. Acepta el aviso de «Permitir acceso» cuando salte en el teléfono.
4. Toca `⋮` arriba a la derecha de la tarjeta USB → **Prueba USB** para ver en qué paso falla.

**La recepción en segundo plano se corta a menudo**
Desactiva la optimización de batería en **Ajustes → Almacenamiento y batería**. En teléfonos Xiaomi, OPPO y similares también hay que poner AeroCam en ahorro de batería «Sin restricciones» en los ajustes del sistema.

---

## Bluetooth
**El envío de fotos por Bluetooth se queda atascado**
- Al disparar en RAW, la cámara convierte antes a JPEG para enviarlo; si manejas la cámara durante el envío, lo cancelará. Lo mejor es apagar la cámara tras hacer las fotos para que envíe en segundo plano.
- En la tarjeta Bluetooth toca **Desconectar y reconectar** o **⋮ → Reiniciar servicio Bluetooth**; la vinculación se mantiene.

**Al pulsar AF en el control remoto Bluetooth no enfoca**
La cámara debe permitir enfocar al pulsar el disparador hasta la mitad. Si usas el botón AF‑ON, revisa en la configuración personalizada de la cámara que **Activación de AF** (AF activation) esté en **Disparador/AF-ON**.

**Si recibo la misma foto por Bluetooth y Wi‑Fi, ¿se guarda dos veces?**
Por defecto no: al recibir el original por Wi‑Fi, se borra automáticamente la copia reducida de Bluetooth. Puedes cambiarlo en **Ajustes → Recepción y notificaciones → «Fotos ya recibidas por Bluetooth»**.

---

## Disparo remoto
**No puedo cambiar la velocidad o el ISO**
- La velocidad requiere modo S o M, y el diafragma modo A o M; para ajustar el ISO a mano desactiva antes el ISO auto.
- En modelos con diales físicos como la Zf: pon el dial de velocidad en **1/3 STEP** y el de ISO en **C**.

**Tocar la pantalla no mueve el punto de enfoque**
Pon la zona AF de la cámara en un modo con punto desplazable (como punto único). En zona automática decide la cámara.

**Faltan datos en el panel de Inicio (objetivo, disparos restantes, contador de obturaciones)**
Algunos datos solo los ofrece la cámara en ciertos modos; cambia a «Control de la cámara» y entra en Disparo remoto para leerlos. El contador de disparos requiere al menos una foto en la tarjeta.

**¿Dónde se ve la temperatura de color (valor K)?**
Nikon guarda la temperatura de color real cifrada en los metadatos, por lo que en «Detalles» solo aparece el modo de balance de blancos.

---

## Destino de guardado y disparar sin tarjeta
**No hay tarjeta en la cámara y al pulsar el disparador no hace nada**
Comprueba que **Bloqueo disparo ranura vacía** esté en **Habilitar disparo** y que la app esté conectada (la barra superior debe poner «solo teléfono»).

**En las fotos aparece la palabra «DEMO»**
Si disparas sin tarjeta y sin estar conectado en modo «solo teléfono», la cámara marca las tomas como **DEMO** y no las guarda. Mete una tarjeta o dispara conectado a AeroCam.

**Las fotos no llegan al teléfono y sale un aviso rojo arriba en Inicio**
- Si dice «La cámara está en modo "Transferencia de imágenes"»: disparar sin tarjeta requiere **Control de la cámara**. Al cambiarlo, la cámara reconectará y pasará automáticamente las fotos ya tomadas.
- Si dice «Wi‑Fi en un toque: sin tarjeta de memoria»: Conexión en un toque no admite disparar sin tarjeta; mete una tarjeta o usa zona Wi‑Fi / mismo Wi‑Fi.

**Salta el aviso «Conexión interrumpida»**
En modo solo teléfono avisa si se pierde la conexión más de 10 segundos, porque las fotos tomadas en ese rato no se guardan en ninguna tarjeta. Al reconectar, la app se recupera sola.

---

## Edición y estilos
**No se abre o no se puede editar un NEF**
Los NEF con compresión Alta eficiencia / Alta eficiencia★ se editan usando su JPEG incrustado; los que solo llevan una vista previa pequeña no se pueden editar. Para revelar RAW completos en el teléfono, pasa la cámara a **Compresión sin pérdidas** — consulta el [Capítulo 6](06-edit.md#raw-editable-en-el-teléfono-cambiar-compresión-raw-de-la-cámara).

**El efecto de .np3 no se ve igual que en la cámara**
El teléfono simula curvas y saturación, pero aún no simula el mezclador de color ni la gradación de color, así que es una aproximación. Además, si el JPEG ya tenía un Picture Control aplicado en cámara, el efecto se suma.

**Al grabar un .np3 en la cámara los colores salen distintos**
Las ranuras personalizadas de la cámara solo aceptan **Base + Curva + Enfoque**; saturación, mezclador de color y gradación no se pueden enviar por conexión. Para un resultado idéntico, copia el `.np3` a una tarjeta e impórtalo desde el menú de la cámara.

**Falla la unión panorámica o faltan fotos**
Cada toma debe solaparse un 30 % con la contigua. Las que no encajen se muestran por nombre; las panorámicas en rejilla no se generan si falta alguna casilla.

---

## FTP
**La cámara muestra Err.31 o Err.32**
Actualiza a la última Beta y comprueba que dirección IP, puerto `2121`, usuario `aerocam` y contraseña coincidan exactamente, con el modo pasivo activado.

**La cámara muestra error de inicio de sesión**
La contraseña debe ser idéntica a la que muestra AeroCam en FTP (distingue mayúsculas y minúsculas). Si pulsaste «Regenerar contraseña», cámbiala también en la cámara.

**Con el FTP activo no conectan el Carrete ni el Disparo remoto**
En modo FTP la cámara no admite conexiones Wi‑Fi de galería ni disparo remoto. Usa un cable USB, o detén la recepción FTP y vuelve a poner la cámara en «Conectar a PC».

---

## Otros
**La app se cierra de repente**
Vuelve a abrirla, ve a **Ajustes → Soporte → «Copiar información de diagnóstico»** y pégala al [informar de un problema](12-report.md); ahí consta el punto exacto del último fallo.

**¿Cómo desactivo las estadísticas de uso anónimas?**
Desactiva **Ajustes → Soporte → «Enviar estadísticas de uso anónimas»** — consulta [Privacidad y estadísticas anónimas](10-privacy.md).
