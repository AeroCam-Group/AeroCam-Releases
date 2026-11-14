# Translating the AeroCam manual

Source: `manual/zh-TW/` (Traditional Chinese). It is the only version that is edited first; every other language is translated from it.

## Target folders
`manual/en/`, `manual/zh-CN/`, `manual/ja/`, `manual/ko/`, `manual/de/`, `manual/fr/`, `manual/es/`, `manual/vi/`, `manual/th/`, `manual/id/`.
Use exactly the same file names as `zh-TW` (`README.md`, `01-install.md` … `12-report.md`). Do not translate `screenshots.md` (it is a to-do list for the owner).

## Rules
1. **First line of every file**, as an HTML comment: `<!-- translated from zh-TW at commit <short hash> -->`. This tells us which translations are out of date.
2. Translate the meaning in plain, short sentences. Keep the structure: same headings, same tables, same order.
3. **Keep unchanged**: file names, paths (`Pictures/AeroCam`), file names in examples (`DSC_1234_S.JPG`), numbers, port `2121`, user name `aerocam`, URLs, email, the 📷 lines' file meaning.
4. **Links between chapters**: keep the file part (`02-connect.md`), but **rewrite the `#anchor` part** to match the translated heading (GitHub builds anchors from the heading text). Check every link after translating.
5. **Camera menu names**: use the **official Nikon menu wording in that language** as shown on the camera / in Nikon's reference manual for that language (e.g. "Connect to PC", "Connection type", "Image transfer", "Camera control", "Connect to smart device", "Send while off", "Picture Control", "Release locked when slot empty"). When unsure, keep the English Nikon term in parentheses.
6. **App screen names**: use the wording of AeroCam's own interface in that language (the app's `values-<lang>/strings.xml`), so the manual matches what users see.
7. Keep product terms as they are: AeroCam, Pro, Cine, Beta, RAW, JPEG, JPEG.S, NEF, .np3, .ncp, LUT, N‑Log, FTP, USB‑C, Wi‑Fi, SnapBridge, NX Studio, Nikon Imaging Cloud, LibRaw.
8. Keep the disclaimer meaning exactly: AeroCam is an independent third‑party app, not affiliated with or authorised by Nikon or any other camera maker.
9. Privacy chapter (`10-privacy.md`): translate precisely, do not add or remove items from the "sent" / "never sent" lists.
10. After a language is done, update `manual/README.md` (language table) and the matching `readme/README.<lang>.md` link to point to `manual/<lang>/README.md`.

## Key terms (zh-TW → meaning)
| zh-TW | Meaning |
|---|---|
| 相機相簿／相機記憶卡 | Browsing the camera's memory card from the phone |
| 手機相簿 | Photos already saved on the phone |
| 自動接收 | Auto receive (camera sends, phone saves) |
| 一鍵連線 | One‑tap connect (phone joins the camera's own Wi‑Fi via Bluetooth) |
| 手機熱點／同一個 Wi‑Fi | Phone hotspot / same Wi‑Fi network |
| 遠端拍攝 | Remote shooting (live view over Wi‑Fi/USB) |
| 藍牙遙控 | Bluetooth remote (no live view) |
| 錄影監控 | Video monitor |
| 拍攝方式 | Shooting method |
| 間隔定時拍攝 | Interval timer shooting (Nikon term) |
| 對焦位移拍攝 | Focus shift shooting (Nikon term) |
| 包圍曝光 | Exposure bracketing |
| 拼貼／拼接 | Panorama shooting / stitching |
| 搖搖樂（降噪合成） | "Shake" multi‑shot noise‑reduction merge (keep a short, friendly name) |
| 疊影比對 | Ghost overlay |
| 優化校準 | Picture Control (Nikon term) |
| 相機風格 C1～C9 | Custom Picture Controls C1–C9 on the camera |
| 風格庫 | Style library |
| 滑桿色調 | Slider tone (Flexible Color sliders) |
| 彈性色彩 | Flexible Color (Nikon term) |
| 無卡拍照／只存手機 | Shooting without a card / save to phone only |
| 存檔位置 | Save destination |
| 照片位置 | Photo location (GPS) |
| 測試金鑰 | Test key |
| 匿名使用統計 | Anonymous usage statistics |
| 診斷資訊 | Diagnostic info |
| 星空模式 | Night (red light) mode |
