<!-- translated from zh-TW at commit 968641f -->

# 11. FAQ and Troubleshooting

## General
**Can I transfer photos from my camera to my phone without upgrading to Pro?**
Yes. On the Free tier, you can auto-receive ~2 MP resized JPEGs over Bluetooth, or browse the camera's SD card over a USB cable and manually pick and download full-resolution originals.

**Do the Beta or test keys cost money?**
No. Both are published free of charge only on GitHub at AeroCam-Releases. If anyone asks you to pay, it is not an official channel.

**App shows "This is not an official version" on launch**
The APK has been repackaged by a third party. It will not accept test keys and may contain unwanted code. Uninstall it and download again from AeroCam-Releases.

**After updating, my paired camera and test key disappeared**
Starting with 92.03.09, newer builds install as a separate app and do not migrate data from older builds. Pair your camera and enter the test key again.

**Where are photos saved?**
Photos go to `Pictures/AeroCam`, videos to `Movies/AeroCam`, and other files to `Download/AeroCam`. Google Photos and other gallery apps can see them. Files saved by builds older than 92.03.09 remain in their original folder.

**I deleted a photo on my phone and want to transfer it again**
Just send it again from the camera — AeroCam detects that the file is no longer on your phone and saves it.

**Photos don't show up after restoring from Trash or reinstalling the app**
Run **Settings → Storage & battery → "Rescan phone photos"**.

---

## Connection
**Cannot connect to the camera over Wi‑Fi**
1. Make sure the camera is on the "Connect to PC" screen with the Wi‑Fi icon visible; half-press the shutter if the screen went to sleep.
2. Check Connection type: use **Image transfer** for auto receive and gallery; use **Camera control** for remote shooting and shooting without a card.
3. Phone hotspot mode: confirm your hotspot is on and the camera is connected to it.
4. Same Wi‑Fi mode: confirm both phone and camera are on the exact same SSID (phones sometimes switch automatically to another Wi‑Fi or mobile data).
5. Try **One-tap connect** — no hotspot or router needed.
6. Tap **ⓘ** and walk through the visual connection guide step by step.

**Camera is never found on hotel or convention Wi‑Fi**
Public Wi‑Fi networks usually block device-to-device traffic. Switch to your phone hotspot or One-tap connect.

**Camera says "Already paired with another device"**
That camera network profile is paired with a different app. Create a new network profile on the camera and pair again.

**One-tap connect cannot find the camera's Wi‑Fi**
After receiving the Bluetooth command, the camera takes 10–30 seconds to bring up its Wi‑Fi, and AeroCam retries automatically. If it still fails, double-check the camera's Wi‑Fi password.

**Phone hotspot keeps turning off**
Some phones turn off their hotspot when connected devices don't use internet data. Disable "Turn off hotspot automatically" in your phone's hotspot settings, or use One-tap connect.

**Camera won't reconnect after toggling the phone hotspot**
Your phone's hotspot IP address may have changed. Wi‑Fi auto receive finds the camera automatically, while FTP requires updating the server IP on the camera.

**Nothing happens when plugging in USB**
1. Confirm the camera's USB setting is **MTP/PTP**.
2. Make sure the cable supports data transfer (some cables are charge-only).
3. Tap Allow on Android's USB access prompt.
4. Tap `⋮` at the top right of the USB tile → **USB test** to see which step failed.

**Background receiving keeps getting interrupted**
Disable battery optimization under **Settings → Storage & battery**. On Xiaomi, OPPO, and similar phones, also set AeroCam to "Unrestricted" battery usage in system settings.

---

## Bluetooth
**Bluetooth photo transfer is stuck**
- When shooting RAW, the camera has to convert each image to JPEG before sending, and operating the camera cancels the transfer. It works best if you turn the camera off after shooting and let it transfer in the background.
- Tap **Disconnect and reconnect** on the Bluetooth tile, or **⋮ → Restart Bluetooth service** (your pairing is preserved).

**Pressing AF on the Bluetooth remote doesn't focus**
The camera must allow half-press shutter AF. If you use back-button AF-ON, check your camera's Custom Settings to ensure **AF activation** is set to **Shutter/AF-ON**.

