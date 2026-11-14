<!-- translated from zh-TW at commit 968641f -->

# 5. Remote Shooting and Control

| Method | Connection | Live view | Tier |
|---|---|---|---|
| [Remote Shooting](#remote-shooting-pro) | Wi‑Fi or USB | ✅ | Pro |
| [Bluetooth Remote](#bluetooth-remote-free) | Bluetooth | ❌ | Free (interval timer is Pro) |
| [Video Monitor](#video-monitor-cine) | USB (Wi‑Fi experimental) | ✅ Built for video | Cine |

---

## Remote Shooting (Pro)
See your camera's live view on your phone, tap to focus, adjust exposure settings, and shoot photos or video. Works over **both Wi‑Fi and USB**, switching to USB automatically when a cable is plugged in.

**Requirements**
1. A camera model with "Connection type" in its menu — see [Supported Cameras](README.md#supported-cameras).
2. Over Wi‑Fi, set the camera's Connection type to **Camera control** — see [Connect Your Camera](02-connect.md#camera-connection-type). If it is still set to "Image transfer", AeroCam shows the steps to switch and reconnects automatically once changed.

Remote shooting runs full screen with the bottom tabs hidden. Tap **←** at the top left or press your phone's Back button to return to Home.

📷 Screenshot: Remote shooting screen (portrait and landscape)

### Screen Layout
| Area | What's shown |
|---|---|
| Top | Camera settings: Mode, Shutter, Aperture, ISO, Auto ISO, EV, WB, Focus, AF-area, Metering, Picture Control, Quality. Two rows in portrait; one scrollable row in landscape |
| Third top row | Back, Record video, Clean view, Lock screen, Save destination, Battery |
| Center | Full uncropped live view with focus box, level gauge, exposure meter, and overlays |
| Bottom | 6 customizable quick toggles + "More" |
| Bottom edge | "Shooting" (shooting method selector), Shutter button, AF button, latest photo thumbnail, and remaining shots |

In landscape mode, quick toggles move to the left black bar and the shutter button sits at the bottom right. **Left-handed mode** (**Settings → Shooting**) moves the shutter button to the bottom left.

### Adjusting Camera Settings
Tap any value at the top to open an adjustment bar at the bottom without covering the live view.
- Exposure mode is read-only (switch P/S/A/M on the camera). Shutter is adjustable in S and M; aperture in A and M.
- When Auto ISO is on, ISO displays `AUTO`. EV includes a `0` button to reset to zero.
- Choosing `K` for White Balance lets you dial in the exact color temperature. Picture Control displays the active name on the camera, including custom ones.
- If a setting **cannot be changed**, the app explains why. On cameras with physical dials like the Zf and Zfc, set the shutter speed dial to **1/3 STEP** and the ISO dial to **C**.

### Focus and Shutter
- **Tap to focus**: Tap anywhere on the live view to move focus there. Set the camera's AF-area mode to one that allows a movable point (such as Single-point AF); in Auto-area AF, the camera decides.
- The actual camera focus box is drawn on screen (Single-point, Dynamic-area, Auto-area, and Tracking are all visible), turning green on focus lock and red on failure.
- **Shutter button**: Tap once to shoot; **press and hold = half-press focus** (border turns green), release to take the shot.
- **AF button**: Refocuses at the current focus point.
- **Focus before shooting** (on by default): Turn off to fire the shutter immediately without waiting for AF (faster for manual focus or pre-focused shots).
- **Tap screen to shoot**: When enabled, tapping the preview focuses at that spot and immediately takes a photo.
- Taps along the far left/right edges (Android back-gesture zone) are ignored so swiping back won't accidentally move focus.

### Bottom Quick Toggles (Customizable)
Defaults to Peaking, Zebra, Level, Grid, Zoom, and one empty slot, with "More" fixed on the far right.
- **Tap** to toggle on/off; **press and hold for 0.5 seconds** to open sub-options (peaking sensitivity, zebra threshold, grid style, zoom magnification).
- **Customize**: Tap the gear icon at the top right of "More". Available toggles: Peaking, Zebra, Level, Grid, Zoom, Histogram, Exposure meter, Tap to shoot, Focus before shooting, Copy to phone, Snapshot, Night mode, Live preview, and Self-timer.

### More Drawer
"More" opens a non-opaque drawer (from the bottom in portrait, from the side in landscape) so you can always see the live view. Divided into three tabs:
- **Aids**: Live preview, Peaking, Overexposure warning (Zebra), Level gauge, Grid lines, Histogram, Exposure meter, Magnified focus, Night mode.
- **Shoot**: Focus before shooting, Tap screen to shoot, AF-area mode, Copy each shot to phone, Preview snapshot.
- **Tools**: Ghost overlay, Multi-shot checklist, Tips.

### Shooting Aids (Phone Display Only — Never Saved in Photos)
| Aid | Details |
|---|---|
| Level gauge | Reads the camera's pitch/roll sensor; turns green within 0.5° and shows roll and pitch angles |
| Histogram | Tap to toggle between "Luma + RGB overlay" and "RGB parade" |
| Zebra (overexposure) | Highlights areas above the brightness threshold with diagonal stripes: 85 / 90 / 95 / 100% (default 95%) |
| Focus peaking | Outlines sharp in-focus edges in color (red, yellow, blue, white) with Low / Medium / High sensitivity for manual focus |
| Exposure meter | Vertical Nikon-style viewfinder meter in 1/3 EV steps. Shows metering offset in M mode, or exposure compensation in P/A/S |
| Grid lines | Rule of thirds, 4×4 grid, Golden ratio, Golden spiral, Diagonals, Center cross |
| Zoom | When supported by the camera (e.g., Zf), **the camera itself zooms in** so you see true sensor pixels at 50% / 100% / 200% / 400%. Tap or use ◀ ▲ ▼ ▶ to pan, and use `Near ◀◀ ◀ ▶ ▶▶ Far` at the bottom for fine manual focus stepping. Other models use app digital zoom (2× / 4× / 8×) |

> Shooting aids are calculated from the camera's compressed live view stream and are meant as a guide — always rely on the captured photo's histogram for critical exposure.

### Shooting Methods
Tap **Shooting** next to the shutter button to pick a mode. The button turns yellow and a status strip appears above the shutter (e.g., `Interval timer shooting · Every 5s · 10 shots`). Tap it to adjust settings and press **Start**, or tap **×** to return to normal shooting. Progress appears at the top while running, with a **Stop** button to cancel anytime.

| Method | Settings | Details |
|---|---|---|
| Single / Normal | 1–9 shots | When combined with Self-timer, fires a burst of N shots (~1 sec apart) after the countdown |
| **Self-timer** | Off, 2, 5, 10 sec | At the top of the "Shooting" menu; works with every shooting method and video recording. Shows a large countdown on screen; tap shutter again to cancel |
| Bulb | 1–3600 sec | Camera must be in M mode with shutter set to Bulb or Time; closes automatically when time is up |
| Interval timer shooting | 2–999 shots, 1–3600 sec interval | Shoots automatically at fixed intervals and displays total duration; pair with "Copy each shot to phone" for time-lapse review |
| Exposure bracketing | 3 / 5 / 7 / 9 shots, 0.3–3.0 EV step | Steps exposure around your current setting and restores the original value when done |
| Focus shift shooting | 2–300 shots, step width | Focuses on the nearest point first and steps focus toward infinity between shots. Requires an AF lens; stack the images on a computer afterward |
| Panorama | Grid size or "Free" | Shoot multiple overlapping frames and stitch into a panorama — see below |
| Shake (noise-reduction merge) | 4 or 8 shots | Handhold a quick burst and merge into a cleaner, low-noise photo — see below |

> AF and tap-to-focus are paused while a multi-shot tool is running. Leaving Remote prompts for confirmation first.

#### Panorama (Stitching)
- **Grid**: Pick a grid size and AeroCam calculates the exact pan/tilt angles per tile while you turn the camera and press the shutter. A guide tells you whether overlap is sufficient ("Ready / Can turn more / May not overlap") and overlays a semi-transparent edge of the previous frame for alignment.
- **Free**: No fixed grid — just overlap each frame by ~30% in any direction (up to 30 shots).
- Once you have 2 or more shots, tap **Stitch** to merge them on your phone; a full 360° sweep outputs a 360° panorama. Camera level data from each shot ensures a level horizon.
- Frames are grouped into a stack in Phone photos so you can re-stitch later — see [Chapter 6](06-edit.md#image-processing-panorama-stitching-and-noise-reduction-merge-pro).

#### Shake (Noise-Reduction Merge)
- Gives cameras without pixel-shift a multi-shot quality boost: shoot 4 or 8 frames handheld (or on a tripod), and AeroCam aligns and averages them, cutting noise to roughly one-third (at 8 shots) without losing detail.
- Merges automatically in the background ("Merging %") and saves as `SHAKE_<timestamp>.JPG` at full resolution with EXIF metadata.
- Moving subjects (cars, people, leaves) are taken from the sharpest single frame to prevent ghosting, and overly blurred frames are automatically rejected.
- Ideal for night scenes, dim interiors, and high ISO.

### Ghost Overlay (Pro)
**More → Tools → Ghost overlay**: Places a reference image over the live view as a **semi-transparent overlay** or **split-screen comparison**, with opacity control and a "Capture current frame" shortcut. Great for repeat framing, copy work, and alignment.

### Other Features
- **Copy each shot to phone**: Saves every shot following your receive rules, including "Save JPEG only from RAW".
- **Latest photo**: The bottom-right thumbnail shows your latest shot with actual shutter, aperture, and ISO. Tap it to browse all shots from the current session and save originals or JPEGs to your phone.
- **Clean view**: Hides all controls except live view; tap the faint corner button to restore. **Lock**: Prevents accidental taps; long-press anywhere on screen to unlock.
- **Video recording**: Tap the record button at the top. Switches the camera into application mode before starting (required on Zf) and switches back when stopped; explains the reason if recording cannot start. Over USB, use [Video Monitor](#video-monitor-cine) for full video tools.
- **Preview snapshot**: Saves the live view frame to `Pictures/AeroCam/Snapshots/` (preview resolution).
- **USB remote shooting**: Smoother live view than Wi‑Fi (default 30 fps; adjustable to 60 fps or unlimited) with optional high-res preview and live fps readout at the bottom right. Configure under **Settings → Shooting**.
- Screen stays awake by default during remote shooting.

---

## Bluetooth Remote (Free)
No Wi‑Fi or live view required. Home → Bluetooth tile → **Bluetooth remote**. Requires [Bluetooth pairing](02-connect.md#pairing) first.
- Tap shutter for a single shot; press and hold shutter to use the camera's continuous drive (CL/CH).
- Hold AF and tap shutter for rapid shots, or use 3-shot / 5-shot burst buttons.
- AF button: hold to focus. Make sure half-press shutter AF is enabled on the camera (if you use back-button AF-ON, check your camera's Custom Settings).
- Includes self-timer countdown, video start/stop, and remaining shot count.
- **Interval timer** is Pro.

📷 Screenshot: Bluetooth remote screen

---

## Video Monitor (Cine)
Turns your phone into a dedicated video field monitor. Plug in USB and tap **🎥 Video monitor** on Home (smoothest, up to ~60 fps); a Wi‑Fi version is also available under the Wi‑Fi tile as an experimental feature.
- On the Zf, flip the Photo/Video selector to **Video**.
- **Top bar**: `● REC` timer, video resolution/frame rate (e.g., `1080 60p` — tap to change), file format (e.g., `H.265 10bit` — required for N‑Log), remaining recording time, and battery.
- **Bottom bar**: Video shutter speed, aperture, ISO, Auto ISO, EV, white balance, focus mode, and metering (video ISO is active in M mode).
- **Record button**: While recording, **press and hold for 1 second** (until the red ring completes) to stop, preventing accidental stops. Pressing Back while recording asks for confirmation first.
- **Monitoring tools**: Exposure meter, histogram, waveform / RGB parade, false color, zebra (including dual-threshold skin-tone zebra), focus peaking, grid lines, safe frames, aspect ratio mattes (`2.39:1`, `1.85:1`, `16:9`, `9:16`, `4:5`), red tally border, and shutter angle readout.
- **LUT** (Android 13+): Apply a monitoring LUT to the preview (built-in N‑Log to Rec.709, plus custom `.cube` import) without baking it into the recording. Turn off **View assist** on the camera so the LUT isn't applied twice.
- **Anamorphic desqueeze** (`1.33x`–`2.0x`), **A/B rack focus** (set two focus points and pull focus smoothly between them), and **Ghost overlay**.
- Tap-to-focus is disabled during recording by default to prevent accidental focus pulls, and can be enabled in the menu.
- **Screenshots**: "Preview snapshot" saves clean live view; "Snapshot (with aids)" burns in LUT, zebra, false color, and aspect mattes.

📷 Screenshot: Video monitor screen

---

## Night Mode (Free)
When shooting astrophotography, bright white screens ruin your dark adaptation. Night mode turns the entire app dark red.
1. Enable via **Settings → Appearance and language → Theme → "Night (red light)"**, or toggle "Night mode" in Remote's bottom toggles or **More → Aids**.
2. Need it even dimmer? Turn on **Minimum app screen brightness**.
3. Want to check true colors? **Press and hold "Hold for true color"** and release to return to red. Available in Remote, Video monitor, and the full-screen photo viewer.
4. Night mode affects only the screen display, never your photos. QR code sharing temporarily restores normal colors so other phones can scan the code.
