<!-- translated from zh-TW at commit 968641f -->

# 7. Einstellungen im Detail

Die **Einstellungen** sind in fünf Kategorien unterteilt. Optionen, die in der kostenlosen Version nicht verfügbar sind, werden ausgeblendet. Hast du einen Vorschlag oder findest du, ein Standardwert sollte geändert werden? Schreib uns über [Problem melden](12-report.md).

## Empfang & Benachrichtigungen

### Empfang
| Einstellung | Optionen | Standard | Details |
|---|---|---|---|
| Empfangene Dateitypen | Alle Dateien / Nur JPG / JPG + RAW / Fotos + Videos / Benutzerdefiniert; außerdem Bei RAW nur JPEG speichern, Komprimiertes JPEG speichern, Komprimierte Kopie ersetzen, wenn Original eintrifft (Pro) | Alle Dateien | Siehe [Kapitel 3](03-receive.md#empfangene-dateitypen) |
| Speicherordner | Nach Kamera / Nach Datum / Nach Kamera und Datum / Nach Dateityp | Nach Kamera und Datum | Unterordnerstruktur unter `Pictures/AeroCam` und `Movies/AeroCam` |
| Dateiname | Original-Kameraname / Datumspräfix / Datums- & Zeitpräfix | Original-Kameraname | Gilt nur für künftige Dateien; die Duplikaterkennung nutzt weiterhin den Original-Kameranamen |
| Empfangsmodus (Pro) | Kontinuierlich / Einzeldatei | Kontinuierlich | Einzeldatei stoppt nach Empfang einer Datei |
| Große Videos nicht automatisch empfangen (Pro) | Größe in MB | 1024 MB | Größere Videos werden als „Gefiltert“ protokolliert und können manuell geladen werden |
| Wi‑Fi-Such-Timeout | 30 Sek. / 1 / 2 / 3 / 5 / 10 Min. / Unbegrenzt | 3 Min. | Stoppt den Auto-Empfang nach Ablauf, um nicht dauerhaft Akku zu verbrauchen |
| FTP-Leerlauf-Autostopp | Nie / 5 / 10 / 30 Min. | Nie | Zählt ab dem letzten empfangenen Foto; stoppt nie während einer laufenden Übertragung |
| Bereits per Bluetooth empfangene Fotos | Bei Wi‑Fi-Empfang durch Original ersetzen / Nicht erneut über Wi‑Fi herunterladen / Beide Versionen behalten | Durch Original ersetzen | Bluetooth empfängt eine ca. 2 MB große verkleinerte Kopie |

### Foto-Standort
| Einstellung | Standard | Details |
|---|---|---|
| Standort an Kamera senden (Bluetooth) | Ein | Sendet beim Einschalten oder bei Bluetooth-Übertragung das Smartphone-GPS an die Kamera zum Einbetten |
| Standort zu empfangenen JPEGs hinzufügen (Smartphone) | Aus (fragt beim ersten Empfang) | Schreibt den Smartphone-Standort anhand der Aufnahmezeit in per Wi‑Fi, USB oder FTP empfangene JPEGs; RAWs bleiben unverändert |

Details unter [Kapitel 3 Foto-Standort](03-receive.md#foto-standort-gps).

### Galerie
| Einstellung | Optionen | Standard | Details |
|---|---|---|---|
| Qualität komprimierter JPEGs (Pro) | 60 / 70 / 80 / 90 % | 80 % | Qualität für auf dem Smartphone neu komprimierte JPEGs (ca. 3–4 MB bei 24 MP) |
| Auswahl nach Download/Löschen | Jedes Mal fragen / Immer behalten / Immer aufheben | Jedes Mal fragen | Verhindert versehentliches Tippen auf „Von Kamera löschen“ |
| Abfrage-Countdown | 3 / 5 / 8 / 10 Sek. | 5 Sek. | Hebt die Auswahl automatisch auf, wenn bei „Jedes Mal fragen“ keine Antwort erfolgt |
| QR-Code-Freigabe automatisch beenden | 15 / 30 / 60 Min. | 30 Min. | Der Link läuft nach dieser Zeit automatisch ab |

### Benachrichtigungen
| Einstellung | Standard | Details |
|---|---|---|
| Nicht stören | Aus | Schaltet alle AeroCam-Benachrichtigungen stumm (die laufende „Empfang“-Benachrichtigung bleibt systembedingt erhalten) |
| Bei Übertragungsbeginn | Aus | |
| Bei Fotoempfang | Ein | |
| Übertragungsprobleme | Ein | Hängende Übertragung, Abbruch durch Kamera oder wenig Speicherplatz auf dem Smartphone |
| Dauerbenachrichtigung ausblenden | — | Öffnet die Android-Benachrichtigungseinstellungen, damit du sie ausblenden kannst, während der Empfang weiterläuft |
| Warnung bei niedrigem Kamera-Akku | Ein, 15 % | Schwellenwerte: 10 / 15 / 20 / 30 %; wird bei aktiver Kameraverbindung geprüft |

## Aufnahme

### Speicherziel
| Einstellung | Optionen | Details |
|---|---|---|
| Speicherziel | Speicherkarte / Karte + Smartphone (Pro) | Wird verwendet, wenn eine Karte eingelegt ist; ohne Karte wechselt die App automatisch zu Nur Smartphone (Pro). Zeigt bei Verbindung den aktuellen Kartenstatus an. Siehe [Kapitel 3](03-receive.md#speicherziel-und-aufnehmen-ohne-speicherkarte) |

### Fernaufnahme
| Einstellung | Optionen | Standard | Details |
|---|---|---|---|
| Beim Start der Fernaufnahme standardmäßig aktiv | Vor Aufnahme fokussieren, Histogramm, Überbelichtungswarnung, Fokus-Peaking, Belichtungsskala | Vor Aufnahme fokussieren, Belichtungsskala | Kann während der Aufnahme jederzeit umgeschaltet werden |
| Farbe der Belichtungsskala | Automatisch / Weiß / Schwarz | Automatisch | Automatisch passt sich der Hintergrundhelligkeit an |
| Fokus-Peaking-Farbe | Rot / Gelb / Blau / Weiß | Rot | Bei roten Motiven auf eine andere Farbe wechseln |
| Bildschirm während Fernaufnahme eingeschaltet lassen | Ein / Aus | Ein | Verhindert das Ausschalten des Displays bei Intervall- oder Langzeitbelichtungen |
| Linkshänder-Modus | Ein / Aus | Aus | Verschiebt den Auslöser im Querformat nach unten links |

### Kabelverbindung (USB‑C)
| Einstellung | Optionen | Standard | Details |
|---|---|---|---|
| USB-Live-View-Bildrate | 30 / 60 fps / Unbegrenzt | 30 fps | 30 fps spart Akku und bleibt kühler; 60 fps ist flüssiger |
| Hochauflösende USB-Vorschau | Ein / Aus | Ein | Schärfere Vorschau bei leicht geringerer Bildrate; fällt automatisch zurück, falls nicht unterstützt |
| Beim Anschließen eines USB-Kabels Empfang automatisch starten (Pro) | Ein / Aus | Ein | Startet den USB-Empfang automatisch beim Einstecken |
| Kamerauhr beim Verbinden synchronisieren | Ein / Aus | Ein | Korrigiert nur bei > 2 Sek. Abweichung; fragt vorher bei > 1 Tag Abweichung |
| Kamera über USB wachhalten | Ein / Aus | Ein | Sendet alle 10 Sek. ein kleines Signal; stoppt nach 30 Min. Leerlauf oder bei niedrigem Akku |

## Darstellung und Sprache
| Einstellung | Optionen | Standard |
|---|---|---|
| Design | Systemstandard / Hell / Dunkel / Sternenhimmel (Rotlicht) | Systemstandard |
| Minimale App-Bildschirmhelligkeit | Ein / Aus (im Sternenhimmel-Modus) | Aus |
| Sprache | Systemstandard / 繁中 / 简中 / 日本語 / English / 한국어 / Deutsch / Français / Español / Tiếng Việt / ไทย / Bahasa Indonesia | Systemstandard |

## Speicher & Akku
| Punkt | Details |
|---|---|
| Vorschaubild-Cache | Zeigt die Cache-Größe samt Lösch-Button an (wird bei Bedarf neu von der Kamera geladen) |
| Temporäre Dateien unvollständiger Downloads | Zeigt die Größe samt Lösch-Button an |
| Smartphone-Fotos neu scannen | Findet Fotos wieder, die auf das Smartphone zurückgekehrt sind (z. B. aus dem Papierkorb oder vor einer Neuinstallation gespeichert) |
| Akku-Optimierung | Empfohlen auszuschalten (zeigt „Nicht optimiert ✓“), damit Hintergrundübertragungen nicht beendet werden |

## Support
| Punkt | Details |
|---|---|
| Diagnoseinfos kopieren | Beim Melden eines Problems einfügen: App-Version, Smartphone- & Netzwerkstatus, Kamerafunktionen, letztes Befehlsprotokoll und letzter Absturzbericht. Von der Kamera-Seriennummer sind nur die letzten 4 Stellen enthalten |
| Logs löschen | Löscht aktuelle und vorherige Sitzungsprotokolle sowie Absturzberichte |
| Nach Updates suchen | Prüft manuell auf eine neue Version; zeigt darunter die aktuelle Version an |
| Testschlüssel | „Kostenlosen Schlüssel holen“ öffnet AeroCam-Releases; „Testschlüssel eingeben“ zum Einfügen; zeigt aktuelle Stufe und Ablaufdatum |
| Open-Source-Lizenzen | Verwendete Drittanbieter-Bibliotheken (wie LibRaw für die RAW-Entwicklung) |
| Anonyme Nutzungsstatistiken senden | Ein einzelner Schalter, standardmäßig an. Siehe [Datenschutz und anonyme Statistiken](10-privacy.md) |
