<!-- translated from zh-TW at commit 968641f -->

# 4. Gallery

At the top of the **Camera roll** tab, there are two sub-tabs: **Phone photos** (already saved on your phone) and **Camera SD card** (browse photos directly on your camera).

## Camera SD Card
Browse your camera's memory cards directly on your phone (dual slots supported) **without selecting photos on the camera first** and without starting auto receive.
- Free over USB; Pro over Wi‑Fi.
- Opening the tab does not occupy the camera until you tap "Connect to browse SD card". Because the camera accepts only one connection at a time, auto receive pauses while you browse and resumes automatically when you leave.
- Switching tabs or viewing a photo full screen keeps the connection alive for 20 seconds so you can jump right back. Moving the app to the background releases the camera immediately (active downloads finish first).
- If you take a photo while the gallery is open, it appears at the top within 1–2 seconds (fastest over USB).

📷 Screenshot: Camera SD card grid view

### Browsing and Filtering
- Grouped by capture date; tap the calendar icon at the top right to jump to a specific day (Year → Month → Day).
- Filters: All, RAW, JPEG, Video, **Not downloaded** (shows only files not yet on your phone), and Starred. When viewing "Not downloaded" or "Starred", tap "Select all N" at the bottom.
- **Columns per row**: Tap the grid icon at the top right to pick 2–7 columns, or pinch to zoom. Landscape mode adds 50% more columns.
- Videos only read the file header without downloading the full video: bottom-left shows `▶ 0:12` (duration) and top-left shows `1080 24p` (resolution & frame rate).

### Thumbnail Badges
Tap **ⓘ** at the right end of the filter bar for a full legend:

| Corner | Meaning |
|---|---|
| Top-left | Second card (`SD2`) or video format |
| Top-right | Star rating |
| Bottom-left | File format: `RAW` (amber), `JPEG` (gray), or `▶` video duration |
| Bottom-right | Copies already on your phone: **✓RAW**, **✓JPEG**, **✓JPEG.S** (multiple badges can stack). Green = camera original, blue = copy, no badge = not on phone yet |

### Selecting
- Long-press one photo and **drag** across to select a whole range; dragging near the screen edge auto-scrolls.
- Tap "Select" next to any date header to select that entire day.
- While selecting, the bottom navigation bar hides and turns into an action bar (Download, Rate, Delete). Tap **✕** at the top left to cancel.

### Downloading
Select photos and tap **Download**. Each option shows **how much phone storage it will use**, with available phone storage at the bottom:
- **Originals**: Full-size RAW, JPEG, or video files.
- **JPEG only** (Pro): Extracts the embedded full-size JPEG from RAW files, or recompresses original JPEGs on your phone (same resolution). Saved as `DSC_1234_S.JPG` with full EXIF metadata. Set compression quality (60/70/80/90%, default 80%) under **Settings → Receive & notifications → Gallery**.
- Downloads run in a queue with live progress and a stop button. Files already on your phone are skipped automatically, and results are logged in History.
- After downloading, the app asks "Keep selection?" and clears it automatically when the countdown ends so you don't accidentally tap "Delete from camera". Check "Remember my choice" to skip the prompt.

### Delete from Camera (Pro)
Select photos and tap the solid **red** "Delete from camera (N)" button. After confirmation, files are **permanently deleted** from the memory card and cannot be undone. Photos not yet downloaded to your phone trigger an extra warning. Protected files (🔑) are skipped by the camera.

> Only the solid red button modifies your camera's memory card. All other delete actions affect only your phone.

### Full-Screen Viewer
Tap any thumbnail to view full screen. Swipe left/right to switch photos; pinch or double-tap to zoom.
- **Portrait**: File name, time, and size at the top; exposure info (`shutter · aperture · ISO · focal length`) below the photo; action buttons at the bottom.
- **Landscape**: Photo fills the screen with info on the right; tap the photo to hide or show overlays.
- Toggle **Details**: Shows RGB histogram, Picture Control, white balance, lens, dimensions, and file size read directly from the camera without downloading first.

### Star Ratings
Rate photos 1–5 stars in the gallery, then filter by "Starred" to download only your picks. Ratings are written into the downloaded file's EXIF Rating tag so Lightroom and other editors recognize them.

---

