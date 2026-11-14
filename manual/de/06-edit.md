<!-- translated from zh-TW at commit 968641f -->

# 6. Fotobearbeitung und Bildstile

## Foto-Editor (kostenlos)
Öffne ein beliebiges Foto in **Smartphone-Fotos** und tippe auf **Bearbeiten**. Unten gibt es drei Tabs: **Zuschneiden**, **Anpassen** und **.np3**.

📷 Screenshot: Foto-Editor (Zuschneiden, Anpassen, .np3)

### Zuschneiden
- Seitenverhältnisse: Original, Frei, 1:1, 4:5, 3:2, 16:9 sowie Kinoformate 1.66, 1.85, 2, 2.20 und 2.39. Hochkantfotos nutzen automatisch das Hochformat.
- Im Rahmen ziehen zum Verschieben; an einer Ecke ziehen zum Ändern der Größe.
- Begradigen ±45° und um 90° gegen den Uhrzeigersinn drehen (`↺`).

### Anpassen
Wähle ein Werkzeug aus der Leiste, stelle den Wert mit dem präzisen Skalenrad ein und tippe auf **Fertig** (bearbeitete Werkzeuge zeigen einen kleinen Punkt):
- **Licht**: Belichtung, Kontrast, Lichter, Tiefen, Weiß, Schwarz.
- **Farbe**: Farbtemperatur, Farbton, Sättigung, Dynamik.
- **Details**: Klarheit, Schärfe, Vignette.

Skalenrad: Rastet auf ganzen Schritten ein (0,1 EV bei Belichtung, 1° bei Begradigen, 1 bei allen anderen) mit feinem Vibrationsfeedback. Halte eines der Enden gedrückt für kontinuierliches Verstellen, tippe auf die Zahl zur direkten Eingabe oder tippe doppelt bzw. auf `↺`, um auf Null zurückzusetzen.

### Allgemeine Bedienung
- **↶ ↷** Rückgängig / Wiederholen.
- **Original** gedrückt halten, um das Bild vor deinen Änderungen zu sehen.
- **◧ Vergleich**: Geteilter Schieberegler zum Vergleichen von Original und Bearbeitung; Zwei-Finger-Zoom bleibt auf beiden Seiten synchron.
- Tippe unten rechts auf **Histogramm**, um das Live-Histogramm einzublenden.

### Speichern
- Kamera-Originale (noch auf der Speicherkarte): **Beim Speichern wird die Kopie auf dem Smartphone ersetzt.** AeroCam bewahrt 7 Tage lang ein Backup des Originals auf, das du in der Einzelbildansicht über „Original wiederherstellen“ zurückholen kannst. Ist die Kamera nicht verbunden, fragt die App, ob sie „Ersetzen“ oder „Als Kopie speichern“ soll.
- Reine Smartphone-Fotos (Aufnahmen ohne Karte, Panoramen, Shake-Serien) werden immer als neue Kopie mit der Endung `_E` gespeichert.
- Behält EXIF-Metadaten bei JPEG-Qualität 95 bei. Wird das Speichern unterbrochen, schließt AeroCam den Vorgang beim nächsten Öffnen der App automatisch ab.
- Filtere in Smartphone-Fotos nach **Bearbeitet**, um bearbeitete Bilder zu finden (unten links mit kleinem `✎` markiert).
- Beim Bearbeiten einer komprimierten Kopie (`JPEG.S`) weist die App darauf hin, für bessere Qualität lieber das Kamera-Original zu bearbeiten.
- Videos können nicht bearbeitet werden.

---

## RAW auf dem Smartphone bearbeiten (experimentell)
NEF-Dateien lassen sich im selben Editor bearbeiten und werden daneben als `DSC_xxxx_E.JPG` gespeichert (erneutes Speichern aktualisiert diese Datei). **Die originale NEF-Datei wird niemals verändert**, und EXIF-Daten bleiben erhalten.
- **Verlustfrei komprimiertes NEF**: Wird mit dem Weißabgleich der Kamera direkt auf dem Smartphone entwickelt.
- **High Efficiency / High Efficiency★ NEF**: Diese proprietäre Komprimierung kann auf dem Smartphone nicht dekodiert werden; stattdessen bearbeitet AeroCam das eingebettete JPEG in voller Größe aus der NEF-Datei. Oben steht dann „Eingebettetes JPEG 8 Bit“ und „Angewendeter Kamerastil: xxx“.
- Dateien, die nur ein kleines Vorschaubild und kein JPEG in voller Größe enthalten, können nicht bearbeitet werden (die App erklärt den Grund).

