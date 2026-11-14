<!-- translated from zh-TW at commit 968641f -->

# 10. Datenschutz und anonyme Statistiken

AeroCam hat keine Benutzerkonten. Deine Fotos werden direkt zwischen deiner Kamera und deinem Smartphone übertragen und **niemals auf irgendeinen Server hochgeladen**. Nur die unten aufgeführten wenigen Daten verlassen jemals dein Smartphone.

## Wann die App eine Internetverbindung aufbaut
| Funktion | Was gesendet wird | Abschaltbar? |
|---|---|---|
| Nach Updates suchen (Beta) | Fragt nur bei GitHub die neueste Versionsnummer ab | Läuft automatisch einmal täglich |
| Anonyme Nutzungsstatistiken | Siehe unten | Ja, unter Einstellungen → Support |
| QR-Code-Freigabe | Läuft nur in deinem lokalen Netzwerk (gleiches Wi‑Fi oder Smartphone-Hotspot), damit Personen nach dem Scannen deine ausgewählten Fotos sehen können | Endet, wenn du auf Stopp tippst oder der Timer abläuft |

## Anonyme Nutzungsstatistiken
Helfen uns zu verstehen, wie viele Personen AeroCam ungefähr nutzen, welche Kameras und Funktionen verwendet werden und wo Probleme auftreten, damit wir wissen, was wir als Nächstes entwickeln sollten. **Werden niemals verkauft und niemals für Werbung verwendet.**

- **Schalter**: **Einstellungen → Support → „Anonyme Nutzungsstatistiken senden“**, standardmäßig an.
- Wird nach der ersten Verbindung mit einer Kamera einmalig erklärt, wobei du „OK“ oder „Ausschalten“ wählen kannst. **Vor deiner Antwort wird nichts gesendet.**
- **Nach dem Ausschalten**: Das Senden stoppt sofort, und sowohl die unten genannte Zufalls-ID als auch noch nicht gesendete Daten werden gelöscht. Beim erneuten Einschalten wird eine neue ID erzeugt.
- Ohne Internetverbindung (z. B. während der Verbindung mit dem eigenen Wi‑Fi der Kamera) werden Ereignisse auf dem Smartphone zwischengespeichert und später gesendet, sobald wieder Internet verfügbar ist.
- Dev-Builds erfassen und senden keinerlei Statistiken.

### Gesendete Daten
- **Von der App erzeugte Zufalls-ID**: Stammt nicht von deinem Smartphone oder deiner Kamera; wird bei Neuinstallation der App oder Ausschalten der Statistiken zurückgesetzt.
- Kameramodell (zum Beispiel Nikon Z f) – nur der Modellname.
- Verbindungsart (Bluetooth, Wi‑Fi, USB, FTP) und Wi‑Fi-Typ (eigenes Kamera-Wi‑Fi, Smartphone-Hotspot, Router).
- Welche Funktionen pro Tag genutzt wurden (nur Funktionsnamen, einmal täglich), einschließlich angetippter gesperrter Funktionen.
- Anzahl erfolgreicher oder fehlgeschlagener Verbindungen; bei Fehlern wird nur ein Kategoriecode (wie „Zeitüberschreitung“) gesendet, niemals Fehlermeldungen.
- Schritte beim Kamera-Hinzufügen: gestartet, erfolgreich, Kamera nicht gefunden und Fehlerursache.
- Anzahl der pro Tag empfangenen Fotos (Zähler für JPEG, RAW und Video – nur Stückzahlen).
- Ob Berechtigungen erteilt oder verweigert wurden.
- Aktuelle Stufe (Kostenlos, Beta-Schlüssel…), App-Version, App-Sprache und Android-Hauptversion.
- Land: Wird aus der Verbindung ermittelt; gespeichert wird nur der Ländercode.

### Niemals gesendet
Kamera-Seriennummer, in der Kamera eingetragener Eigentümer- oder Copyright-Name, Standort (GPS), Fotos und Videos, Dateinamen, Aufnahmedaten (EXIF), Wi‑Fi-Namen und -Passwörter, Geräte-IDs (IMEI, Android-ID, Werbe-ID), Name, E-Mail, Konto oder Wortlaut von Fehlermeldungen.

### Speicherdauer
- Tagesdetails pro Gerät werden 90 Tage lang aufbewahrt; danach bleiben nur tägliche Gesamtsummen erhalten.
- Zufalls-IDs, die rund 13 Monate inaktiv waren, werden gelöscht.
- Der Server sieht bei der Verarbeitung einer Anfrage technisch bedingt deine IP-Adresse; sie wird nur zur Ländererkennung und zum Schutz vor Missbrauch verwendet und **niemals in den Statistikdaten gespeichert**.

## Standortinformationen
- **Standort an Kamera senden (Bluetooth)**: Dein Smartphone sendet seinen Standort an die Kamera, damit diese ihn in Fotos schreibt.
- **Standort zu empfangenen JPEGs hinzufügen (Smartphone)**: Standardmäßig aus. Wenn aktiviert, bleiben während einer Empfangssitzung aufgezeichnete Standortpunkte nur auf diesem Smartphone und werden nach 24 Stunden gelöscht.
- Beide Schalter befinden sich unter **Einstellungen → Empfang & Benachrichtigungen → Foto-Standort** – siehe [Kapitel 3](03-receive.md#foto-standort-gps).
- In einem Foto gespeicherte Standortdaten bleiben beim Teilen der Originaldatei erhalten. **Bei der QR-Code-Freigabe wird der Standort standardmäßig entfernt.**

## Verwendung von Berechtigungen
| Berechtigung | Zweck |
|---|---|
| Bluetooth, Geräte in der Nähe | Koppeln mit der Kamera, Bluetooth-Fotoübertragung, Bluetooth-Fernauslöser, Finden von Wi‑Fi-Kameras |
| Standort | Standort an die Kamera senden oder in Fotos ergänzen; wird von Android auch zum Auslesen von Wi‑Fi-Namen benötigt |
| Benachrichtigungen | Empfangsfortschritt, empfangene Fotos, Übertragungsprobleme, Warnung bei niedrigem Kamera-Akku |
| Fotos und Videos | Fotos in Smartphone-Fotos anzeigen und verwalten |

## Diagnoseinfos
**Einstellungen → Support → „Diagnoseinfos kopieren“** kopiert lediglich Text in deine Zwischenablage – **du entscheidest**, ob du ihn uns schickst. Enthalten sind App-Version, Smartphone- und Netzwerkstatus, Kamerafunktionen sowie aktuelle Verbindungsprotokolle; von der Kamera-Seriennummer sind nur die letzten 4 Stellen enthalten. Prüfe den Text vor dem Einfügen in ein öffentliches GitHub-Issue darauf, dass nichts enthalten ist, was du privat halten möchtest.
