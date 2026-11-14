<!-- translated from zh-TW at commit 968641f -->

# 7. Settings Reference

**Settings** is organized into five categories. Options not available on the Free tier are hidden. Have a suggestion or think a default should change? Let us know via [Report a Problem](12-report.md).

## Receive & Notifications

### Receive
| Setting | Options | Default | Details |
|---|---|---|---|
| File types to receive | All files / JPEG only / JPG + RAW / Photos + videos / Custom; plus Save JPEG only from RAW, Save compressed JPEG, Replace compressed copy when original arrives (Pro) | All files | See [Chapter 3](03-receive.md#file-types-to-receive) |
| Save folder | By camera / By date / By camera and date / By file type | By camera and date | Subfolder structure under `Pictures/AeroCam` and `Movies/AeroCam` |
| File naming | Original camera name / Date prefix / Date & time prefix | Original camera name | Applies to future files only; duplicate detection still uses the original camera name |
| Receive mode (Pro) | Continuous / Single file | Continuous | Single file stops after receiving one file |
| Skip large videos (Pro) | Size in MB | 1024 MB | Larger videos are logged as "Filtered" for manual download |
| Wi‑Fi search timeout | 30 sec / 1 / 2 / 3 / 5 / 10 min / Unlimited | 3 min | Stops auto receive after timeout so it doesn't keep retrying and draining battery |
| FTP idle auto-stop | Never / 5 / 10 / 30 min | Never | Counts from the last received photo; never stops mid-transfer |
| Photos already received via Bluetooth | Replace with original when received over Wi‑Fi / Do not download again over Wi‑Fi / Keep both copies | Replace with original | Bluetooth receives a ~2 MB smaller copy |

### Photo Location
| Setting | Default | Details |
|---|---|---|
| Send location to camera (Bluetooth) | On | Sends phone GPS to the camera on power-on or Bluetooth transfer so the camera embeds it |
| Add location to received JPEGs (phone) | Off (asks on first receive) | Embeds phone location by capture time into JPEGs received via Wi‑Fi, USB, or FTP; RAW files are untouched |

See [Chapter 3 Photo Location](03-receive.md#photo-location-gps) for details.

### Gallery
| Setting | Options | Default | Details |
|---|---|---|---|
| Compressed JPEG quality (Pro) | 60 / 70 / 80 / 90% | 80% | Quality for JPEGs recompressed on your phone (~3–4 MB at 24 MP) |
| Selection after download/delete | Ask every time / Always keep / Always clear | Ask every time | Helps prevent accidentally tapping "Delete from camera" |
| Prompt countdown | 3 / 5 / 8 / 10 sec | 5 sec | Clears selection automatically if unanswered when "Ask every time" is chosen |
| QR code share auto-stop | 15 / 30 / 60 min | 30 min | Link expires automatically after this duration |

### Notifications
| Setting | Default | Details |
|---|---|---|
| Do Not Disturb | Off | Mutes all AeroCam notifications (the ongoing "Receiving" notification remains as required by Android) |
| Transfer started | Off | |
| Photo received | On | |
| Transfer issues | On | Stalled transfer, canceled by camera, or low phone storage |
| Hide ongoing notification | — | Opens Android's notification settings so you can hide it while keeping receive running |
| Low camera battery alert | On, 15% | Threshold options: 10 / 15 / 20 / 30%; checked while connected to the camera |

## Shooting

### Save Destination
| Setting | Options | Details |
|---|---|---|
| Save destination | Memory card / Card + phone (Pro) | Used when a memory card is inserted; switches automatically to Phone only when no card is inserted (Pro). Shows current card status when connected. See [Chapter 3](03-receive.md#save-destination-and-shooting-without-a-card) |

### Remote Shooting
| Setting | Options | Default | Details |
|---|---|---|---|
| Enabled by default in Remote | Focus before shooting, Histogram, Overexposure warning, Focus peaking, Exposure meter | Focus before shooting, Exposure meter | Can still be toggled anytime while shooting |
| Exposure meter color | Auto / White / Black | Auto | Auto adapts to background brightness |
| Focus peaking color | Red / Yellow / Blue / White | Red | Switch colors when shooting red subjects |
| Keep screen on during Remote | On / Off | On | Prevents screen sleep during interval or long-exposure shoots |
| Left-handed mode | On / Off | Off | Moves shutter button to bottom left in landscape |

### Wired Connection (USB‑C)
| Setting | Options | Default | Details |
|---|---|---|---|
| USB live view frame rate | 30 / 60 fps / Unlimited | 30 fps | 30 fps saves battery and runs cooler; 60 fps is smoother |
| USB high-res live view | On / Off | On | Sharper preview with slightly lower fps; falls back automatically if unsupported |
| Auto-start receiving when USB cable is plugged in (Pro) | On / Off | On | Starts USB receive automatically on plug-in |
| Sync camera clock on connect | On / Off | On | Adjusts only if off by >2 sec; asks first if off by >1 day |
| Keep camera awake over USB | On / Off | On | Sends a tiny keep-alive every 10 sec; stops after 30 min idle or low battery |

## Appearance and Language
| Setting | Options | Default |
|---|---|---|
| Theme | Follow system / Light / Dark / Night (red light) | Follow system |
| Minimum app screen brightness | On / Off (in Night mode) | Off |
| Language | Follow system / 繁中 / 简中 / 日本語 / English / 한국어 / Deutsch / Français / Español / Tiếng Việt / ไทย / Bahasa Indonesia | Follow system |

## Storage & Battery
| Item | Details |
|---|---|
| Thumbnail cache | Shows cache size with a clear button (regenerated from camera as needed) |
| Incomplete download temp files | Shows size with a clear button |
| Rescan phone photos | Finds photos restored to your phone (e.g., from Trash or saved before reinstalling) |
| Battery optimization | Recommended to disable (shows "Not optimized ✓") so background transfers aren't killed |

## Support
| Item | Details |
|---|---|
| Copy diagnostic info | Paste when reporting an issue: app version, phone & network status, camera capabilities, recent command log, and last crash trace. Only the last 4 digits of the camera serial number are included |
| Clear logs | Deletes current and previous session logs and crash records |
| Check for updates | Manually checks for a newer release; shows current version below |
| Test key | "Get free key" opens AeroCam-Releases; "Enter test key" lets you paste it; shows current tier and expiry date |
| Open-source licenses | Third-party libraries used (such as LibRaw for RAW development) |
| Send anonymous usage statistics | Single toggle, on by default. See [Privacy and Anonymous Statistics](10-privacy.md) |
