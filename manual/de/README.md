<!-- translated from zh-TW at commit 968641f -->

# AeroCam Benutzerhandbuch (Deutsch)

> Entspricht **Beta 92.04.08.10** (aktualisiert am 2026-11-15). Zeilen mit 📷 sind Platzhalter für Screenshots, die später ergänzt werden.

Mit AeroCam überträgst du Fotos direkt von deiner Kamera auf dein Android-Smartphone. Außerdem kannst du die Kamera vom Smartphone aus fernsteuern, Fotos bearbeiten und Bildstile auf die Kamera schreiben. Derzeit wird die **Nikon Z-Serie** unterstützt; weitere Marken folgen später.

AeroCam ist eine unabhängig entwickelte Drittanbieter-App und steht in keiner Verbindung zu Nikon oder anderen Kameraherstellern und wird von diesen nicht autorisiert.

## Inhalt

1. [Installation und Erste Schritte](01-install.md): Installation, Berechtigungen, Bildschirmübersicht, Testschlüssel, Updates, Sprache
2. [Kamera verbinden](02-connect.md): Bluetooth, Wi‑Fi (One-Tap-Verbindung / Smartphone-Hotspot / Gleiches Wi‑Fi), USB-Kabel, Auswahlhilfe, Verbindungsanleitung
3. [Automatischer Empfang und Speichern](03-receive.md): Empfang starten/pausieren, Empfangsregeln, Ordner und Dateinamen, Aufnehmen ohne Speicherkarte, Foto-Standort, Kamera-Dashboard, Verlauf
4. [Galerie](04-gallery.md): Kamera-Speicherkarte, Smartphone-Fotos, Herunterladen und Löschen, Bewertungen, Speicherkarten-Backup, QR-Code-Freigabe
5. [Fernaufnahme und Fernsteuerung](05-remote.md): Wi‑Fi-/USB-Fernaufnahme, Aufnahmemethoden, Aufnahmehilfen, Bluetooth-Fernauslöser, Video-Monitor, Sternenhimmel-Modus
6. [Fotobearbeitung und Bildstile](06-edit.md): Editor, .np3-Stilvorschau, RAW auf dem Smartphone bearbeiten, Kamerastile C1–C9, Panorama-Stitching, Rauschreduzierung (Shake-Serie)
7. [Einstellungen im Detail](07-settings.md)
8. [FTP-Empfang](08-ftp.md): Fotos nach der Aufnahme automatisch aufs Smartphone senden
9. [Kostenlos / Pro / Cine](09-tiers.md)
10. [Datenschutz und anonyme Statistiken](10-privacy.md)
11. [Häufige Fragen und Fehlerbehebung](11-faq.md)
12. [Problem melden](12-report.md)

## Unterstützte Kameras

| Modell | Automatischer Empfang, Kameragalerie | Fernaufnahme | Status |
|---|---|---|---|
| Z9, Z8, Z6III, Zf, Z5II, Z50II, ZR und andere Modelle mit „Verbindungstyp“ (Connection type) im Menü | ✅ | ✅ | Auf der Zf getestet; Berichte zu anderen Modellen willkommen |
| Z6, Z7, Z6II, Z7II, Z5, Z50, Zfc, Z30 und ältere Modelle | ✅ | ❌ (wird vom Verbindungsprotokoll dieser Modelle nicht unterstützt) | Berichte willkommen |
| Canon, Sony, Fujifilm | In Vorbereitung | In Vorbereitung | |

Wenn du AeroCam mit einem anderen Kameramodell getestet hast, teile uns bitte über [Kamerabericht](https://github.com/AeroCam-Group/AeroCam-Releases/issues/new/choose) mit, welche Funktionen laufen und welche nicht.

## Voraussetzungen
- Ein Smartphone mit Android 10 oder höher.
- Eine Kamera der Nikon Z-Serie.

## Verwendete Begriffe
| Begriff in diesem Handbuch | Bedeutung |
|---|---|
| Kameragalerie / Kamera-Speicherkarte | Fotos auf der Speicherkarte der Kamera, die über eine Verbindung auf dem Smartphone durchsucht werden |
| Smartphone-Fotos / Smartphone-Galerie | Fotos, die bereits auf dem Smartphone gespeichert sind |
| RAW | Nikon NEF-Dateien |
| JPEG.S | Komprimiertes JPEG (aus RAW extrahiertes JPEG, auf dem Smartphone neu komprimiertes JPEG oder per Bluetooth gesendete verkleinerte Version), Dateiendung `_S.JPG` |
| Picture Control | Farbprofile der Kamera wie Standard oder Ausgewogen; eigene Profile liegen auf C1–C9 |
| Pro / Cine | Kostenpflichtige Stufen; während der Beta-Phase kannst du sie mit dem kostenlosen Testschlüssel nutzen – siehe [Kapitel 9](09-tiers.md) |
