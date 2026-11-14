<!-- translated from zh-TW at commit 968641f -->

# 11. Häufige Fragen und Fehlerbehebung

## Allgemein
**Kann ich Fotos von der Kamera aufs Smartphone übertragen, ohne auf Pro zu upgraden?**
Ja. In der kostenlosen Version kannst du verkleinerte JPEGs mit ca. 2 MP automatisch per Bluetooth empfangen oder die Speicherkarte der Kamera über ein USB-Kabel durchsuchen und Originale in voller Auflösung manuell auswählen und herunterladen.

**Kosten die Beta oder die Testschlüssel Geld?**
Nein. Beides wird ausschließlich kostenlos auf GitHub unter AeroCam-Releases veröffentlicht. Wenn jemand Geld von dir verlangt, ist das kein offizieller Kanal.

**Beim Öffnen erscheint „Dies ist keine offizielle Version“**
Die APK wurde von Dritten neu verpackt, akzeptiert keine Testschlüssel und könnte unerwünschten Code enthalten. Deinstalliere sie und lade sie erneut von AeroCam-Releases herunter.

**Nach einem Update sind meine gekoppelte Kamera und der Testschlüssel weg**
Ab Version 92.03.09 werden neuere Builds als eigene App installiert und übernehmen keine Daten aus älteren Builds. Kopple deine Kamera erneut und gib den Testschlüssel noch einmal ein.

**Wo werden Fotos gespeichert?**
Fotos landen in `Pictures/AeroCam`, Videos in `Movies/AeroCam` und sonstige Dateien in `Download/AeroCam`. Google Fotos und andere Galerie-Apps sehen sie direkt. Dateien aus Versionen vor 92.03.09 bleiben in ihrem ursprünglichen Ordner.

**Ich habe ein Foto auf dem Smartphone gelöscht und möchte es erneut übertragen**
Sende es einfach noch einmal von der Kamera – AeroCam erkennt, dass die Datei nicht mehr auf dem Smartphone liegt, und speichert sie erneut.

**Fotos tauchen nach dem Wiederherstellen aus dem Papierkorb oder einer Neuinstallation nicht in der Galerie auf**
Führe **Einstellungen → Speicher & Akku → „Smartphone-Fotos neu scannen“** aus.

---

## Verbindung
**Keine Verbindung zur Kamera per Wi‑Fi möglich**
1. Stelle sicher, dass die Kamera auf dem Bildschirm „Mit PC verbinden“ steht und das Wi‑Fi-Symbol sichtbar ist; drücke den Auslöser halb, falls das Display ausgegangen ist.
2. Prüfe den Verbindungstyp: **Bildübertragung** für Auto-Empfang und Galerie; **Kamerasteuerung** für Fernaufnahme und Aufnehmen ohne Speicherkarte.
3. Smartphone-Hotspot-Modus: Prüfe, ob dein Hotspot eingeschaltet und die Kamera damit verbunden ist.
4. Gleiches-Wi‑Fi-Modus: Prüfe, ob Smartphone und Kamera exakt denselben Netzwerknamen nutzen (Smartphones wechseln manchmal automatisch zu einem anderen WLAN oder zu mobilen Daten).
5. Probiere die **One-Tap-Verbindung** – ganz ohne Hotspot oder Router.
6. Tippe auf **ⓘ** und gehe die bebilderte Verbindungsanleitung Schritt für Schritt durch.

**Im Hotel- oder Messe-WLAN wird die Kamera nie gefunden**
Öffentliche Wi‑Fi-Netzwerke blockieren meist den Datenverkehr zwischen Geräten. Wechsle auf deinen Smartphone-Hotspot oder die One-Tap-Verbindung.

**Die Kamera meldet „Bereits mit einem anderen Gerät gekoppelt“**
Dieses Netzwerkprofil auf der Kamera ist mit einer anderen App gekoppelt. Erstelle auf der Kamera ein neues Netzwerkprofil und kopple erneut.

**One-Tap-Verbindung findet das Kamera-Wi‑Fi nicht**
Nach dem Bluetooth-Befehl braucht die Kamera 10–30 Sekunden, um ihr Wi‑Fi zu starten; AeroCam versucht es automatisch erneut. Schlägt es weiterhin fehl, prüfe das Wi‑Fi-Passwort der Kamera.

**Der Smartphone-Hotspot schaltet sich ständig aus**
Manche Smartphones deaktivieren ihren Hotspot, wenn verbundene Geräte keine Internetdaten nutzen. Deaktiviere „Hotspot automatisch ausschalten“ in den Hotspot-Einstellungen deines Smartphones oder nutze die One-Tap-Verbindung.

