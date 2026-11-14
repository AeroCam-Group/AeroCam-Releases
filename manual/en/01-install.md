<!-- translated from zh-TW at commit 968641f -->

# 1. Install and Get Started

## Install
1. Download the latest Beta APK (`…-Beta-xx.xx.xx.apk`) from [Releases](https://github.com/AeroCam-Group/AeroCam-Releases/releases/latest).
2. Open the APK on your phone. The first time, Android asks you to allow "Install unknown apps" — allow it.
3. When a new version comes out, download and install it right over the old one. Your paired cameras and settings stay intact.

> Only download from AeroCam-Releases. APKs from other sources may have been modified. If you see "This is not an official version" when opening the app, someone has repackaged it: it will not accept test keys and may contain extra code. Uninstall it and download again from AeroCam-Releases.

> If you used an **older Beta before 92.03.09**: newer versions install as a separate app. Pair your camera and enter the test key again, then uninstall the old version once everything works.

📷 Screenshot: System prompt for "Install unknown apps"

## Permissions
The app only asks for a permission when you use a feature that needs it. You can deny anything you don't need:

| Permission | Purpose |
|---|---|
| Bluetooth, Nearby devices | Bluetooth pairing, Bluetooth photo transfer, Bluetooth remote; also needed on Android 13+ to find Wi‑Fi cameras |
| Location | Send phone location to the camera to embed in photos, or add location to received JPEGs; also required by Android to read Wi‑Fi network names |
| Notifications | Receive progress, incoming photos, transfer issues, low camera battery alerts |
| Photos and videos | Display and organize photos on your phone |

For full details on each permission, see [Privacy and Anonymous Statistics](10-privacy.md).

## Screen Tour
There are four tabs at the bottom:

| Tab | What's inside |
|---|---|
| **Home** | Camera dashboard (battery, lens, memory cards, connection status), four connection methods (Wi‑Fi, USB, Bluetooth, FTP), transfer status and history, camera styles, and manage cameras |
| **Camera roll** | Two sub-tabs: "Phone photos" and "Camera SD card" — see [Chapter 4](04-gallery.md) |
| **Remote** | View your camera's live view on your phone, adjust settings, and shoot photos or video — see [Chapter 5](05-remote.md) |
| **Settings** | Five categories — see [Chapter 7](07-settings.md) |

Not sure how to connect? Tap **ⓘ** next to the connection status on Home, or at the top right of any step in "Add camera", to open a step-by-step visual guide for that connection method.

📷 Screenshot: Home screen

## Test Key (Unlock Pro and Cine)
The Beta starts on the Free tier.
1. Copy the current test key from the [AeroCam-Releases home page](https://github.com/AeroCam-Group/AeroCam-Releases). In the app, go to **Settings → Support → "Get free key"** to open that page directly.
2. Go to **Settings → Support → "Enter test key"**, paste the full text, and tap "Apply". Tapping any locked feature also shows "Enter test key" in its dialog.
3. Each key is valid for 14 days and a new one is published every week. When yours expires, the app returns to the Free tier — just paste the new key.

> Both the Beta and test keys are **free**, and are only published on GitHub at AeroCam-Releases. If anyone asks you to pay for them, it is not an official channel.

## Check for Updates
The Beta checks automatically the first time you open it each day. You can also check manually under **Settings → Support → "Check for updates"**.

## Language
The interface supports Traditional Chinese, Simplified Chinese, Japanese, English, 한국어, Deutsch, Français, Español, Tiếng Việt, ไทย, and Bahasa Indonesia. By default it follows your phone's system language, or you can switch it under **Settings → Appearance and language → Language**.

English, Traditional Chinese, and Japanese are always 100% complete. New features in other languages may show English first and get translated in a later update. If you spot a bad translation, please let us know using the "Translation error" form in [Report a Problem](12-report.md).

## Anonymous Usage Statistics
The first time you connect to a camera, the app explains "Send anonymous usage statistics" once. You can choose "OK" or "Turn off" — nothing is sent before you answer. You can turn it off anytime under **Settings → Support**. To see exactly what is sent and what is never sent, read [Privacy and Anonymous Statistics](10-privacy.md).