**Will receiving the same photo over Bluetooth and Wi‑Fi save two copies?**
Not by default: when Wi‑Fi receives the original file, it automatically deletes the smaller Bluetooth copy. You can change this under **Settings → Receive & notifications → "Photos already received via Bluetooth"**.

---

## Remote Shooting
**Cannot adjust shutter speed or ISO**
- Shutter speed requires S or M mode; aperture requires A or M mode; turn off Auto ISO before adjusting ISO manually.
- On cameras with physical dials like the Zf: set the shutter speed dial to **1/3 STEP** and the ISO dial to **C**.

**Tapping the preview doesn't move the focus point**
Set the camera's AF-area mode to a mode that allows a movable point (such as Single-point AF). In Auto-area AF, the camera chooses automatically.

**Some dashboard items are missing (lens, remaining shots, shutter count)**
Some cameras report certain details only in specific modes. Switching to "Camera control" and entering Remote usually makes them available. Shutter count requires at least one photo on the memory card.

**Where can I see the exact color temperature (Kelvin)?**
Nikon stores the measured Kelvin value in an encrypted MakerNote tag, so "Details" displays the White Balance preset name only.

---

## Save Destination and Shooting Without a Card
**Pressing the shutter does nothing when no card is inserted**
Confirm **Slot empty release lock** is set to **Enable release** on the camera, and that AeroCam is connected (status bar shows "phone only").

**Photos show "DEMO" on the camera**
If no card is inserted and AeroCam isn't connected in "phone only" mode, the camera marks shots as **DEMO** and does not save them. Insert a card or shoot while connected to AeroCam.

**Photos aren't reaching my phone, and a red banner appears at the top of Home**
- "Camera is in 'Image transfer' mode": Shooting without a card requires **Camera control**. Switch modes on the camera; it will reconnect and transfer the buffered shots automatically.
- "One-tap Wi‑Fi: no memory card": One-tap connect does not support cardless capture. Insert a card or switch to a phone hotspot / same Wi‑Fi.

**"Connection lost" pops up**
When saving to phone only, dropping the connection for more than 10 seconds triggers an alert because photos taken while disconnected aren't saved to a card. AeroCam recovers automatically once reconnected.

---

## Editing and Styles
**NEF won't open or cannot be edited**
High efficiency / High efficiency★ NEF files are edited using their embedded full-size JPEG; files containing only a small preview cannot be edited. To develop full RAW files on your phone, switch the camera to **Lossless compression** — see [Chapter 6](06-edit.md#phone-editable-raw-switch-camera-raw-compression).

**.np3 look differs from the camera**
The phone editor simulates tone curves and saturation; Color Blender and Color Grading are not simulated yet, so results are approximate. If a JPEG already had a Picture Control applied in-camera, the effects stack.

**Colors look different after writing .np3 to the camera**
Custom camera slots accept only **Base + Curve + Sharpening**; Saturation, Color Blender, and Color Grading cannot be written over the connection. For full results, copy the `.np3` file to a memory card and import it via the camera menu.

**Panorama stitching fails or skips photos**
Each frame needs about 30% overlap with neighboring frames. Unmatched files are listed by name, and grid panoramas require all tiles to be present before stitching.

---

## FTP
**Camera displays Err.31 or Err.32**
Update to the latest Beta, and double-check that the IP address, port `2121`, user name `aerocam`, and password on the camera match AeroCam's FTP tile, with Passive mode turned on.

**Camera displays a login failure**
The password must match the one shown on AeroCam's FTP tile exactly (case-sensitive). If you tapped "Regenerate" password, update it on the camera too.

**Cannot connect Camera roll or Remote while FTP is running**
While in FTP mode, the camera does not accept Wi‑Fi connections for gallery or remote shooting. Use a USB cable, or stop FTP receive and switch the camera back to "Connect to PC".

---

## Other
**App crashes**
Reopen AeroCam, go to **Settings → Support → "Copy diagnostic info"**, and paste it when [reporting the problem](12-report.md) — it includes the stack trace of the last crash.

**How do I turn off anonymous usage statistics?**
Turn off **Settings → Support → "Send anonymous usage statistics"** — see [Privacy and Anonymous Statistics](10-privacy.md).
