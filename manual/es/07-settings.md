<!-- translated from zh-TW at commit 968641f -->

# 7. Referencia de ajustes

**Ajustes** se divide en cinco categorías; entra en cada una para ver sus opciones. En la versión gratuita se ocultan los ajustes que no aplican. Si tienes sugerencias o crees que algún valor por defecto debería cambiar, cuéntanoslo en [Informar de un problema](12-report.md).

## Recepción y notificaciones

### Recepción
| Ajuste | Opciones | Por defecto | Descripción |
|---|---|---|---|
| Tipos de archivo a recibir | Todos los archivos / Solo JPG / JPG + RAW / Fotos + vídeos / Personalizado; además Guardar solo JPEG de RAW, Guardar JPEG comprimido, Reemplazar copia comprimida al llegar el original (Pro) | Todos los archivos | Consulta el [Capítulo 3](03-receive.md#tipos-de-archivo-a-recibir) |
| Carpeta de guardado | Por cámara / Por fecha / Por cámara y fecha / Por tipo de archivo | Por cámara y fecha | Organización dentro de `Pictures/AeroCam` y `Movies/AeroCam` |
| Nombre de archivo | Nombre original / Prefijo de fecha / Prefijo de fecha y hora | Nombre original | Solo afecta a archivos futuros; los duplicados se siguen comprobando por el nombre original |
| Modo de recepción (Pro) | Continuo / Un solo archivo | Continuo | Un solo archivo = se detiene al recibir uno |
| No recibir vídeos grandes automáticamente (Pro) | Tamaño (MB) | 1024 MB | Los que superen el límite quedan como «Filtrado» para descarga manual |
| Si no se encuentra la cámara por Wi‑Fi | 30 s / 1 / 2 / 3 / 5 / 10 min / Sin límite | 3 min | Detiene la recepción automática tras ese tiempo para ahorrar batería |
| Apagado automático de FTP por inactividad | No apagar / 5 / 10 / 30 min | No apagar | Cuenta desde la última foto recibida; nunca corta una transferencia activa |
| Fotos ya recibidas por Bluetooth | Reemplazar por original al recibir por Wi‑Fi / No volver a descargar por Wi‑Fi / Conservar ambas copias | Reemplazar por original | Por Bluetooth llega una copia reducida de unos 2 MB |

### Ubicación de fotos
| Ajuste | Por defecto | Descripción |
|---|---|---|
| Enviar ubicación a la cámara (Bluetooth) | Activado | Al encender la cámara o transferir por Bluetooth, envía la ubicación del teléfono para grabarla en las fotos |
| Añadir ubicación a los JPEG recibidos (teléfono) | Desactivado (pregunta la primera vez) | Graba la ubicación del teléfono según la hora de captura en los JPEG recibidos por Wi‑Fi, USB o FTP; no toca los RAW |

Más detalles en el [Capítulo 3 Ubicación de fotos](03-receive.md#ubicación-de-fotos-gps).

### Galería
| Ajuste | Opciones | Por defecto | Descripción |
|---|---|---|---|
| Calidad de JPEG comprimido (Pro) | 60 / 70 / 80 / 90 % | 80 % | Calidad de los JPEG recomprimidos en el teléfono (24 MP ocupan unos 3–4 MB) |
| Selección tras descargar / eliminar | Preguntar siempre / Mantener siempre / Limpiar siempre | Preguntar siempre | Evita dejar fotos marcadas y tocar por error «Eliminar de la cámara» |
| Cuenta atrás del aviso | 3 / 5 / 8 / 10 s | 5 s | Con «Preguntar siempre», limpia la selección si no respondes antes de acabar |
| Detener compartir por código QR tras | 15 / 30 / 60 min | 30 min | Pasado ese tiempo el enlace deja de funcionar |

### Notificaciones
| Ajuste | Por defecto | Descripción |
|---|---|---|
| No molestar | Desactivado | Silencia todas las notificaciones de AeroCam (la notificación fija «Recibiendo» sigue visible por exigencia de Android) |
| Al iniciar transferencia | Desactivado | |
| Al recibir foto | Activado | |
| Problemas de transferencia | Activado | Bloqueo, cancelación de la cámara o falta de espacio en el teléfono |
| Ocultar notificación fija | — | Abre los ajustes de notificaciones de Android para ocultarla; la recepción sigue funcionando |
| Aviso de batería baja de la cámara | Activado, 15 % | Umbral a elegir: 10 / 15 / 20 / 30 %; solo se comprueba estando conectada |

## Disparo

### Destino de guardado
| Ajuste | Opciones | Descripción |
|---|---|---|
| Destino de guardado | Tarjeta de memoria / Tarjeta + teléfono (Pro) | Se usa cuando hay tarjeta; sin tarjeta cambia solo a solo teléfono (Pro). Estando conectada indica si hay tarjeta. Consulta el [Capítulo 3](03-receive.md#destino-de-guardado-y-disparar-sin-tarjeta) |

### Disparo remoto
| Ajuste | Opciones | Por defecto | Descripción |
|---|---|---|---|
| Activado por defecto al entrar en Disparo remoto | Enfocar antes de disparar, Histograma, Aviso de sobreexposición, Focus peaking, Exposímetro | Enfocar antes de disparar, Exposímetro | Se pueden activar o desactivar en cualquier momento |
| Color del exposímetro | Automático / Blanco / Negro | Automático | Automático = según el brillo del fondo |
| Color de focus peaking | Rojo / Amarillo / Azul / Blanco | Rojo | Cambia de color si el sujeto es rojizo |
| Pantalla siempre encendida en Disparo remoto | Activado / Desactivado | Activado | Evita que se apague la pantalla en intervalos o exposiciones largas |
| Modo zurdo | Activado / Desactivado | Desactivado | En horizontal mueve el disparador abajo a la izquierda |

### Conexión por cable (USB‑C)
| Ajuste | Opciones | Por defecto | Descripción |
|---|---|---|---|
| Frecuencia de vista previa USB | 30 / 60 fps / Sin límite | 30 fps | 30 ahorra batería y calienta menos; 60 es más fluido |
| Vista previa USB en gran tamaño | Activado / Desactivado | Activado | Más nitidez, aunque puede bajar algo los fps; vuelve solo si la cámara no lo admite |
| Iniciar recepción automáticamente al conectar cable USB (Pro) | Activado / Desactivado | Activado | Arranca la recepción USB nada más enchufar |
| Sincronizar hora de la cámara al conectar | Activado / Desactivado | Activado | Solo corrige si hay >2 s de diferencia; pregunta antes si pasa de 1 día |
| Mantener cámara activa por cable | Activado / Desactivado | Activado | Envía una pequeña señal cada 10 s; se detiene tras 30 min sin uso o batería baja |

## Apariencia e idioma
| Ajuste | Opciones | Por defecto |
|---|---|---|
| Tema | Seguir sistema / Claro / Oscuro / Noche estrellada (luz roja) | Seguir sistema |
| Brillo mínimo de pantalla de la app | Activado / Desactivado (en modo noche estrellada) | Desactivado |
| Idioma | Seguir sistema / 繁中 / 简中 / 日本語 / English / 한국어 / Deutsch / Français / Español / Tiếng Việt / ไทย / Bahasa Indonesia | Seguir sistema |

## Almacenamiento y batería
| Elemento | Descripción |
|---|---|
| Caché de miniaturas | Muestra lo que ocupa y permite borrarla (se vuelve a leer de la cámara si hace falta) |
| Archivos temporales de descargas incompletas | Muestra el tamaño y permite borrarlos |
| Volver a escanear fotos del teléfono | Recupera fotos que volvieron al teléfono, por ejemplo restauradas de la papelera o guardadas antes de reinstalar |
| Optimización de batería | Conviene desactivarla (que ponga «Sin optimizar ✓») para que Android no corte la recepción en segundo plano |

## Soporte
| Elemento | Descripción |
|---|---|
| Copiar información de diagnóstico | Pégala al reportar un fallo: versión de la app, estado de teléfono y red, capacidades de la cámara, historial reciente de comandos y último error de cierre. Del número de serie solo incluye los 4 últimos dígitos |
| Borrar registros | Elimina los logs de esta sesión, la anterior y los registros de cierres |
| Buscar actualizaciones | Comprueba manualmente si hay versión nueva; abajo indica la actual |
| Clave de prueba | «Obtener clave gratuita» abre AeroCam-Releases; «Introducir clave de prueba» permite pegarla; muestra plan actual y caducidad |
| Licencias de código abierto | Componentes de terceros utilizados (como LibRaw para revelado RAW) |
| Enviar estadísticas de uso anónimas | Un único interruptor, activado por defecto. Consulta [Privacidad y estadísticas anónimas](10-privacy.md) |