**Nach Aus- und Einschalten des Hotspots verbindet sich die Kamera nicht wieder**
Die IP-Adresse deines Smartphone-Hotspots hat sich möglicherweise geändert. Der Wi‑Fi-Auto-Empfang findet die Kamera von selbst; bei FTP musst du die Server-IP an der Kamera aktualisieren.

**Beim Anschließen per USB passiert nichts**
1. Prüfe, ob die USB-Einstellung der Kamera auf **MTP/PTP** steht.
2. Stelle sicher, dass das Kabel Datenübertragung unterstützt (manche Kabel sind reine Ladekabel).
3. Tippe bei der Android-USB-Abfrage auf Zulassen.
4. Tippe oben rechts auf der USB-Kachel auf `⋮` → **USB-Test**, um zu sehen, welcher Schritt fehlschlägt.

**Der Hintergrundempfang bricht häufig ab**
Deaktiviere die Akku-Optimierung unter **Einstellungen → Speicher & Akku**. Bei Smartphones von Xiaomi, OPPO und ähnlichen Marken stelle AeroCam zusätzlich in den Systemeinstellungen auf „Nicht eingeschränkt“.

---

## Bluetooth
**Die Bluetooth-Fotoübertragung hängt**
- Bei RAW-Aufnahmen muss die Kamera jedes Bild vor dem Senden in JPEG umwandeln, und jede Bedienung der Kamera bricht den Transfer ab. Am zuverlässigsten klappt es, wenn du die Kamera nach dem Fotografieren ausschaltest und sie im Hintergrund senden lässt.
- Tippe auf der Bluetooth-Kachel auf **Trennen und neu verbinden** oder **⋮ → Bluetooth-Dienst neu starten** (deine Kopplung bleibt erhalten).

**Drücken von AF im Bluetooth-Fernauslöser fokussiert nicht**
Die Kamera muss den Autofokus per halb gedrücktem Auslöser zulassen. Wenn du Back-Button-AF (AF‑ON) nutzt, prüfe in den Individualfunktionen der Kamera, ob **AF-Aktivierung** (AF activation) auf **Auslöser/AF-ON** steht.

**Werden beim Empfang desselben Fotos über Bluetooth und Wi‑Fi zwei Kopien gespeichert?**
Standardmäßig nicht: Sobald Wi‑Fi die Originaldatei empfängt, wird die kleinere Bluetooth-Kopie automatisch gelöscht. Du kannst dies unter **Einstellungen → Empfang & Benachrichtigungen → „Bereits per Bluetooth empfangene Fotos“** ändern.

---

## Fernaufnahme
**Belichtungszeit oder ISO lassen sich nicht verstellen**
- Die Belichtungszeit erfordert Modus S oder M, die Blende Modus A oder M; schalte vor dem manuellen Ändern von ISO die ISO-Automatik aus.
- Bei Kameras mit physischen Einstellrädern wie der Zf: Stelle das Zeitenrad auf **1/3 STEP** und das ISO-Rad auf **C**.

**Tippen in die Vorschau verschiebt den Fokuspunkt nicht**
Stelle die AF-Messfeldsteuerung der Kamera auf einen Modus mit beweglichem Messfeld (z. B. Einzelfeld-AF). Bei automatischer Messfeldsteuerung wählt die Kamera selbst.

**Auf dem Start-Dashboard fehlen einige Werte (Objektiv, Restaufnahmen, Auslösungen)**
Manche Kameras melden bestimmte Daten nur in bestimmten Modi. Das Umschalten auf „Kamerasteuerung“ und Öffnen der Fernaufnahme macht sie meist verfügbar. Für die Auslösezahl muss mindestens ein Foto auf der Speicherkarte sein.

**Wo sehe ich die genaue Farbtemperatur (Kelvin)?**
Nikon speichert den gemessenen Kelvin-Wert verschlüsselt in den MakerNotes, daher zeigen die „Details“ nur den Namen der Weißabgleich-Voreinstellung an.

---

## Speicherziel und Aufnehmen ohne Speicherkarte
**Ohne eingelegte Karte passiert beim Drücken des Auslösers nichts**
Prüfe, ob an der Kamera **Auslösesperre** auf **Auslösung möglich** steht und AeroCam verbunden ist (Statusleiste zeigt „Nur Smartphone“).

