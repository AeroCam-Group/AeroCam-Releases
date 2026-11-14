<!-- translated from zh-TW at commit 968641f -->

# 10. Privacy and Anonymous Statistics

AeroCam has no user accounts. Your photos transfer directly between your camera and your phone and **are never uploaded to any server**. Only the small items listed below ever leave your phone.

## When the App Connects to the Internet
| Feature | What is sent | Can you turn it off? |
|---|---|---|
| Check for updates (Beta) | Queries GitHub only for the latest version info | Runs automatically once a day |
| Anonymous usage statistics | See below | Yes, under Settings → Support |
| QR code sharing | Runs only on your local network (same Wi‑Fi or phone hotspot) so people who scan can view your selected photos | Stops when you tap Stop or when the timer ends |

## Anonymous Usage Statistics
Used to understand roughly how many people use AeroCam, which cameras and features they use, and where issues happen so we know what to build next. **Never sold to anyone and never used for ads.**

- **Toggle**: **Settings → Support → "Send anonymous usage statistics"**, on by default.
- Explained once the first time you connect to a camera, where you can choose "OK" or "Turn off". **Nothing is sent before you answer.**
- **When turned off**: Sending stops immediately, and both the random ID below and any unsent data are deleted. Turning it back on generates a new ID.
- When offline (for example, while connected to the camera's own Wi‑Fi), events are stored on your phone and sent later when internet access is available.
- Dev builds never record or send statistics.

### Data Sent
- **App-generated random ID**: Not derived from your phone or camera; resets if you reinstall the app or turn statistics off.
- Camera model (for example, Nikon Z f) — model name only.
- Connection method (Bluetooth, Wi‑Fi, USB, FTP) and Wi‑Fi type (camera's own Wi‑Fi, phone hotspot, router).
- Which features were used each day (feature names only, once per day), including locked features tapped.
- Number of successful or failed connections; on failure, only a category code (such as "timeout") is sent, never error messages.
- Add-camera steps: started, succeeded, camera not found, and failure reason.
- Number of photos received each day (counts for JPEG, RAW, and video — counts only).
- Whether permissions were granted or denied.
- Current tier (Free, Beta key…), app version, app language, and major Android version.
- Country: determined from the connection; only the country code is stored.

### Never Sent
Camera serial number, owner or copyright name set in the camera, location (GPS), photos and videos, file names, shooting metadata (EXIF), Wi‑Fi names and passwords, phone IDs (IMEI, Android ID, advertising ID), name, email, account, or error message text.

### Retention
- Per-device daily details are kept for 90 days, after which only daily aggregate totals remain.
- Random IDs inactive for about 13 months are deleted.
- The server necessarily sees your IP address when handling a request; it is used only to determine country and prevent abuse, and **is never stored in statistics data**.

## Location Information
- **Send location to camera (Bluetooth)**: Your phone sends its location to the camera so the camera writes it into photos.
- **Add location to received JPEGs (phone)**: Off by default. When enabled, location points recorded during a receive session stay only on this phone and are deleted after 24 hours.
- Both switches are under **Settings → Receive & notifications → Photo location** — see [Chapter 3](03-receive.md#photo-location-gps).
- Location embedded in a photo travels with the file when you share the original. **QR code sharing strips location by default.**

## Permission Usage
| Permission | Purpose |
|---|---|
| Bluetooth, Nearby devices | Pairing with the camera, Bluetooth photo transfer, Bluetooth remote, finding Wi‑Fi cameras |
| Location | Sending location to the camera or adding it to photos; also required by Android to read Wi‑Fi names |
| Notifications | Receive progress, incoming photos, transfer issues, low camera battery alerts |
| Photos and videos | Displaying and organizing photos in Phone photos |

## Diagnostic Info
**Settings → Support → "Copy diagnostic info"** only copies text to your clipboard — **you decide** whether to send it to us. It includes app version, phone and network status, camera capabilities, and recent connection logs, with only the last 4 digits of your camera serial number. Before pasting into a public GitHub Issue, review it to make sure nothing you prefer to keep private is included.
