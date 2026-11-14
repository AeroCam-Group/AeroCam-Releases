<!-- translated from zh-TW at commit 968641f -->

# 5. Fernaufnahme und Fernsteuerung

| Methode | Verbindung | Live-Bild | Stufe |
|---|---|---|---|
| [Fernaufnahme](#fernaufnahme-pro) | Wi‑Fi oder USB | ✅ | Pro |
| [Bluetooth-Fernauslöser](#bluetooth-fernauslöser-kostenlos) | Bluetooth | ❌ | Kostenlos (Intervallaufnahme ist Pro) |
| [Video-Monitor](#video-monitor-cine) | USB (Wi‑Fi experimentell) | ✅ Speziell für Video | Cine |

---

## Fernaufnahme (Pro)
Sieh das Live-Bild deiner Kamera auf dem Smartphone, tippe zum Fokussieren, ändere Belichtungseinstellungen und nimm Fotos oder Videos auf. Funktioniert **sowohl über Wi‑Fi als auch über USB** – steckst du ein USB-Kabel an, wechselt die App automatisch auf USB.

**Voraussetzungen**
1. Ein Kameramodell mit „Verbindungstyp“ im Menü – siehe [Unterstützte Kameras](README.md#unterstützte-kameras).
2. Bei Wi‑Fi-Verbindung muss der Verbindungstyp der Kamera auf **Kamerasteuerung** stehen – siehe [Kamera verbinden](02-connect.md#verbindungstyp-connection-type-an-der-kamera). Steht er noch auf „Bildübertragung“, zeigt AeroCam die Schritte zum Umschalten an und verbindet sich danach automatisch neu.

Die Fernaufnahme läuft im Vollbildmodus ohne untere Navigationsleiste. Tippe oben links auf **←** oder drücke die Zurück-Taste deines Smartphones, um zum Startbildschirm zurückzukehren.

📷 Screenshot: Fernaufnahme-Bildschirm (Hoch- und Querformat)

### Bildschirmaufbau
| Bereich | Inhalt |
|---|---|
| Oben | Kameraeinstellungen: Modus, Belichtungszeit, Blende, ISO, ISO-Automatik, Belichtungskorrektur, Weißabgleich, Fokusmodus, AF-Messfeldsteuerung, Belichtungsmessung, Picture Control, Bildqualität. Im Hochformat zweizeilig, im Querformat einzeilig (horizontal scrollbar) |
| Dritte Zeile oben | Zurück, Videoaufnahme, Saubere Ansicht, Bildschirmsperre, Speicherziel, Akku |
| Mitte | Unbeschnittenes Live-Bild mit Fokusfeld, Wasserwaage, Belichtungsskala und Hilfslinien |
| Unten | 6 anpassbare Schnellschalter + „Mehr“ |
| Ganz unten | „Aufnahme“ (Aufnahmemethode wählen), Auslöser, AF-Taste, Vorschaubild des letzten Fotos und verbleibende Aufnahmen |

Im Querformat wandern die Schnellschalter in den linken schwarzen Rand, der Auslöser sitzt unten rechts. Der **Linkshänder-Modus** (**Einstellungen → Aufnahme**) verschiebt den Auslöser nach unten links.

### Kameraeinstellungen ändern
Tippe oben auf einen Wert, um unten eine Einstellleiste zu öffnen, die das Live-Bild nicht verdeckt.
- Der Belichtungsmodus ist schreibgeschützt (P / S / A / M bitte direkt an der Kamera wählen). Belichtungszeit ist in S und M verstellbar, Blende in A und M.
- Bei aktiver ISO-Automatik steht bei ISO `AUTO`. Neben der Belichtungskorrektur setzt `0` den Wert sofort zurück.
- Wählst du beim Weißabgleich `K`, kannst du die Farbtemperatur direkt einstellen. Picture Control zeigt den aktiven Namen auf der Kamera an, einschließlich eigener Profile.
- Lässt sich ein Wert **nicht ändern**, erklärt die App den Grund. Bei Kameras mit physischen Einstellrädern wie der Zf und Zfc stelle das Zeitenrad auf **1/3 STEP** und das ISO-Rad auf **C**.

### Fokus und Auslöser
- **Tippen zum Fokussieren**: Tippe auf eine beliebige Stelle im Live-Bild, um dorthin zu fokussieren. Wähle an der Kamera eine AF-Messfeldsteuerung mit beweglichem Fokusfeld (z. B. Einzelfeld-AF); bei automatischer Messfeldsteuerung entscheidet die Kamera.
- Das tatsächliche Fokusfeld der Kamera wird eingezeichnet (Einzelfeld, Dynamisch, Automatisch und Motivverfolgung werden angezeigt) – grün bei scharfem Fokus, rot bei Fehlschlag.
- **Auslöser**: Einmal tippen löst aus; **gedrückt halten = halb drücken zum Fokussieren** (Rahmen wird grün), Loslassen nimmt das Foto auf.
- **AF-Taste**: Fokussiert am aktuellen Fokuspunkt neu.
- **Vor Aufnahme fokussieren** (standardmäßig an): Ausschalten, um ohne Warten auf den AF sofort auszulösen (schneller bei manuellem Fokus oder bereits eingestellter Schärfe).
- **Tippen zum Aufnehmen**: Ist dies aktiv, fokussiert ein Tipp ins Live-Bild auf diese Stelle und löst sofort aus.
- Tipp-Gesten ganz am linken oder rechten Bildschirmrand (Android-Zurück-Geste) lösen keinen Fokus aus, damit beim Zurückwischen nichts verstellt wird.

### Untere Schnellschalter (anpassbar)
Standardmäßig belegt mit Peaking, Zebra, Wasserwaage, Raster, Zoom und einem freien Platz; ganz rechts steht fest „Mehr“.
- **Antippen** schaltet ein oder aus; **0,5 Sekunden gedrückt halten** öffnet Detailoptionen (Peaking-Empfindlichkeit, Zebra-Schwellenwert, Rasterart, Zoomstufe).
- **Anpassen**: Tippe oben rechts in „Mehr“ auf das Zahnradsymbol. Verfügbar sind: Peaking, Zebra, Wasserwaage, Raster, Zoom, Histogramm, Belichtungsskala, Tippen zum Aufnehmen, Vor Aufnahme fokussieren, Auf Smartphone kopieren, Screenshot, Sternenhimmel-Modus, Live-Vorschau und Selbstauslöser.

### „Mehr“-Menü
„Mehr“ öffnet eine halbtransparente Schublade (im Hochformat von unten, im Querformat von der Seite), sodass das Live-Bild sichtbar bleibt. Aufgeteilt in drei Tabs:
- **Hilfen**: Live-Vorschau, Peaking, Überbelichtungswarnung (Zebra), Wasserwaage, Hilfslinien, Histogramm, Belichtungsskala, Fokuslupe, Sternenhimmel-Modus.
- **Aufnahme**: Vor Aufnahme fokussieren, Tippen zum Aufnehmen, AF-Messfeldsteuerung, Jedes Bild aufs Smartphone kopieren, Vorschau-Screenshot.
- **Werkzeuge**: Geisterbild-Überlagerung, Mehrfachaufnahme-Checkliste, Tipps.

### Aufnahmehilfen (nur auf dem Smartphone sichtbar, nicht im Foto gespeichert)
| Hilfe | Beschreibung |
|---|---|
| Wasserwaage | Liest den Neigungssensor der Kamera aus; wird bei unter 0,5° Abweichung grün und zeigt Roll- sowie Neigungswinkel an |
| Histogramm | Antippen wechselt zwischen „Luminanz + RGB-Überlagerung“ und „RGB getrennt“ |
| Zebra (Überbelichtung) | Markiert Bereiche über dem Helligkeitsschwellenwert mit diagonalen Streifen: 85 / 90 / 95 / 100 % (Standard 95 %) |
| Fokus-Peaking | Hebt scharfe Kanten farbig hervor (Rot, Gelb, Blau, Weiß) mit Empfindlichkeit Niedrig / Mittel / Hoch als Hilfe beim manuellen Fokussieren |
| Belichtungsskala | Vertikale Belichtungsanzeige im Nikon-Sucherstil in 1/3-EV-Schritten. Zeigt im M-Modus die Abweichung von der Messung, in P / A / S die Korrektur |
| Hilfslinien | Drittel-Regel, 4×4-Raster, Goldener Schnitt, Goldene Spirale, Diagonalen, Mittenkreuz |
| Zoom | Wird es von der Kamera unterstützt (z. B. Zf), **zoomt die Kamera selbst hinein**, sodass du echte Sensorpixel bei 50 % / 100 % / 200 % / 400 % siehst. Tippe oder nutze ◀ ▲ ▼ ▶ zum Verschieben und `Nah ◀◀ ◀ ▶ ▶▶ Fern` unten für feine manuelle Fokusschritte. Andere Modelle nutzen den digitalen App-Zoom (2× / 4× / 8×) |

> Aufnahmehilfen werden aus dem komprimierten Live-View-Stream berechnet und dienen nur als Orientierung – verlasse dich für kritische Belichtungen immer auf das Histogramm des aufgenommenen Fotos.

### Aufnahmemethoden
Tippe neben dem Auslöser auf **Aufnahme**, um einen Modus zu wählen. Der Button wird gelb und über dem Auslöser erscheint eine Statusleiste (z. B. `Intervallaufnahme · Alle 5 Sek. · 10 Bilder`). Tippe darauf, um Einstellungen anzupassen und **Start** zu drücken, oder auf **×**, um zur normalen Aufnahme zurückzukehren. Während des Ablaufs steht oben der Fortschritt samt **Stopp**-Button zum jederzeitigen Abbrechen.

| Methode | Einstellungen | Beschreibung |
|---|---|---|
| Einzelbild / Normal | 1–9 Aufnahmen | In Kombination mit dem Selbstauslöser wird nach dem Countdown eine Serie von N Bildern (ca. 1 Sek. Abstand) ausgelöst |
| **Selbstauslöser** | Aus, 2, 5, 10 Sek. | Ganz oben im Menü „Aufnahme“; funktioniert mit jeder Aufnahmemethode und bei Videoaufnahmen. Zeigt einen großen Countdown in der Bildmitte; erneutes Tippen auf den Auslöser bricht ab |
| Langzeitbelichtung (Bulb) | 1–3600 Sek. | Kamera muss im M-Modus stehen und die Belichtungszeit auf Bulb oder Time gestellt sein; beendet sich nach Ablauf automatisch |
| Intervallaufnahme (Interval timer shooting) | 2–999 Bilder, 1–3600 Sek. Intervall | Nimmt automatisch in festen Abständen auf und zeigt die Gesamtdauer an; ideal zusammen mit „Jedes Bild aufs Smartphone kopieren“ zur Zeitraffer-Kontrolle |
| Belichtungsreihe | 3 / 5 / 7 / 9 Bilder, 0,3–3,0 EV Schrittweite | Stuft die Belichtung um den aktuellen Wert ab und stellt danach den Ausgangswert wieder her |
| Fokusverlagerung (Focus shift shooting) | 2–300 Bilder, Schrittweite | Fokussiert zuerst auf den nächsten Punkt und verlagert den Fokus zwischen den Aufnahmen Richtung Unendlich. Erfordert ein AF-Objektiv; das Focus-Stacking erfolgt anschließend am Computer |
| Panorama | Rastergröße oder „Frei“ | Mehrere überlappende Aufnahmen machen und zu einem Panorama zusammenfügen – siehe unten |
| Shake (Rauschreduzierung) | 4 oder 8 Bilder | Kurze Serie aus der Hand aufnehmen und zu einem rauschärmeren Bild verrechnen – siehe unten |

> Während eines Mehrfachaufnahme-Werkzeugs sind AF und Tippen zum Fokussieren pausiert. Beim Verlassen der Fernaufnahme fragt die App vorher nach.

#### Panorama (Stitching)
- **Raster**: Wähle eine Rastergröße, und AeroCam berechnet die exakten Schwenk-/Neigewinkel pro Kachel, während du die Kamera drehst und auslöst. Eine Anzeige meldet, ob die Überlappung reicht („Bereit / Kann noch weiter drehen / Eventuell zu wenig Überlappung“) und blendet den Rand des vorigen Bildes halbtransparent zum Ausrichten ein.
- **Frei**: Kein festes Raster – überlappe jedes Bild einfach um ca. 30 % in beliebiger Richtung (bis zu 30 Aufnahmen).
- Ab 2 Aufnahmen kannst du auf **Zusammenfügen** tippen, um das Panorama direkt auf dem Smartphone zu berechnen; eine volle 360°-Drehung erzeugt ein 360°-Panorama. Die gespeicherten Wasserwaagendaten der Kamera sorgen für einen geraden Horizont.
- Die Einzelbilder werden in Smartphone-Fotos als Stapel gruppiert, sodass du sie später erneut zusammenfügen kannst – siehe [Kapitel 6](06-edit.md#bildverarbeitung-panorama-stitching-und-rauschreduzierung-pro).

#### Shake (Rauschreduzierung)
- Ermöglicht Kameras ohne Pixel-Shift eine Qualitätssteigerung durch Mehrfachbelichtung: Nimm 4 oder 8 Bilder aus der Hand (oder vom Stativ) auf – AeroCam richtet sie exakt aus und mittelt sie, wodurch das Rauschen (bei 8 Bildern) auf etwa ein Drittel sinkt, ohne Details zu verlieren.
- Die Verrechnung läuft automatisch im Hintergrund („Verrechne %“) und speichert das Ergebnis als `SHAKE_<Zeitstempel>.JPG` in voller Auflösung mit EXIF-Daten.
- Bewegte Motive (Autos, Personen, Blätter) werden aus dem schärfsten Einzelbild übernommen, um Geisterbilder zu vermeiden; stark verwackelte Aufnahmen werden automatisch aussortiert.
- Ideal für Nachtszenen, dunkle Innenräume und hohe ISO-Werte.

### Geisterbild-Überlagerung (Pro)
**Mehr → Werkzeuge → Geisterbild-Überlagerung**: Legt ein Referenzbild als **halbtransparente Überlagerung** oder **geteilte Bildschirmansicht** über das Live-Bild, inklusive Deckkraftregler und „Aktuelles Bild aufnehmen“. Perfekt für exakte Wiederholungsaufnahmen, Repros und Ausrichtungen.

### Weitere Funktionen
- **Jedes Bild aufs Smartphone kopieren**: Speichert jede Aufnahme nach deinen Empfangsregeln, einschließlich „Bei RAW nur JPEG speichern“.
- **Letztes Foto**: Das Vorschaubild unten rechts zeigt deine letzte Aufnahme samt Belichtungszeit, Blende und ISO. Tippe darauf, um alle Bilder der aktuellen Session anzusehen und Originale oder JPEGs aufs Smartphone zu speichern.
- **Saubere Ansicht**: Blendet alle Bedienelemente außer dem Live-Bild aus; tippe auf den blassen Eck-Button zum Wiederherstellen. **Sperre**: Verhindert versehentliches Tippen; zum Entsperren beliebig lange auf den Bildschirm drücken.
- **Videoaufnahme**: Tippe oben auf den Aufnahme-Button. Schaltet die Kamera vor dem Start in den Anwendungsmodus (auf der Zf erforderlich) und danach wieder zurück; falls keine Aufnahme möglich ist, wird der Grund angezeigt. Per USB empfiehlt sich der [Video-Monitor](#video-monitor-cine).
- **Vorschau-Screenshot**: Speichert das Live-View-Bild unter `Pictures/AeroCam/Snapshots/` (Vorschauauflösung).
- **USB-Fernaufnahme**: Flüssigeres Live-Bild als per Wi‑Fi (Standard 30 fps; einstellbar auf 60 fps oder unbegrenzt) mit optionaler hochauflösender Vorschau und Live-fps-Anzeige unten rechts. Einstellbar unter **Einstellungen → Aufnahme**.
- Während der Fernaufnahme bleibt der Bildschirm standardmäßig eingeschaltet.

---

## Bluetooth-Fernauslöser (kostenlos)
Kein Wi‑Fi und kein Live-Bild nötig. Start → Bluetooth-Kachel → **Bluetooth-Fernauslöser**. Erfordert zuerst eine [Bluetooth-Kopplung](02-connect.md#koppeln).
- Auslöser antippen für ein Einzelbild; Auslöser gedrückt halten für die Serienaufnahme der Kamera (CL / CH).
- AF halten und Auslöser antippen für schnelle Einzelbilder, oder die Tasten für 3er- / 5er-Serien nutzen.
- AF-Taste: Gedrückt halten zum Fokussieren. An der Kamera muss der Autofokus per halb gedrücktem Auslöser erlaubt sein (falls du Back-Button-AF über AF‑ON nutzt, prüfe die Individualfunktionen der Kamera).
- Bietet Selbstauslöser-Countdown, Video-Start/Stopp und Anzeige der verbleibenden Aufnahmen.
- **Intervallaufnahme** ist eine Pro-Funktion.

📷 Screenshot: Bluetooth-Fernauslöser-Bildschirm

---

## Video-Monitor (Cine)
Macht dein Smartphone zu einem vollwertigen Video-Kontrollmonitor. Stecke USB an und tippe auf dem Startbildschirm auf **🎥 Video-Monitor** (am flüssigsten, bis ca. 60 fps); eine Wi‑Fi-Variante steht unter der Wi‑Fi-Kachel als experimentelle Funktion bereit.
- Stelle an der Zf den Foto-/Video-Wählschalter auf **Video**.
- **Obere Leiste**: `● REC`-Timer, Videoauflösung/-bildrate (z. B. `1080 60p` – zum Ändern antippen), Dateiformat (z. B. `H.265 10bit` – für N‑Log erforderlich), verbleibende Aufnahmezeit und Akku.
- **Untere Leiste**: Video-Belichtungszeit, Blende, ISO, ISO-Automatik, Belichtungskorrektur, Weißabgleich, Fokusmodus und Belichtungsmessung (Video-ISO ist im M-Modus aktiv).
- **Aufnahme-Button**: Während der Aufnahme **1 Sekunde gedrückt halten** (bis der rote Ring voll ist), um zu stoppen – das verhindert versehentliches Abbrechen. Drückst du während der Aufnahme Zurück, fragt die App vorher nach.
- **Monitoring-Werkzeuge**: Belichtungsskala, Histogramm, Waveform / RGB-Parade, Falschfarben (False Color), Zebra (inklusive zweiter Hautton-Zebraschwelle), Fokus-Peaking, Hilfslinien, Sicherheitsrahmen (Safe Frames), Seitenverhältnis-Masken (`2.39:1`, `1.85:1`, `16:9`, `9:16`, `4:5`), roter Tally-Rahmen und Verschlusswinkel-Anzeige.
- **LUT** (ab Android 13): Wendet eine Vorschau-LUT auf das Live-Bild an (integrierte N‑Log-zu-Rec.709-LUT sowie eigener `.cube`-Import), ohne sie in die Videodatei einzubrennen. Schalte an der Kamera die **Ansichtshilfe** (View assist) aus, damit die LUT nicht doppelt angewendet wird.
- **Anamorphotisches Entzerren** (`1.33x`–`2.0x`), **A/B-Rack-Focus** (zwei Fokuspunkte festlegen und sanft dazwischen verlagern) und **Geisterbild-Überlagerung**.
- Tippen zum Fokussieren ist während der Aufnahme standardmäßig deaktiviert, um versehentliche Fokusfahrten zu vermeiden, und kann im Menü aktiviert werden.
- **Screenshots**: „Vorschau-Screenshot“ speichert das reine Live-Bild; „Screenshot (mit Hilfen)“ speichert inklusive LUT, Zebra, Falschfarben und Seitenverhältnis-Masken.

📷 Screenshot: Video-Monitor-Bildschirm

---

## Sternenhimmel-Modus (kostenlos)
Bei der Astrofotografie müssen sich deine Augen an die Dunkelheit gewöhnen – helles weißes Bildschirmlicht verengt die Pupillen. Der Sternenhimmel-Modus färbt die gesamte App dunkelrot.
1. Aktivieren über **Einstellungen → Darstellung und Sprache → Design → „Sternenhimmel (Rotlicht)“**, oder über die unteren Schnellschalter bzw. **Mehr → Hilfen** in der Fernaufnahme.
2. Noch dunkler gewünscht? Aktiviere **Minimale App-Bildschirmhelligkeit**.
3. Echte Farben prüfen? **Halte „Für Echtfarben gedrückt halten“** – beim Loslassen kehrt die rote Ansicht zurück. Verfügbar in Fernaufnahme, Video-Monitor und der Vollbild-Fotoansicht.
4. Der Sternenhimmel-Modus verändert nur die Bildschirmanzeige, niemals deine Fotos. Bei der QR-Code-Freigabe werden vorübergehend normale Farben wiederhergestellt, damit andere Smartphones den Code scannen können.