## Phone Photos
Shows photos already saved on your phone — no camera connection needed.
- Only shows files still present on your phone: if you delete a photo in Google Photos or another app, it disappears here too, and returns automatically if you restore it from Trash.
- Sorted by capture time, with filters for "Edited", "Panorama", "Shake", and more.
- **Full-screen viewer**: Shows shooting parameters and **Details** (capture time, transfer time, RGB histogram, Picture Control, white balance, lens, dimensions, file type, and source). Bottom actions: **Share**, **Open with...**, **Edit**, and **Delete**.
- **Delete**: Select photos and tap **Delete** to choose "Delete all on phone", "RAW only", "JPEG only (incl. .S)", or "Videos only". Files move to your phone's **Trash** and can be restored within 30 days. **Your camera's memory card is completely untouched.**
- **Image processing**: Select multiple photos and swipe up the bottom action bar to expand "Image processing" for **Stitch (Panorama)** and **Noise-reduction merge (Shake)** — see [Chapter 6](06-edit.md#image-processing-panorama-stitching-and-noise-reduction-merge-pro).
- Missing photos? Run **Settings → Storage & battery → "Rescan phone photos"**.

📷 Screenshot: Phone photos grid and full-screen viewer

---

## Memory Card Backup (Pro)
Back up your camera card to your phone from the USB tile ("Back up memory card") or the top-right menu in Camera roll ("Backup").
- **Scope**: Entire card, or custom (capture date, files not yet on phone, SD1 / SD2).
- **File types**: RAW + JPEG, RAW only, JPEG only, or Save JPEG only from RAW, with optional videos.
- Tap **Calculate** to see file count, total size, estimated time, and free phone space. Backing up RAW files or videos over Wi‑Fi warns you that it will take a long time.
- Runs in the background (pausable from the notification shade). If interrupted, it asks to resume next time.
- Every saved file is read back and verified. Once a backup finishes completely with zero errors, you can tap **Delete backed-up files from camera** (deletes only verified files from that run, with double confirmation).

---

## QR Code Sharing
Let people nearby scan a QR code with their phone camera to view and download your photos in their browser — **no app installation required**.

### How to Share
1. In **Phone photos**, long-press to select photos and tap the first button on the action bar: **Share**. Only photos already on your phone (JPEG, RAW) can be shared; video sharing is not supported yet.
2. A large QR code and short URL (e.g., `192.168.43.1:8080/k7Qx2mPa`) appear. Anyone nearby can scan it with their camera app.
3. You can also tap **Copy link** or **Send link** (LINE, Messenger, etc.).

> **Recipients must be on the same Wi‑Fi network or connected to your phone's hotspot.** Public Wi‑Fi in hotels and cafes often blocks device-to-device connections — switch to your phone hotspot if the page won't load.

### Options
- **Set password** (off by default): Requires a 4-digit PIN before viewing. The password is never included in shared text messages — tell your recipient in person.
- **Quality**: Free tier shares resized JPEGs (2048 px long edge) downloaded one by one. Pro unlocks **Full resolution**, **Include RAW files**, and multi-select **ZIP download**.
- **Keep location (GPS)** (off by default): GPS data is stripped from shared JPEGs by default and is never shown on the web page. Your original files on the phone are never altered.
- Auto-stop timer: Set under **Settings → Receive & notifications → Gallery** (15 / 30 / 60 minutes, default 30).

### While Sharing
- Sharing continues in the background if you leave the screen or turn off the display; your notification shade has buttons to "Show QR code" and "Stop sharing".
- Brief network drops wait 30 seconds; if your IP address changes, the same link code is kept and the screen prompts recipients to rescan.
- The recipient's web page automatically displays in Traditional Chinese, Simplified Chinese, Japanese, or English based on their phone language, with full-screen preview, EXIF info, and one-tap retry on failed downloads.
- **Security**: URLs include a random 8-character token with brute-force lockout; only selected photos are exposed; recipients can only view and download (no upload or delete). Tapping **Stop sharing** invalidates the URL immediately.

> Phones from Xiaomi, OPPO, and similar brands aggressively kill background apps. The share screen reminds you to set AeroCam to "Unrestricted" battery usage.

📷 Screenshot: QR code sharing screen and recipient browser view
