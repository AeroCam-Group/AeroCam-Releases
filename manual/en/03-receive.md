<!-- translated from zh-TW at commit 968641f -->

# 3. Auto Receive and Saving

## Camera Dashboard
Once connected, the top card on Home shows your camera's live status:

| Item | Details |
|---|---|
| Model, lens | For example, "Nikon Z f" and "NIKKOR Z 24–120 mm f/4" |
| Battery | Percentage (turns red at 20% or below) |
| Connection | Phone hotspot, Same Wi‑Fi, Camera Wi‑Fi, or USB |
| Memory cards | Used/total space and remaining shots for each card; dual slots listed separately |
| Quality | For example, `RAW` or `JPEG fine★ L`; updates automatically when you change quality or insert/remove cards |
| Save destination | For example, "Saving to: card ✓" — see [Save Destination and Shooting Without a Card](#save-destination-and-shooting-without-a-card) below |
| Transfer | Current status, with "History ›" in the top right |
| Camera styles | Last read C1–C9 slots — see [Chapter 6](06-edit.md#camera-styles-c1c9-pro) |

Items that the camera does not report in its current mode are hidden. Switching to "Camera control" and entering Remote usually unlocks more status items.

### Manage Cameras
Expand **Manage cameras (n)** below the dashboard to edit, delete, or add cameras. Each camera's details page shows:
- Model, serial number (middle digits masked; tap to reveal), firmware version, **shutter count**, and the date it was read.
- **Monthly shutter count**: bar chart for the last 6 months (tracked from when you start using AeroCam).
- Last connection time, method, lens, battery level, and free space on memory cards.
- Number of files transferred to your phone, first connection date, and saved network profiles.

Shutter count is read from the newest photo on the memory card, so there must be at least one photo on the card.

### Low Battery Alert
Sends a notification when the camera battery drops to your threshold (default 15%). It will not alert again until the battery rises at least 5% above the threshold. Adjust or turn it off under **Settings → Receive & notifications**.

📷 Screenshot: Camera dashboard

---

## Auto Receive (Pro)
1. On Home, tap Wi‑Fi → **Start receiving**. The app keeps a background connection to the camera (visible in your notification shade).
2. During playback on the camera, press **i → Send to PC / Select to send** (camera menu wording varies by model), and the photos transfer straight to your phone.

If you want photos pushed automatically the instant you press the shutter, use [FTP Receive](08-ftp.md). When a USB cable is plugged in, receiving switches to USB automatically.

### Pause Receiving
While Wi‑Fi auto receive is active, tap **⏸ Pause** at the top right of the "Transfer" card (or "Pause" in the notification) to pause temporarily:
- Wi‑Fi stays connected, so Camera roll and Remote continue working normally.
- Photos queued on the camera wait until you tap **Resume receiving**, then transfer in order. Any photo currently mid-transfer finishes first.
- Receiving resumes automatically if you tap Resume, stop receiving, swipe the app away from recents, lose Wi‑Fi, turn off the camera, or plug in a USB cable.

### When Disconnected
- If the connection drops, AeroCam reconnects automatically. After several failed retries, it searches again by camera ID so it still finds the camera even if its IP address changed.
- **Camera switches to Bluetooth transfer**: Because the camera has only one wireless chip, it turns off Wi‑Fi while sending over Bluetooth. Home displays "Camera is sending photos over Bluetooth… Wi‑Fi will reconnect automatically when done" and does not treat it as an error.
- **Camera roll or Remote borrows the connection**: The camera accepts only one connection at a time. When you open Camera roll or Remote, auto receive yields the link and resumes automatically when you leave.
- **When the camera cannot be found on Wi‑Fi**: After the timeout (default 3 minutes), receiving stops automatically and notifies you so it doesn't drain your battery. Change the timeout under **Settings → Receive & notifications**.

---

## Receive Rules
Configure these under **Settings → Receive & notifications**. Wi‑Fi, USB, and FTP all follow the same rules.

### File Types to Receive
Choose what to save: All files, JPEG only, JPG + RAW, Photos + videos, or Custom (JPEG, RAW, HEIF, TIFF, Video, Other).

Plus three extra toggles (Pro):

| Toggle | What it does |
|---|---|
| **Save JPEG only from RAW** | Extracts only the full-size JPEG embedded inside the RAW file (typically 2–5 MB instead of a 20–50 MB RAW) at full resolution with full EXIF metadata, saved as `DSC_1234_S.JPG`. Great for social sharing and everyday viewing |
| **Save compressed JPEG** | Recompresses incoming camera JPEGs on your phone (`_S.JPG`, same pixel resolution, quality set in Gallery settings) |
| **Replace compressed copy when original arrives** | Deletes the `_S.JPG` copy on your phone once the original JPEG is saved |

> To receive RAW files, set your camera's image quality to RAW or RAW+JPEG, and set the camera's "Connect to PC" upload option to RAW+JPEG (not "JPEG only"). Menu wording varies by model.

### Other Rules
| Rule | Details |
|---|---|
| Receive mode | Continuous, or stop after receiving one file |
| Large videos | Videos larger than the threshold (default 1024 MB) are skipped during auto receive, logged as "Filtered", and can be downloaded manually |
| Save folder | By camera, By date, By camera and date, or By file type |
| File naming | Original camera name (`DSC_1234.NEF`), Date prefix (`20261011_DSC_1234.NEF`), or Date & time prefix (`20261011_153012_DSC_1234.NEF` — keeps photos from multiple cameras sorted chronologically). Applies only to newly saved files |

### Where Files Are Saved
- Photos: `Pictures/AeroCam/…`
- Videos: `Movies/AeroCam/…`
- Other files: `Download/AeroCam/…`

Other apps like Google Photos can see them right away. If you uninstall and reinstall AeroCam, use **Settings → Storage & battery → "Rescan phone photos"** to bring previously saved photos back into the gallery.

### Duplicate Detection
- Checked using camera serial number, file name, size, capture time, and file hash. Duplicates are skipped and logged as "Duplicate".
- If you delete a photo on your phone (including moving it to Trash) and send it again, AeroCam saves it again.
- You do not need to stop and restart receiving to resend the same photo.

### When the Same Photo Arrives via Bluetooth and Wi‑Fi
Wi‑Fi transfers full-resolution files, so Wi‑Fi takes priority:
- If Wi‑Fi arrives first and Bluetooth sends it later: the Bluetooth copy is ignored.
- If Bluetooth arrives first and Wi‑Fi receives the same photo later, behavior follows **Settings → Receive & notifications → "Photos already received via Bluetooth"**:
  - **Replace with original when received over Wi‑Fi** (recommended): saves the full-size file and deletes the smaller Bluetooth copy.
  - **Do not download again over Wi‑Fi**.
  - **Keep both copies**.
- Original RAW files are always saved.

---

## Save Destination and Shooting Without a Card
Controls where photos go when you press the shutter. AeroCam checks whether a memory card is inserted and chooses automatically:
- **Card inserted**: Uses **Settings → Shooting → Save destination**:
  - **Memory card**: saves to the camera's card.
  - **Card + phone** (Pro): saves to the card and copies to your phone at the same time.
- **No card inserted** (Pro): Automatically switches to **Phone only (cardless capture)**. You can press the shutter as usual and photos transfer straight to your phone, named by capture time (e.g., `AC_20261025_193805.JPG`). Inserting a card switches back automatically.

Works from Home, Camera roll, and Remote, over both Wi‑Fi and USB.

**First-time setup:**
1. In the camera's Custom Settings menu, set **Slot empty release lock** to **Enable release** (otherwise the camera blocks the shutter when no card is inserted).
2. Over Wi‑Fi, set the camera's Connection type to **Camera control**. If it is on "Image transfer", AeroCam reminds you to switch about 3 seconds after the first shot; the photo stays buffered on the camera and transfers automatically once you switch. USB does not have this limitation.
3. One-tap connect does not support shooting without a card — use a phone hotspot or same Wi‑Fi instead.

**Status bar messages** (top of Home and Camera roll):

| Message | Meaning |
|---|---|
| Saving to: card ✓ | Saving to the camera's memory card |
| Saving to: card + phone ✓ | Saving to both the card and your phone |
| Saving to: phone only (no card in camera) | Photos transfer directly to your phone |
| Camera is in "Image transfer" mode… (red) | Switch Connection type to "Camera control" |
| One-tap Wi‑Fi: no memory card, cannot shoot (red) | Insert a card, or switch to hotspot / same Wi‑Fi |
| Memory card full (red) | Swap cards or free up space (does not auto-switch to phone only) |
| No memory card in camera, cannot shoot (red) | Free tier, or phone has less than 1 GB free space |

> Video recording is not available without a memory card, and continuous shooting is slower because each photo must transfer to the phone.

---

## Photo Location (GPS)
Under **Settings → Receive & notifications → Photo location**, there are two switches:
- **Send location to camera (Bluetooth)** (on by default): When the camera powers on or sends over Bluetooth, your phone sends its GPS location to the camera so the camera embeds it in new photos.
- **Add location to received JPEGs (phone)**: Adds your phone's location to JPEGs received over Wi‑Fi, USB, FTP, gallery download, or remote shooting based on capture time. Asks once the first time you start receiving.
  - RAW files are never modified, and photos that already have GPS data keep their original coordinates.
  - Location history recorded during a session stays only on your phone and is deleted after 24 hours.
  - If the capture time doesn't match any recorded point, nothing is written (better no location than a wrong one).
  - AeroCam must be open when you start receiving in order to record location.

> Embedded GPS coordinates travel with the original file when you share it. QR code sharing removes GPS by default — see [Chapter 4](04-gallery.md#qr-code-sharing).

---

## History
Tap **History ›** at the top right of the "Transfer" card on Home. Lists every receive, gallery download, and remote capture result (Succeeded, Duplicate, Skipped, Failed) with thumbnails.
- Tap any entry to preview full screen inside the app.
- Search, filter by camera, or clear history. Clearing history does not delete files on your phone.
