<!-- translated from zh-TW at commit 968641f -->

# 3. Automatischer Empfang und Speichern

## Kamera-Dashboard
Nach dem Verbinden zeigt die obere Karte auf dem Startbildschirm den Live-Status deiner Kamera:

| Punkt | Inhalt |
|---|---|
| Modell, Objektiv | Zum Beispiel „Nikon Z f“ und „NIKKOR Z 24–120 mm f/4“ |
| Akku | Prozentwert (wird ab 20 % oder weniger rot) |
| Verbindungsart | Smartphone-Hotspot, Gleiches Wi‑Fi, Kamera-Wi‑Fi oder USB |
| Speicherkarten | Belegter/gesamter Speicherplatz und verbleibende Aufnahmen je Karte; zwei Kartenslots werden getrennt aufgeführt |
| Bildqualität | Zum Beispiel `RAW` oder `JPEG Fine★ L`; aktualisiert sich automatisch beim Ändern der Qualität oder Einlegen/Entnehmen von Karten |
| Speicherziel | Zum Beispiel „Speichern unter: Karte ✓“ – siehe [Speicherziel und Aufnehmen ohne Speicherkarte](#speicherziel-und-aufnehmen-ohne-speicherkarte) unten |
| Übertragung | Aktueller Status, oben rechts „Verlauf ›“ |
| Kamerastile | Zuletzt ausgelesene Plätze C1–C9 – siehe [Kapitel 6](06-edit.md#kamerastile-c1c9-pro) |

Werte, die die Kamera im aktuellen Modus nicht meldet, werden ausgeblendet. Wenn du auf „Kamerasteuerung“ umschaltest und die Fernaufnahme öffnest, stehen meist mehr Statuswerte zur Verfügung.

### Kameras verwalten
Klappe **Kameras verwalten (n)** unter dem Dashboard aus, um Kameras zu bearbeiten, zu löschen oder hinzuzufügen. Die Detailseite jeder Kamera zeigt:
- Modell, Seriennummer (mittlere Stellen maskiert; zum Anzeigen antippen), Firmware-Version, **Auslösungen** und Auslesedatum.
- **Monatliche Auslösungen**: Balkendiagramm der letzten 6 Monate (Daten werden ab Nutzungsbeginn erfasst).
- Letzte Verbindungszeit, Verbindungsart, Objektiv, Akkustand und freier Speicherplatz auf den Karten.
- Anzahl der ans Smartphone übertragenen Dateien, Datum der ersten Verbindung und gespeicherte Netzwerkprofile.

Die Auslösezahl wird aus den Metadaten des neuesten Fotos auf der Speicherkarte gelesen; daher muss mindestens ein Foto auf der Karte sein.

### Warnung bei niedrigem Akku
Sendet eine Benachrichtigung, wenn der Kamera-Akku auf den Schwellenwert (Standard 15 %) fällt. Eine erneute Warnung erfolgt erst, wenn der Akku wieder mindestens 5 % über dem Schwellenwert lag. Einstellbar unter **Einstellungen → Empfang & Benachrichtigungen**.

📷 Screenshot: Kamera-Dashboard

---

## Automatischer Empfang (Pro)
1. Tippe auf dem Startbildschirm auf Wi‑Fi → **Empfang starten**. Die App hält im Hintergrund die Verbindung zur Kamera (in der Benachrichtigungsleiste sichtbar).
2. Drücke bei der Bildwiedergabe auf der Kamera **i → An PC senden / Zum Senden auswählen** (Send to PC / Select to send – Menütext je nach Modell unterschiedlich), und die Fotos werden direkt ans Smartphone übertragen.

Wenn Fotos sofort beim Drücken des Auslösers automatisch übertragen werden sollen, nutze [FTP-Empfang](08-ftp.md). Steckt ein USB-Kabel, wechselt der Empfang automatisch auf USB.

### Empfang pausieren
Während der Wi‑Fi-Auto-Empfang läuft, kannst du oben rechts in der Karte „Übertragung“ auf **⏸ Pause** (oder in der Benachrichtigung auf „Pause“) tippen:
- Das Wi‑Fi bleibt verbunden, Kamera-Ordner und Fernaufnahme funktionieren normal weiter.
- Auf der Kamera vorgemerkte Fotos warten, bis du auf **Empfang fortsetzen** tippst, und werden dann der Reihe nach übertragen. Ein gerade laufender Transfer wird noch zu Ende geführt.
- Der Empfang wird automatisch fortgesetzt, wenn du auf Fortsetzen tippst, den Empfang stoppst, die App aus den letzten Anwendungen wischst, das Wi‑Fi abbricht, die Kamera ausschaltest oder ein USB-Kabel anschließt.

### Bei Verbindungsabbruch
- Bricht die Verbindung ab, verbindet sich AeroCam automatisch neu. Nach mehreren Fehlversuchen sucht die App erneut über die Kamera-ID, sodass die Kamera auch bei geänderter IP-Adresse gefunden wird.
- **Kamera wechselt zur Bluetooth-Übertragung**: Da die Kamera nur einen Funkchip besitzt, schaltet sie während des Sendens per Bluetooth das Wi‑Fi ab. Auf dem Startbildschirm erscheint „Kamera sendet Fotos per Bluetooth… Wi‑Fi verbindet sich danach automatisch neu“ – dies gilt nicht als Fehler.
- **Kamera-Ordner oder Fernaufnahme leiht sich die Verbindung aus**: Die Kamera erlaubt nur eine Verbindung gleichzeitig. Öffnest du Kamera-Ordner oder Fernaufnahme, pausiert der Auto-Empfang und läuft nach dem Verlassen automatisch weiter.
- **Kamera im Wi‑Fi nicht auffindbar**: Nach Ablauf des Zeitlimits (Standard 3 Minuten) stoppt der Empfang automatisch und benachrichtigt dich, um Akku zu sparen. Das Limit lässt sich unter **Einstellungen → Empfang & Benachrichtigungen** anpassen.

---

## Empfangsregeln
Diese Einstellungen findest du unter **Einstellungen → Empfang & Benachrichtigungen**. Sie gelten gleichermaßen für Wi‑Fi, USB und FTP.

### Empfangene Dateitypen
Wähle aus, was gespeichert werden soll: Alle Dateien, Nur JPG, JPG + RAW, Fotos + Videos oder Benutzerdefiniert (JPEG, RAW, HEIF, TIFF, Video, Sonstige).

Dazu drei zusätzliche Schalter (Pro):

| Schalter | Funktion |
|---|---|
| **Bei RAW nur JPEG speichern** | Extrahiert beim Empfang einer RAW-Datei nur das darin eingebettete JPEG in voller Größe (meist 2–5 MB statt 20–50 MB RAW) bei voller Auflösung und mit allen EXIF-Daten als `DSC_1234_S.JPG`. Ideal für Social Media und schnelles Sichten |
| **Komprimiertes JPEG speichern** | Komprimiert eingehende Kamera-JPEGs auf dem Smartphone neu (`_S.JPG`, gleiche Pixelauflösung, Qualität wie in den Galerie-Einstellungen gewählt) |
| **Komprimierte Kopie ersetzen, wenn Original eintrifft** | Löscht die `_S.JPG`-Kopie auf dem Smartphone, sobald das Original-JPEG gespeichert wurde |

> Um RAW-Dateien zu empfangen, stelle die Bildqualität an der Kamera auf RAW oder RAW+JPEG und wähle im Kamera-Menü „Mit PC verbinden“ unter den Sendeoptionen RAW+JPEG (nicht „Nur JPEG“). Die Menübezeichnung hängt vom Kameramodell ab.

### Weitere Regeln
| Regel | Beschreibung |
|---|---|
| Empfangsmodus | Kontinuierlich empfangen oder nach einer Datei stoppen |
| Große Videos | Videos oberhalb des Schwellenwerts (Standard 1024 MB) werden beim Auto-Empfang übersprungen, als „Gefiltert“ protokolliert und können manuell geladen werden |
| Speicherordner | Nach Kamera, Nach Datum, Nach Kamera und Datum oder Nach Dateityp |
| Dateiname | Original-Kameraname (`DSC_1234.NEF`), Datumspräfix (`20261011_DSC_1234.NEF`) oder Datums- & Zeitpräfix (`20261011_153012_DSC_1234.NEF` – sortiert Fotos mehrerer Kameras chronologisch). Gilt nur für neu gespeicherte Dateien |

### Speicherorte
- Fotos: `Pictures/AeroCam/…`
- Videos: `Movies/AeroCam/…`
- Sonstige Dateien: `Download/AeroCam/…`

Andere Apps wie Google Fotos sehen diese Dateien sofort. Nach einer Neuinstallation von AeroCam kannst du über **Einstellungen → Speicher & Akku → „Smartphone-Fotos neu scannen“** früher gespeicherte Bilder wieder in die Galerie aufnehmen.

### Duplikaterkennung
- Wird anhand von Kamera-Seriennummer, Dateiname, Dateigröße, Aufnahmezeit und Datei-Hash geprüft. Duplikate werden übersprungen und im Verlauf als „Duplikat“ markiert.
- Löscht du ein Foto auf dem Smartphone (auch im Papierkorb) und sendest es erneut, speichert AeroCam es wieder.
- Um dasselbe Foto erneut zu senden, musst du den Empfang nicht stoppen und neu starten.

### Wenn dasselbe Foto per Bluetooth und Wi‑Fi eintrifft
Da Wi‑Fi die volle Auflösung überträgt, hat Wi‑Fi Vorrang:
- Trifft Wi‑Fi zuerst ein und Bluetooth sendet später: Die Bluetooth-Kopie wird ignoriert.
- Trifft Bluetooth zuerst ein und Wi‑Fi empfängt dasselbe Foto später, gilt **Einstellungen → Empfang & Benachrichtigungen → „Bereits per Bluetooth empfangene Fotos“**:
  - **Bei Wi‑Fi-Empfang durch Original ersetzen** (empfohlen): Speichert die Datei in voller Größe und löscht die kleinere Bluetooth-Version.
  - **Nicht erneut über Wi‑Fi herunterladen**.
  - **Beide Versionen behalten**.
- Original-RAW-Dateien werden immer empfangen.

---

## Speicherziel und Aufnehmen ohne Speicherkarte
Legt fest, wo Fotos beim Auslösen gespeichert werden. AeroCam prüft, ob eine Speicherkarte eingelegt ist, und wählt automatisch:
- **Karte eingelegt**: Nutzt **Einstellungen → Aufnahme → Speicherziel**:
  - **Speicherkarte**: Speichert auf der Karte in der Kamera.
  - **Karte + Smartphone** (Pro): Speichert auf der Karte und überträgt gleichzeitig eine Kopie aufs Smartphone.
- **Keine Karte eingelegt** (Pro): Wechselt automatisch zu **Nur Smartphone (Aufnehmen ohne Karte)**. Du kannst ganz normal auslösen und die Fotos landen direkt auf dem Smartphone, benannt nach Aufnahmezeit (z. B. `AC_20261025_193805.JPG`). Sobald du eine Karte einlegst, schaltet die App automatisch zurück.

Funktioniert auf Start, Kamera-Ordner und Fernaufnahme – sowohl per Wi‑Fi als auch per USB.

**Ersteinrichtung:**
1. Stelle im Individualfunktionen-Menü der Kamera **Auslösesperre** (Slot empty release lock) auf **Auslösung möglich** (Enable release), sonst blockiert die Kamera ohne Karte den Auslöser.
2. Stelle bei Wi‑Fi-Verbindung den Verbindungstyp der Kamera auf **Kamerasteuerung** (Camera control). Steht er auf „Bildübertragung“, erinnert dich AeroCam ca. 3 Sekunden nach dem ersten Bild ans Umschalten; das Foto bleibt im Kameraspeicher und wird nach dem Umschalten automatisch übertragen. Per USB gibt es diese Einschränkung nicht.
3. One-Tap-Verbindung unterstützt kein Aufnehmen ohne Karte – nutze stattdessen Smartphone-Hotspot oder Gleiches Wi‑Fi.

**Statusleiste verstehen** (oben auf Start und Kamera-Ordner):

| Anzeige | Bedeutung |
|---|---|
| Speichern unter: Karte ✓ | Speichert auf der Speicherkarte der Kamera |
| Speichern unter: Karte + Smartphone ✓ | Speichert auf Karte und Smartphone |
| Speichern unter: Nur Smartphone (keine Karte in der Kamera) | Fotos werden direkt ans Smartphone gesendet |
| Kamera ist im Modus „Bildübertragung“… (rot) | Bitte Verbindungstyp auf „Kamerasteuerung“ umstellen |
| One-Tap-Wi‑Fi: Keine Speicherkarte, Aufnahme nicht möglich (rot) | Karte einlegen oder auf Hotspot / Gleiches Wi‑Fi wechseln |
| Speicherkarte voll (rot) | Karte wechseln oder Platz schaffen (wechselt nicht automatisch auf Nur Smartphone) |
| Keine Speicherkarte in der Kamera, Aufnahme nicht möglich (rot) | Kostenlose Version oder weniger als 1 GB freier Speicher auf dem Smartphone |

> Ohne Speicherkarte sind keine Videoaufnahmen möglich, und Serienaufnahmen sind langsamer, da jedes Bild einzeln ans Smartphone übertragen werden muss.

---

## Foto-Standort (GPS)
Unter **Einstellungen → Empfang & Benachrichtigungen → Foto-Standort** gibt es zwei Schalter:
- **Standort an Kamera senden (Bluetooth)** (standardmäßig an): Beim Einschalten der Kamera oder bei Bluetooth-Übertragung sendet dein Smartphone seinen GPS-Standort an die Kamera, die ihn direkt in neue Fotos schreibt.
- **Standort zu empfangenen JPEGs hinzufügen (Smartphone)**: Ergänzt den Smartphone-Standort anhand der Aufnahmezeit in JPEGs, die per Wi‑Fi, USB, FTP, Galerie-Download oder Fernaufnahme eintreffen. Fragt beim ersten Empfangsstart einmalig nach.
  - RAW-Dateien werden niemals verändert; Fotos mit vorhandenen GPS-Daten behalten ihre ursprünglichen Koordinaten.
  - Während einer Session aufgezeichnete Standortdaten bleiben nur auf deinem Smartphone und werden nach 24 Stunden gelöscht.
  - Passt die Aufnahmezeit zu keinem aufgezeichneten Punkt, wird nichts geschrieben (lieber kein Standort als ein falscher).
  - AeroCam muss beim Starten des Empfangs geöffnet sein, damit der Standort aufgezeichnet werden kann.

> Eingebettete GPS-Koordinaten bleiben beim Teilen der Originaldatei erhalten. Bei der QR-Code-Freigabe wird der Standort standardmäßig entfernt – siehe [Kapitel 4](04-gallery.md#qr-code-freigabe).

---

## Verlauf
Tippe oben rechts in der Karte „Übertragung“ auf dem Startbildschirm auf **Verlauf ›**. Zeigt alle Ergebnisse von Auto-Empfang, Galerie-Downloads und Fernaufnahmen (Erfolgreich, Duplikat, Übersprungen, Fehlgeschlagen) samt Vorschaubildern.
- Antippen öffnet eine Vollbildvorschau in der App.
- Du kannst suchen, nach Kamera filtern oder den Verlauf leeren. Beim Leeren des Verlaufs werden keine Dateien auf dem Smartphone gelöscht.
