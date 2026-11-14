<!-- translated from zh-TW at commit 968641f -->

# 6. Photo Editing and Styles

## Photo Editor (Free)
Open any photo in **Phone photos** and tap **Edit**. There are three tabs at the bottom: **Crop**, **Adjust**, and **.np3**.

📷 Screenshot: Photo editor (Crop, Adjust, .np3)

### Crop
- Aspect ratios: Original, Free, 1:1, 4:5, 3:2, 16:9, plus cinema ratios 1.66, 1.85, 2, 2.20, and 2.39. Vertical photos automatically use portrait orientation.
- Drag inside the frame to move; drag any corner to resize.
- Straighten ±45° and rotate 90° counterclockwise (`↺`).

### Adjust
Pick a tool from the row to adjust with the precision ruler dial, then tap **Done** to return (adjusted tools show a small dot):
- **Light**: Exposure, Contrast, Highlights, Shadows, Whites, Blacks.
- **Color**: Temperature, Tint, Saturation, Vibrance.
- **Detail**: Clarity, Sharpness, Vignette.

Ruler dial: Snaps to whole steps (0.1 EV for Exposure, 1° for Straighten, 1 for others) with subtle haptic ticks. Press and hold either end to step continuously, tap the number to type a value directly, or double-tap / tap `↺` to reset to zero.

### Common Controls
- **↶ ↷** Undo / Redo.
- Press and hold **Original** to peek before your edits.
- **◧ Compare**: Split-screen slider comparing original and edited versions; pinch-to-zoom stays synchronized on both sides.
- Tap **Histogram** at the bottom right to expand the live histogram.

### Saving
- Camera originals (still on your memory card): **Saving replaces the copy on your phone.** AeroCam keeps a backup of the original for 7 days with a "Restore original" option in the viewer. If the camera isn't connected, it asks whether to "Replace" or "Save as copy".
- Phone-only photos (cardless captures, panoramas, Shake merges) are always saved as a new copy ending in `_E`.
- Preserves EXIF metadata at JPEG quality 95. If saving is interrupted, AeroCam finishes it automatically the next time you open the app.
- Filter by **Edited** in Phone photos to find edited images (marked with a small `✎` at the bottom left).
- Editing a compressed copy (`JPEG.S`) reminds you to edit the camera original instead for better quality.
- Videos cannot be edited.

---

## Edit RAW on Phone (Experimental)
NEF files open in the exact same editor and save alongside as `DSC_xxxx_E.JPG` (subsequent saves update that file). **The original NEF is never modified**, and EXIF metadata is preserved.
- **Lossless compressed NEF**: Developed directly on your phone using the camera's white balance.
- **High efficiency / High efficiency★ NEF**: This proprietary compression cannot be decoded on the phone, so AeroCam edits the full-size embedded JPEG inside the NEF instead. The top bar displays "Embedded JPEG 8 bit" and "Camera style applied: xxx".
- Files with only a tiny preview and no full-size JPEG cannot be edited (the app explains why).

### Phone-Editable RAW (Switch Camera RAW Compression)
To make future NEF shots developable directly on your phone, you can switch your camera to "Lossless compression" right from AeroCam:
- Access via "Shoot lossless RAW next time" on the editor's High Efficiency banner, or tap the image quality badge at the top right of the Memory cards card on Home (active whenever the camera is set to shoot RAW).
- Always asks for confirmation first, writes to the camera, reads back to verify, and shows the change in remaining shots (lossless files are larger, so remaining count drops slightly).
- AeroCam remembers your camera's previous setting so you can restore it later, and won't overwrite it if you already changed it on the camera.

---

