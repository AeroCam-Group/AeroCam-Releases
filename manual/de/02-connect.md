<!-- translated from zh-TW at commit 968641f -->

# 2. Kamera verbinden

AeroCam bietet vier Verbindungsarten. Du kannst mehrere gleichzeitig einrichten – die App nutzt automatisch die jeweils verfügbare Verbindung. Die vier Kacheln auf dem Startbildschirm (Wi‑Fi, USB, Bluetooth, FTP) zeigen ihren aktuellen Status an.

> Du weißt nicht, wie du verbinden sollst? Tippe auf **ⓘ** neben dem Verbindungsstatus auf dem Startbildschirm oder oben rechts bei jedem Schritt unter „Kamera hinzufügen“. Es öffnet sich eine bebilderte Anleitung (je eine Seite für Smartphone-Hotspot, Gleiches Wi‑Fi, One-Tap-Verbindung, USB, Bluetooth und FTP) mit Screenshots von Smartphone und Kamera sowie einer Checkliste am Ende, falls keine Verbindung zustande kommt.

## Welche Verbindung passt zu dir?

| Was du möchtest | Empfehlung |
|---|---|
| Fotos empfangen, auch wenn die Kamera ausgeschaltet ist, ganz ohne Aufwand | **Bluetooth** (verkleinerte JPEGs, kostenlos) |
| Unterwegs ohne Hotspot arbeiten, aber volle Auflösung, Galerie und Fernaufnahme nutzen | **One-Tap-Verbindung** (Pro) |
| Direkt nach dem Auslösen mit höchster WLAN-Geschwindigkeit automatisch übertragen | **[FTP-Empfang](08-ftp.md)** (Pro, Hotspot erforderlich) |
| Maximale Stabilität, Video-Monitor, lange Fernaufnahme-Sessions | **USB-Kabel** (manuelles Auswählen & Herunterladen kostenlos) |
| Zuhause oder im Studio | **Gleiches Wi‑Fi** (Pro) |

## Geschwindigkeits-Richtwerte (getestet mit Nikon Zf und Pixel 10 Pro)

| Verbindungsart | Eine RAW-Datei (ca. 18 MB) |
|---|---|
| FTP-Empfang | ca. 1 Sek. (ca. 17 MB/s) |
| Wi‑Fi-Galerie-Download | ca. 1,3 Sek. (ca. 13 MB/s) |
| USB | Meist schneller als Wi‑Fi, je nach Kabel (ca. 35 MB/s mit USB-2.0-Kabel) |
| Bluetooth | Verkleinertes JPEG (ca. 2 MB), 15–20 Sek. pro Foto |

## Statuslichter auf dem Startbildschirm
Die vier Kacheln Wi‑Fi, USB, Bluetooth und FTP färben sich je nach Status ein (grau, wenn nicht verbunden):

| Farbe | Bedeutung |
|---|---|
| 🟢 Grün | Verbunden oder bereit (hellgrün bei Bluetooth = Standby, bereit für Versand bei ausgesch. Kamera) |
| 🔵 Blau | Übertragung läuft |
| 🟠 Orange | Verbindungsaufbau (blinkend) oder Aktion nötig (Berechtigung, hängt, Fehler) |
| 🔴 Rot | Wi‑Fi oder Bluetooth am Smartphone ist ausgeschaltet |

---

## Bluetooth (kostenlos, ersetzt SnapBridge)

### Koppeln
1. Kamera: **MENU → Netzwerkmenü → Mit Smart-Gerät verbinden → Pairing (Bluetooth) → Pairing starten**.
2. Falls die Kamera bereits mit SnapBridge gekoppelt war, lösche die Kopplung zuerst in SnapBridge und entferne die Kamera in den Bluetooth-Einstellungen des Smartphones (zwei Apps können nicht gleichzeitig mit derselben Kamera gekoppelt sein).
3. AeroCam: Startbildschirm „Bluetooth“ → **Kamera koppeln** → Start. Auf Smartphone und Kamera erscheint derselbe Code – bestätige auf beiden Geräten. Auf der Kamera wird dein Smartphone als `AeroCam_<Smartphone-Modell>` angezeigt.

