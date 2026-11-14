<!-- translated from zh-TW at commit 968641f -->

# 8. FTP-Empfang (Pro)

Deine Kamera **sendet Fotos direkt nach jeder Aufnahme per FTP an dein Smartphone** – ohne dass du Bilder an der Kamera auswählen oder die Galerie öffnen musst. Auf einer Nikon Zf getestet, landet jede ca. 18 MB große RAW-Datei in rund 1 Sekunde auf dem Smartphone.

AeroCam bringt einen eigenen FTP-Server mit, sodass **du keinen externen Server einrichten musst**.

## Ideal für
- Events, Hochzeiten und Sport: Fotos laufen schon während des Fotografierens live aufs Smartphone.
- Sofortige Bildkontrolle und Teilen auf Social Media direkt nach dem Auslösen.

## Voraussetzungen
- Eine Kamera mit integriertem FTP-Upload (Nikon Z f, Z 8, Z 9, Z 6III usw.).
- Der **mobile Hotspot** deines Smartphones ist eingeschaltet und die Kamera damit verbunden (oder beide sind mit demselben Router verbunden).
- Eine Speicherkarte in der Kamera (FTP überträgt Dateien von der Karte).

## Ersteinrichtung
1. Schalte den Hotspot deines Smartphones ein.
2. Öffne in AeroCam auf dem Startbildschirm **FTP** → tippe ganz oben auf **Empfang starten**. Die Karte zeigt die Serverdaten an – tippe auf ein Feld, um es zu kopieren:
   - Serveradresse (z. B. `10.14.29.30`)
   - Port: `2121`
   - Benutzername: `aerocam`
   - Passwort: 8-stelliges, von der App erzeugtes Passwort (jederzeit über „Neu generieren“ änderbar)
   - Passivmodus (PASV): **Ein**
3. Kamera: **MENU → Netzwerkmenü → Mit FTP-Server verbinden → Netzwerkeinstellungen → Profil erstellen**:
   - Wähle für Wi‑Fi den Hotspot deines Smartphones.
   - Wähle als Servertyp `FTP`, gib Adresse, Port, Benutzername und Passwort von oben ein und aktiviere den Passivmodus.
4. Aktiviere diese FTP-Verbindung an der Kamera. Sobald die FTP-Kachel in AeroCam „Verbunden“ anzeigt, ist die Einrichtung abgeschlossen.
5. Schalte im FTP-Menü der Kamera **Automatisch senden** (Auto send / Versand nach Aufnahme) ein, damit jedes neue Foto automatisch übertragen wird.

Unsicher bei einem Schritt? Tippe neben der FTP-Kachel auf **ⓘ** für eine bebilderte Anleitung.

📷 Screenshot: Ausgeklappte FTP-Einstellungskarte

## Im Betrieb
- Statusanzeige: Aus, Aktiv · Warte auf Kamera, Verbunden, Empfängt oder Fehler.
- Die Benachrichtigung zeigt „FTP-Empfang · N empfangen“ samt aktuellem Dateinamen und Übertragungsrate.
- Fotos werden nach deinen Regeln unter **Einstellungen → Empfang & Benachrichtigungen** gespeichert (Ordner, Dateiname, Nur JPEG, Bei RAW nur JPEG speichern usw.) und mit der Quelle `FTP` protokolliert.
- Bricht die Verbindung ab oder schaltet sich die Kamera mitten in einer Datei aus, werden unvollständige Dateien automatisch gelöscht, damit keine defekten Bilder in der Galerie landen.
- Nach dem Ausschalten der Kamera wechselt der Status innerhalb von ca. 1 Minute auf getrennt; beim Wiedereinschalten verbindet sich die Kamera automatisch neu.
- **Leerlauf-Autostopp**: **Einstellungen → Empfang & Benachrichtigungen → „FTP-Leerlauf-Autostopp“** (Nie, 5, 10 oder 30 Minuten). Zählt ab dem letzten empfangenen Foto, stoppt nie während einer Übertragung und benachrichtigt dich beim Beenden.

## Wichtige Hinweise
- **Lass den Hotspot eingeschaltet.** Manche Smartphones schalten ihren Hotspot automatisch ab, wenn kein verbundenes Gerät Internetdaten nutzt – deaktiviere „Hotspot automatisch ausschalten“ in den Hotspot-Einstellungen deines Smartphones.
- Durch Aus- und Wiedereinschalten des Hotspots kann sich die IP-Adresse des Smartphones ändern; passe sie bei Bedarf an der Kamera an.
- FTP-Empfang und **Wi‑Fi-Auto-Empfang können nicht gleichzeitig laufen** – startest du einen, wird der andere automatisch beendet.
- Solange FTP aktiv ist, befindet sich die Kamera im FTP-Modus, sodass **Kamera-Ordner und Fernaufnahme nicht per Wi‑Fi verbinden können**. Nutze stattdessen ein USB-Kabel oder stoppe den FTP-Empfang und stelle die Kamera wieder auf „Mit PC verbinden“.
- Der FTP-Server läuft ausschließlich im lokalen Hotspot- oder Wi‑Fi-Netzwerk und ist niemals aus dem öffentlichen Internet erreichbar.
- One-Tap-Verbindung lässt sich nicht mit FTP kombinieren (One-Tap-Verbindung startet das eigene Wi‑Fi der Kamera, während FTP erfordert, dass die Kamera deinem Smartphone-Netzwerk beitritt).

## Direkt an ein NAS senden
Du kannst in den FTP-Einstellungen deiner Kamera auch direkt ein Heim-NAS eintragen, ohne den Umweg über das Smartphone zu gehen. Das ist eine eingebaute Kamerafunktion und benötigt AeroCam nicht.