## .np3 Style Preview (Free)
Under the **.np3** tab in the editor, apply Nikon Picture Control files (`.np3`, `.ncp`) to preview how they look on your phone.
- Tap any style to apply it, adjust strength from 0–100%, and fine-tune further in **Adjust**.
- Swipe left/right on the photo to cycle styles, or press and hold to view the original. Quick filters for `★` Favorites and Recent appear below.
- Tap **All N ▴** to expand the full Style library (see below) with search and filters.
- Simulates tone curves and saturation: files with custom curves use their embedded curve, while files built with Flexible Color sliders ("Slider tone") are converted to curves based on NX Studio measurements. **Color Blender and Color Grading are not simulated yet**, so results are an approximation.
- Works best on NEF files. If a JPEG already had a Picture Control baked in at capture, the effect stacks (the app warns you).

📷 Screenshot: .np3 tab in editor

---

## Camera Styles C1–C9 (Pro)
Manage custom Picture Control slots C1–C9 on your camera from your phone. Tap the **Camera styles** card on Home (requires Wi‑Fi or USB connection).
- Each slot shows a preview, name, and badges for active status, custom curve, or Flexible Color.
- **Tap a slot** to pick a style from your library and write it to the camera. AeroCam reads it back to verify and shows `✓` only when matched. **Long-press** or tap `⋮` to clear a slot. If a photo is currently transferring, writing waits until that file finishes.
- The camera is only queried when you open this screen, tap `↻`, write, or clear; Home shows the last read values and timestamp.
- Below C1–C9, the 9 Nikon Imaging Cloud recipes are listed read-only (add those via Nikon Imaging Cloud).

### What Gets Written to the Camera
Custom camera slots accept a **base Picture Control + adjustment sliders**, not a raw `.np3` file:
- Tap **+ New style** in the library to pick a base (Standard, Flat, Creative Picture Control…) and set Sharpening, Clarity, Contrast, Brightness, Saturation, and Hue.
- **Writing `.np3` / `.ncp` to the camera (approximate)**: Files with curves — as well as "Slider tone" files converted to curves — write **Name + Curve + Sharpening (Sharpening, Mid-range sharpening, Clarity)** into a C slot using your chosen base. **Saturation, Color Blender, and Color Grading cannot be written over the connection**; AeroCam lists all values in the file and clearly marks what won't transfer before writing.
- For full fidelity, copy the `.np3` to a memory card and import it via the camera menu.

### Style Library
- Holds up to 256 styles (`.np3` and `.ncp`).
- Search bar `🔍`, filter chips (All, `★`, Recent, With curve, On camera, Writable), and **+ New**.
- Each style displays a preview thumbnail using your own imported reference photo (`+ → "Preview reference photo…"`), or a color swatch chart until you import one.

📷 Screenshot: Camera styles C1–C9 and Style library

---

## Image Processing: Panorama Stitching and Noise-Reduction Merge (Pro)
Select multiple photos in **Phone photos** and **swipe up** the bottom action bar (or tap its handle) to open "Image processing".

### Stitch (Panorama)
- Selecting inside a "Panorama" stack stitches frames according to their captured grid positions and saves the result back into that stack labeled "Panorama".
- Selecting any overlapping photos in the regular gallery lets AeroCam automatically detect how they connect and saves the result as a new stack.
- Unmatched photos won't fail the whole batch: AeroCam stitches the largest connected group and lists any skipped file names. Grid panoramas require every tile to be present so the output has no holes.
- A full 360° sweep exports a 360° panorama. Results are automatically leveled using recorded camera level data, ghost-free, and keep EXIF metadata.
- See [Chapter 5 Panorama](05-remote.md#panorama-stitching) for shooting instructions.

### Noise-Reduction Merge (Shake)
- Aligns and averages selected frames to reduce noise while preserving detail; moving areas use a single frame to avoid ghosting.
- Selecting inside a "Shake" stack saves the merged result back into that stack (labeled "Merged"), or you can tap **Merge** / **Re-merge** above the stack.
- See [Chapter 5 Shake](05-remote.md#shake-noise-reduction-merge) for shooting instructions.

> Only one stitch or merge job runs at a time. Progress appears on screen, and you can tap the banner to open the result when finished.