📷 Screenshot: Bluetooth-Kachel

### Nach dem Koppeln
Nach dem Koppeln bleibt Bluetooth dauerhaft aktiv, bis du die Kopplung aufhebst (mit vorheriger Bestätigung).
- Normalerweise **lauscht** AeroCam nur im Hintergrund auf das Bluetooth-Signal der Kamera und weckt eine schlafende Kamera nicht auf.
- **Beim Einschalten der Kamera**: AeroCam verbindet sich kurz, synchronisiert Uhrzeit und GPS-Standort des Smartphones (damit die Kamera den Standort in neue Fotos schreibt) und trennt sich wieder.
- **Wenn die Kamera Fotos senden soll**: Aktiviere im Kamera-Menü „Mit Smart-Gerät verbinden“ die Option **Versand bei ausgesch. Kamera** (Send while off). Dann verbindet sich die Kamera selbstständig per Bluetooth und sendet Fotos – auch wenn sie ausgeschaltet ist.
- Empfangene Fotos sind von der Kamera erzeugte JPEGs mit ca. 2 MB (auch RAW-Aufnahmen werden zuerst von der Kamera in JPEG umgewandelt) und dauern ca. 15–20 Sekunden pro Bild. Für Originaldateien nutze Wi‑Fi, USB oder FTP.
- Um Fotos sofort abzurufen, tippe auf der Bluetooth-Kachel auf **Jetzt empfangen**.
- Nach Aus-/Einschalten von Bluetooth, Neustart des Smartphones oder App-Updates läuft der Dienst automatisch weiter. Während des Wartens zeigt Android systembedingt eine unauffällige Dauerbenachrichtigung an, die du in den Systemeinstellungen ausblenden kannst.

### Statusanzeigen der Bluetooth-Kachel
🟢 Kamera in der Nähe · Eingeschaltet / 🟢 Hellgrün: Standby (bereit für Versand bei ausgesch. Kamera) / ⚪ Kamera nicht sichtbar (zeigt Zeitpunkt der letzten Sichtung) / 🔵 Übertragung läuft / 🟠 Hängt möglicherweise / 🔴 Smartphone-Bluetooth ist aus.

Da Bluetooth nicht dauerhaft verbunden bleibt, zeigt diese Kachel an, ob die Kamera in Reichweite gehört wird und was sie gerade tut.

### Wenn die Übertragung hängt
- Kommen während einer Übertragung 30 Sekunden lang keine Daten an, trennt die App automatisch, und die Kamera versucht es später erneut; nach 20 Sekunden ohne Aktivität färbt sich die Kachel gelb („Hängt möglicherweise“).
- **Trennen und neu verbinden**: Beendet nur die aktuelle Übertragung.
- **⋮ → Bluetooth-Dienst neu starten**: Startet den gesamten Bluetooth-Hintergrunddienst neu, die Kopplung bleibt erhalten.
- Bei RAW-Aufnahmen muss die Kamera jedes Bild vor dem Senden in JPEG umwandeln. Wenn du die Kamera währenddessen bedienst (Auslöser halb drücken, fotografieren), bricht die Kamera den Versand ab. Am besten schaltest du die Kamera nach dem Fotografieren einfach aus und lässt sie im Hintergrund senden.

---

## Wi‑Fi (Pro): Drei Verbindungsarten

| Methode | Funktionsweise | Wann nutzen? |
|---|---|---|
| **One-Tap-Verbindung** (empfohlen) | Schaltet per Bluetooth das eigene Wi‑Fi der Kamera ein, das Smartphone verbindet sich automatisch | Unterwegs, wenn du keinen Hotspot öffnen möchtest |
| **Smartphone-Hotspot** (im Guide empfohlen) | Die Kamera verbindet sich mit dem mobilen Hotspot deines Smartphones | Wenn One-Tap-Verbindung instabil ist oder du FTP bzw. Aufnehmen ohne Karte nutzt |
| **Gleiches Wi‑Fi** | Smartphone und Kamera sind mit demselben Router verbunden | Zuhause oder im Studio |