**Auf der Kamera erscheint „DEMO“ auf den Fotos**
Ist keine Karte eingelegt und AeroCam nicht im Modus „Nur Smartphone“ verbunden, markiert die Kamera Aufnahmen als **DEMO** und speichert sie nicht. Lege eine Karte ein oder fotografiere mit verbundenem AeroCam.

**Fotos kommen nicht auf dem Smartphone an und oben erscheint ein rotes Banner**
- „Kamera ist im Modus ‚Bildübertragung‘“: Aufnehmen ohne Karte erfordert **Kamerasteuerung**. Schalte an der Kamera um; sie verbindet sich neu und überträgt die zwischengespeicherten Bilder automatisch.
- „One-Tap-Wi‑Fi: Keine Speicherkarte“: One-Tap-Verbindung unterstützt kein Aufnehmen ohne Karte. Lege eine Karte ein oder wechsle zu Smartphone-Hotspot / Gleiches Wi‑Fi.

**Es erscheint „Verbindung unterbrochen“**
Beim Speichern nur aufs Smartphone löst ein Verbindungsabbruch von über 10 Sekunden eine Warnung aus, da währenddessen aufgenommene Fotos auf keiner Karte gespeichert werden. Sobald die Verbindung wieder steht, läuft AeroCam automatisch weiter.

---

## Bearbeitung und Bildstile
**NEF lässt sich nicht öffnen oder bearbeiten**
High-Efficiency- / High-Efficiency★-NEFs werden über ihr eingebettetes JPEG in voller Größe bearbeitet; Dateien mit nur einer kleinen Vorschau können nicht bearbeitet werden. Um volle RAW-Dateien auf dem Smartphone zu entwickeln, stelle die Kamera auf **Verlustfreie Komprimierung** – siehe [Kapitel 6](06-edit.md#auf-dem-smartphone-bearbeitbares-raw-kamera-raw-komprimierung-umschalten).

**Der .np3-Look weicht von der Kamera ab**
Der Smartphone-Editor simuliert Tonwertkurven und Sättigung; Farbmischer und Color Grading werden noch nicht simuliert, daher ist das Ergebnis eine Annäherung. Wurde ein Picture Control bereits bei der JPEG-Aufnahme eingerechnet, addieren sich die Effekte.

**Nach dem Schreiben von .np3 auf die Kamera sehen die Farben anders aus**
Benutzerdefinierte Kameraspeicherplätze übernehmen nur **Basis + Kurve + Schärfung**; Sättigung, Farbmischer und Color Grading lassen sich nicht über die Verbindung schreiben. Für das vollständige Ergebnis kopiere die `.np3`-Datei auf eine Speicherkarte und importiere sie über das Kameramenü.

**Panorama-Stitching schlägt fehl oder lässt Fotos aus**
Jede Aufnahme benötigt ca. 30 % Überlappung zu den Nachbarbildern. Nicht zuordenbare Dateien werden namentlich genannt, und Rasterpanoramen erfordern alle Kacheln vor dem Zusammenfügen.

---

## FTP
**Die Kamera zeigt Err.31 oder Err.32 an**
Aktualisiere auf die neueste Beta und prüfe, ob IP-Adresse, Port `2121`, Benutzername `aerocam` und Passwort an der Kamera exakt mit der FTP-Kachel in AeroCam übereinstimmen und der Passivmodus eingeschaltet ist.

**Die Kamera meldet einen Anmeldefehler**
Das Passwort muss exakt (inklusive Groß-/Kleinschreibung) mit der Anzeige in AeroCam FTP übereinstimmen. Falls du auf „Neu generieren“ getippt hast, aktualisiere das Passwort auch an der Kamera.

**Während FTP läuft, verbinden sich Kamera-Ordner oder Fernaufnahme nicht**
Im FTP-Modus akzeptiert die Kamera keine Wi‑Fi-Verbindungen für Galerie oder Fernaufnahme. Nutze ein USB-Kabel oder stoppe den FTP-Empfang und stelle die Kamera wieder auf „Mit PC verbinden“.

---

## Sonstiges
**Die App stürzt ab**
Öffne AeroCam erneut, gehe zu **Einstellungen → Support → „Diagnoseinfos kopieren“** und füge den Text beim [Melden des Problems](12-report.md) ein – er enthält den Fehlerort des letzten Absturzes.

**Wie schalte ich die anonymen Nutzungsstatistiken aus?**
Deaktiviere **Einstellungen → Support → „Anonyme Nutzungsstatistiken senden“** – siehe [Datenschutz und anonyme Statistiken](10-privacy.md).