### Auf dem Smartphone bearbeitbares RAW (Kamera-RAW-Komprimierung umschalten)
Damit zukünftige NEF-Aufnahmen direkt auf dem Smartphone entwickelt werden können, kannst du deine Kamera direkt aus AeroCam heraus auf „Verlustfreie Komprimierung“ umstellen:
- Zugriff über „Nächstes Mal verlustfreies RAW aufnehmen“ im High-Efficiency-Banner des Editors oder durch Antippen des Bildqualitäts-Badges oben rechts auf der Speicherkarten-Karte auf dem Startbildschirm (aktiv, sobald die Kamera auf RAW eingestellt ist).
- Fragt immer vorher nach Bestätigung, schreibt die Einstellung in die Kamera, liest sie zur Kontrolle zurück und zeigt die Änderung der verbleibenden Aufnahmen an (verlustfreie Dateien sind größer, daher sinkt die Restzahl leicht).
- AeroCam merkt sich die vorherige Einstellung deiner Kamera, damit du sie später wiederherstellen kannst, und überschreibt sie nicht, wenn du sie bereits an der Kamera geändert hast.

---

## .np3-Stilvorschau (kostenlos)
Im Tab **.np3** des Editors kannst du Nikon Picture Control-Dateien (`.np3`, `.ncp`) auf Fotos anwenden und das Ergebnis vorab auf dem Smartphone ansehen.
- Tippe auf einen Stil, um ihn anzuwenden, stelle die Stärke von 0–100 % ein und nimm unter **Anpassen** weitere Feinabstimmungen vor.
- Wische auf dem Foto nach links/rechts, um Stile durchzuschalten, oder halte gedrückt für das Original. Darunter befinden sich Schnellfilter für `★` Favoriten und Zuletzt verwendet.
- Tippe auf **Alle N ▴**, um die gesamte Stilbibliothek (siehe unten) samt Suche und Filtern zu öffnen.
- Simuliert werden Tonwertkurven und Sättigung: Dateien mit eigenen Kurven nutzen ihre eingebettete Kurve, während Dateien mit Flexible-Color-Reglern („Regler-Tonwert“) anhand von NX-Studio-Messungen in Kurven umgerechnet werden. **Farbmischer und Color Grading werden noch nicht simuliert**, daher ist die Vorschau eine Annäherung.
- Funktioniert am besten mit NEF-Dateien. Wenn in ein JPEG bereits bei der Aufnahme ein Picture Control eingebacken wurde, addieren sich die Effekte (die App warnt dich).

📷 Screenshot: Tab .np3 im Editor

---

## Kamerastile C1–C9 (Pro)
Verwalte die benutzerdefinierten Picture-Control-Speicherplätze C1–C9 deiner Kamera vom Smartphone aus. Tippe auf dem Startbildschirm auf die Karte **Kamerastile** (erfordert eine Wi‑Fi- oder USB-Verbindung).
- Jeder Platz zeigt eine Vorschau, den Namen sowie Abzeichen für aktiven Status, eigene Kurve oder Flexible Color.
- **Tippe auf einen Platz**, um einen Stil aus deiner Bibliothek auszuwählen und auf die Kamera zu schreiben. AeroCam liest ihn zur Kontrolle zurück und zeigt nur bei Übereinstimmung ein `✓`. **Gedrückt halten** oder `⋮` antippen leert den Platz. Läuft gerade eine Fotoübertragung, wartet der Schreibvorgang, bis diese Datei fertig ist.
- Die Kamera wird nur abgefragt, wenn du diesen Bildschirm öffnest, auf `↻` tippst, schreibst oder löschst; der Startbildschirm zeigt die zuletzt ausgelesenen Werte samt Uhrzeit.
- Unter C1–C9 werden die 9 Rezepte der Nikon Imaging Cloud schreibgeschützt aufgelistet (diese werden über die Nikon Imaging Cloud hinzugefügt).