### One-Tap-Verbindung
1. Schließe zuerst die **Bluetooth-Kopplung** ab.
2. Tippe auf dem Startbildschirm auf Wi‑Fi → „One-Tap-Verbindung“.
3. Gib beim ersten Mal das **Passwort** des Kamera-Wi‑Fi ein (der Netzwerkname wie `NIKON_…` wird automatisch eingetragen). Es wird nur lokal auf deinem Smartphone gespeichert.
4. Wenn Android fragt, ob die Wi‑Fi-Verbindung erlaubt werden soll, tippe auf Zulassen.
5. Sobald „Mit Kamera-Wi‑Fi verbunden“ erscheint, laufen Galerie, Fernaufnahme und automatischer Empfang über diese Verbindung. Tippe auf „Trennen“, um zu deinem normalen Wi‑Fi zurückzukehren.

Wenn Galerie oder Fernaufnahme noch nicht verbunden sind, erscheint direkt auf dem Bildschirm auch die Schaltfläche „Über Kamera-Wi‑Fi verbinden“.

> - Solange du mit dem Wi‑Fi der Kamera verbunden bist, nutzt dein Smartphone für das Internet mobile Daten.
> - One-Tap-Verbindung **funktioniert nicht mit FTP** und **unterstützt kein Aufnehmen ohne Speicherkarte** (nutze ohne Karte bitte Smartphone-Hotspot oder Gleiches Wi‑Fi).

📷 Screenshot: One-Tap-Verbindungskarte und verbundener Zustand

### Smartphone-Hotspot / Gleiches Wi‑Fi (erste Kopplung)
1. Kamera: **MENU → Netzwerkmenü → Mit PC verbinden**, und ein Netzwerkprofil erstellen (mit dem Hotspot deines Smartphones oder deinem Heim-Wi‑Fi verbinden).
   - Neuere Modelle (mit „Verbindungstyp“ im Menü): Wähle unter „Verbindungstyp“ die Option **Bildübertragung**.
   - Ältere Modelle: Wähle einfach **Mit PC verbinden**.
2. AeroCam: **Start → „＋“ Kamera hinzufügen**, und die Verbindungsart wählen (Gleiches Wi‑Fi oder Smartphone-Hotspot). Die App prüft das Netzwerk und sucht automatisch nach der Kamera; alternativ kannst du die IP manuell eingeben.
3. Auf dem Kamerabildschirm erscheint ein **4-stelliger PIN-Code**. Gib ihn auf dem Smartphone ein und drücke auf der Kamera OK.
4. Danach wird alles als „Kameraprofil“ gespeichert, sodass du beim nächsten Start direkt verbinden kannst. Du kannst mehrere Kameras und Netzwerke speichern. Nach App-Updates ist **kein erneutes Koppeln nötig**, und AeroCam findet die Kamera auch dann wieder, wenn sich ihre IP-Adresse ändert.

> Meldet die Kamera „Bereits mit einem anderen Gerät gekoppelt“, wird dieses Kameraprofil von einer anderen App belegt. Lege auf der Kamera ein neues Netzwerkprofil an und kopple erneut.

📷 Screenshot: Assistent „Kamera hinzufügen“ und PIN-Eingabe

### Prüfungen vor dem Verbinden
- Wenn du auf „Empfang starten“ tippst oder Kamera-Ordner / Fernaufnahme öffnest, prüft AeroCam zuerst das Netzwerk. Ist im Profil „Smartphone-Hotspot“ hinterlegt, der Hotspot aber ausgeschaltet (oder „Gleiches Wi‑Fi“ nicht verbunden), erscheint ein gelbes Banner (z. B. „Bitte schalte zuerst deinen Smartphone-Hotspot ein“) samt Schnellbuttons für „Hotspot-Einstellungen“ und „Wi‑Fi-Einstellungen“. Sobald du es aktiviert hast und zu AeroCam zurückkehrst, verschwindet das Banner.
- Wird die Kamera weder im Wi‑Fi noch im Hotspot gefunden, zeigt der Startbildschirm „Kamera im Netzwerk nicht gefunden“ (meist ist „Mit PC verbinden“ auf der Kamera nicht aktiv) mit dem Button „Verbindungsanleitung ansehen“.

