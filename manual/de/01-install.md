<!-- translated from zh-TW at commit 968641f -->

# 1. Installation und Erste Schritte

## Installation
1. Lade die neueste Beta-APK (`…-Beta-xx.xx.xx.apk`) unter [Releases](https://github.com/AeroCam-Group/AeroCam-Releases/releases/latest) herunter.
2. Öffne die APK auf deinem Smartphone. Beim ersten Mal fragt Android nach der Berechtigung „Unbekannte Apps installieren“ – bitte erlaube dies.
3. Sobald eine neue Version erscheint, kannst du sie einfach herunterladen und über die alte installieren. Gekoppelte Kameras und Einstellungen bleiben erhalten.

> Lade die App nur von AeroCam-Releases herunter. APKs aus anderen Quellen könnten verändert worden sein. Wenn beim Öffnen „Dies ist keine offizielle Version“ erscheint, wurde die App von Dritten neu verpackt: Sie akzeptiert keine Testschlüssel und könnte fremden Code enthalten. Deinstalliere sie und lade sie erneut von AeroCam-Releases herunter.

> Wenn du eine **ältere Beta vor 92.03.09** genutzt hast: Neuere Versionen werden als eigene App installiert. Kopple deine Kamera neu, gib den Testschlüssel erneut ein und deinstalliere die alte Version erst, wenn alles läuft.

📷 Screenshot: Systemdialog „Unbekannte Apps installieren“

## Berechtigungen
Die App fragt Berechtigungen erst ab, wenn du eine Funktion nutzt, die sie benötigt. Was du nicht brauchst, musst du nicht erlauben:

| Berechtigung | Zweck |
|---|---|
| Bluetooth, Geräte in der Nähe | Bluetooth-Kopplung, Fotoübertragung per Bluetooth, Bluetooth-Fernauslöser; ab Android 13 auch zum Finden von Wi‑Fi-Kameras nötig |
| Standort | Sendet den Smartphone-Standort an die Kamera (zum Speichern in Fotos) oder ergänzt empfangene JPEGs mit Standortdaten; wird von Android auch zum Auslesen des Wi‑Fi-Namens benötigt |
| Benachrichtigungen | Empfangsfortschritt, empfangene Fotos, Übertragungsprobleme, Warnung bei niedrigem Kamera-Akku |
| Fotos und Videos | Fotos auf dem Smartphone anzeigen und verwalten |

Ausführliche Infos zu jeder Berechtigung findest du unter [Datenschutz und anonyme Statistiken](10-privacy.md).

## Bildschirmübersicht
Unten gibt es vier Tabs:

| Tab | Inhalt |
|---|---|
| **Start** | Kamera-Dashboard (Akku, Objektiv, Speicherkarten, Verbindungsstatus), vier Verbindungsarten (Wi‑Fi, USB, Bluetooth, FTP), Übertragungsstatus und Verlauf, Kamerastile, Kameras verwalten |
| **Kamera-Ordner** | Zwei Unter-Tabs: „Smartphone-Fotos“ und „Kamera-Speicherkarte“ – siehe [Kapitel 4](04-gallery.md) |
| **Fernaufnahme** | Live-Bild der Kamera auf dem Smartphone ansehen, Einstellungen ändern, Fotos und Videos aufnehmen – siehe [Kapitel 5](05-remote.md) |
| **Einstellungen** | Fünf Kategorien – siehe [Kapitel 7](07-settings.md) |

Wenn du nicht weißt, wie du die Kamera verbindest, tippe auf **ⓘ** neben dem Verbindungsstatus auf dem Startbildschirm oder oben rechts bei jedem Schritt unter „Kamera hinzufügen“, um eine Schritt-für-Schritt-Anleitung mit Bildern zu öffnen.

📷 Screenshot: Startbildschirm

## Testschlüssel (Pro und Cine freischalten)
Die Beta startet in der kostenlosen Version.
1. Kopiere den aktuellen Testschlüssel von der [AeroCam-Releases-Startseite](https://github.com/AeroCam-Group/AeroCam-Releases). In der App öffnet **Einstellungen → Support → „Kostenlosen Schlüssel holen“** diese Seite direkt.
2. Gehe zu **Einstellungen → Support → „Testschlüssel eingeben“**, füge den gesamten Text ein und tippe auf „Anwenden“. Auch beim Antippen einer gesperrten Funktion erscheint im Dialog „Testschlüssel eingeben“.
3. Jeder Schlüssel ist 14 Tage gültig und wird jede Woche erneuert. Nach Ablauf kehrt die App zur kostenlosen Version zurück – füge dann einfach den neuen Schlüssel ein.

> Sowohl die Beta als auch die Testschlüssel sind **kostenlos** und erscheinen ausschließlich auf GitHub unter AeroCam-Releases. Wenn jemand Geld dafür verlangt, ist das kein offizieller Kanal.

## Nach Updates suchen
Die Beta prüft einmal täglich beim ersten Öffnen automatisch auf Updates. Du kannst auch manuell unter **Einstellungen → Support → „Nach Updates suchen“** prüfen.

## Sprache
Die Oberfläche unterstützt Traditionelles Chinesisch, Vereinfachtes Chinesisch, Japanisch, Englisch, 한국어, Deutsch, Français, Español, Tiếng Việt, ไทย und Bahasa Indonesia. Standardmäßig folgt sie der Systemsprache deines Smartphones, du kannst sie aber unter **Einstellungen → Darstellung und Sprache → Sprache** wechseln.

Englisch, Traditionelles Chinesisch und Japanisch sind immer vollständig übersetzt. Neue Funktionen in anderen Sprachen erscheinen eventuell zunächst auf Englisch und werden später nachgereicht. Wenn dir eine schlechte Übersetzung auffällt, melde sie bitte über das Formular „Übersetzungsfehler“ unter [Problem melden](12-report.md).

## Anonyme Nutzungsstatistiken
Nach der ersten Verbindung mit einer Kamera erklärt die App einmalig das Senden anonymer Nutzungsstatistiken. Du kannst „OK“ oder „Ausschalten“ wählen – vor deiner Antwort wird nichts gesendet. Du kannst die Funktion jederzeit unter **Einstellungen → Support** ausschalten. Was genau gesendet wird und was niemals gesendet wird, steht unter [Datenschutz und anonyme Statistiken](10-privacy.md).