### Was auf die Kamera geschrieben wird
Benutzerdefinierte Kameraspeicherplätze akzeptieren ein **Basis-Picture-Control + Anpassungsregler**, keine rohe `.np3`-Datei:
- Tippe in der Bibliothek auf **＋ Neuer Stil**, um eine Basis (Standard, Ausgewogen, Creative Picture Control…) zu wählen und Scharfzeichnung, Detailkontrast, Kontrast, Helligkeit, Farbsättigung sowie Farbton festzulegen.
- **`.np3` / `.ncp` auf die Kamera schreiben (Annäherung)**: Dateien mit Kurven – sowie in Kurven umgerechnete „Regler-Tonwert“-Dateien – schreiben **Name + Kurve + Schärfung (Scharfzeichnung, Mitteltöne-Scharfzeichnung, Detailkontrast)** mit der gewählten Basis in einen C-Platz. **Sättigung, Farbmischer und Color Grading können über die Verbindung nicht übertragen werden**; AeroCam listet vor dem Schreiben alle Werte der Datei auf und markiert klar, was nicht übertragen wird.
- Für das exakte Originalergebnis kopiere die `.np3`-Datei auf eine Speicherkarte und importiere sie über das Kameramenü.

### Stilbibliothek
- Fasst bis zu 256 Stile (`.np3` und `.ncp`).
- Suchleiste `🔍`, Filterchips (Alle, `★`, Zuletzt, Mit Kurve, Auf Kamera, Schreibbar) und **＋ Neu**.
- Jeder Stil zeigt ein Vorschaubild mit deinem eigenen importierten Referenzfoto (`＋ → „Vorschau-Referenzbild…“`) oder einer Farbkarte, solange noch keines importiert wurde.

📷 Screenshot: Kamerastile C1–C9 und Stilbibliothek

---

## Bildverarbeitung: Panorama-Stitching und Rauschreduzierung (Pro)
Wähle in **Smartphone-Fotos** mehrere Bilder aus und **wische die untere Aktionsleiste nach oben** (oder tippe auf den Griff), um „Bildverarbeitung“ zu öffnen.

### Zusammenfügen (Panorama)
- Wählst du Bilder innerhalb eines „Panorama“-Stapels aus, werden sie gemäß ihren aufgenommenen Rasterpositionen zusammengefügt und als „Panorama“ wieder in diesem Stapel gespeichert.
- Wählst du beliebige überlappende Fotos in der normalen Galerie aus, erkennt AeroCam automatisch deren Anordnung und speichert das Ergebnis als neuen Stapel.
- Nicht passende Fotos lassen nicht den gesamten Durchlauf scheitern: AeroCam fügt die größte zusammenhängende Gruppe zusammen und listet übersprungene Dateinamen auf. Bei Rasterpanoramen müssen alle Kacheln vorhanden sein, damit keine Löcher entstehen.
- Eine volle 360°-Runde ergibt ein 360°-Panorama. Die Ergebnisse werden mithilfe der aufgezeichneten Wasserwaagendaten automatisch ausgerichtet, sind frei von Geisterbildern und behalten ihre EXIF-Daten.
- Die Aufnahmeanleitung findest du in [Kapitel 5 Panorama](05-remote.md#panorama-stitching).

### Rauschreduzierung (Shake)
- Richtet ausgewählte Aufnahmen aus und mittelt sie, um Rauschen zu reduzieren und Details zu bewahren; bewegte Bereiche werden aus einem Einzelbild übernommen, um Geisterbilder zu vermeiden.
- Wählst du Bilder in einem „Shake“-Stapel aus, wird das verrechnete Bild wieder in diesem Stapel gespeichert (als „Verrechnet“ markiert); alternativ kannst du über dem Stapel auf **Verrechnen** / **Neu verrechnen** tippen.
- Die Aufnahmeanleitung findest du in [Kapitel 5 Shake](05-remote.md#shake-rauschreduzierung).

> Es läuft immer nur ein Stitching- oder Verrechnungsvorgang gleichzeitig. Der Fortschritt erscheint auf dem Bildschirm, und nach Abschluss öffnest du das Ergebnis mit einem Tipp aufs Banner.