### „Verbindungstyp“ (Connection type) an der Kamera
Bei neueren Modellen (Z9, Z8, Z6III, Zf, Z5II, Z50II…): **MENU → Netzwerkmenü → Mit PC verbinden → Verbindungstyp**
- **Bildübertragung** (Image transfer): für automatischen Empfang und das Durchsuchen der Kamera-Speicherkarte.
- **Kamerasteuerung** (Camera control): für Fernaufnahme und Aufnehmen ohne Speicherkarte.

Beim Umschalten trennt sich das Kamera-Wi‑Fi kurz; AeroCam verbindet sich automatisch neu, ohne dass du neu koppeln musst. Öffnest du die Fernaufnahme, während die Kamera noch auf „Bildübertragung“ steht, zeigt die App die Schritte zum Umschalten an.

---

## USB-Kabel
Schneller und stabiler als Wi‑Fi, **kein Koppeln nötig**, und du musst die Kamera nicht vorher hinzufügen.
1. Stelle an der Kamera die USB-Option auf **MTP/PTP** (nicht „iPhone“ oder „UVC/UAC“).
2. Verwende ein **datenfähiges** USB‑C-Kabel (manche Kabel sind reine Ladekabel). Ein USB-3-Kabel mit 5Gbps / 10Gbps sorgt für höhere Geschwindigkeit.
3. Auf dem Startbildschirm zeigt die USB-Kachel „Z f erkannt · Zugriffsberechtigung erforderlich“ → tippe auf „Zugriff erlauben“ und bestätige die Android-Abfrage einmalig.

### Farben der USB-Kachel
| Farbe | Bedeutung |
|---|---|
| ⚪ Grau | Keine Kamera erkannt (oder reines Ladekabel) |
| 🟠 Orange | Kamera erkannt; Zugriffsberechtigung erforderlich |
| 🔴 Rot | Kamera-USB steht nicht auf MTP/PTP, Zugriff verweigert oder Test fehlgeschlagen (Grund wird angezeigt) |
| 🟢 Grün | Per USB-Kabel verbunden |

### Während der USB-Verbindung
- Kamera-Ordner, Fernaufnahme und automatischer Empfang **wechseln automatisch auf USB**; beim Abziehen des Kabels geht es automatisch zurück zu Wi‑Fi. Auch wenn du während einer Wi‑Fi-Fernaufnahme ein Kabel ansteckst, wechselt die Verbindung nahtlos auf USB (außer während laufender Intervallaufnahme, Belichtungsreihe oder Langzeitbelichtung/Bulb).
- **USB-Empfang** (Pro): Tippe auf der USB-Kachel auf „Empfang starten“, um neu aufgenommene Fotos sowie über „An PC senden“ verschickte Bilder auf dem Smartphone zu speichern. Standardmäßig startet der Empfang beim Einstecken automatisch (**Einstellungen → Aufnahme → „Beim Anschließen eines USB-Kabels Empfang automatisch starten“**).
- **Zeitsynchronisation**: Synchronisiert beim Einstecken einmalig die Kamerauhr (korrigiert nur bei > 2 Sek. Abweichung; fragt vorher nach bei > 1 Tag Abweichung).
- **Wachhalten**: Sendet alle 10 Sekunden ein kleines Signal, solange Kamera-Ordner oder Fernaufnahme geöffnet sind, damit die Kamera nicht einschläft; stoppt nach 30 Minuten Inaktivität oder bei niedrigem Akku.
- Dein Smartphone lädt möglicherweise die Kamera über USB – bei längeren Sessions empfiehlt sich eine Powerbank.
- **USB-Test** (⋮ oben rechts auf der USB-Kachel): Prüft Verbindung, Kamerainfos, Speicherkarten, Live-View-Bildrate und Lesegeschwindigkeit.

📷 Screenshot: USB-Kachel

---

## FTP
Die Kamera sendet Fotos direkt nach der Aufnahme selbstständig per Push ans Smartphone – siehe [Kapitel 8](08-ftp.md).
