<!-- translated from zh-TW at commit 968641f -->

# 2. Kết nối máy ảnh

AeroCam hỗ trợ bốn phương thức kết nối. Bạn có thể thiết lập đồng thời nhiều cách, ứng dụng sẽ tự động dùng phương thức đang khả dụng. Bốn ô trên Trang chủ (Wi‑Fi, USB, Bluetooth, FTP) hiển thị trạng thái của từng kết nối.

> Chưa rõ cách kết nối? Nhấn **ⓘ** cạnh trạng thái kết nối ở Trang chủ, hoặc góc trên bên phải mỗi bước trong «Thêm máy ảnh» để mở hướng dẫn từng bước có ảnh minh họa (mỗi phương thức một trang: điểm phát sóng di động, cùng mạng Wi‑Fi, kết nối một chạm, USB, Bluetooth, FTP), có đủ ảnh chụp màn hình điện thoại lẫn máy ảnh và mục «Kiểm tra khi không kết nối được» ở cuối.

## Cách chọn phương thức phù hợp

| Nhu cầu của bạn | Gợi ý |
|---|---|
| Nhận ảnh ngay cả khi đã tắt máy ảnh, không cần thao tác nhiều | **Bluetooth** (ảnh JPEG thu nhỏ, miễn phí) |
| Chụp ngoài trời, không muốn bật điểm phát sóng, cần ảnh gốc, duyệt thẻ, chụp từ xa | **Kết nối một chạm** (Pro) |
| Chụp xong tự động đẩy ngay sang điện thoại, tốc độ không dây nhanh nhất | **[Nhận ảnh qua FTP](08-ftp.md)** (Pro, cần bật điểm phát sóng) |
| Ổn định nhất, giám sát quay phim, chụp từ xa thời gian dài | **Cáp USB** (chọn và tải thủ công miễn phí) |
| Ở nhà hoặc trong studio | **Cùng mạng Wi‑Fi** (Pro) |

## Tốc độ tham khảo (thử nghiệm thực tế trên Nikon Zf và Pixel 10 Pro)

| Phương thức | Một tệp RAW (khoảng 18 MB) |
|---|---|
| Nhận qua FTP | Khoảng 1 giây (khoảng 17 MB/s) |
| Tải từ thư viện Wi‑Fi | Khoảng 1,3 giây (khoảng 13 MB/s) |
| USB | Thường nhanh hơn Wi‑Fi, tùy loại cáp (cáp USB 2.0 đạt khoảng 35 MB/s) |
| Bluetooth | Ảnh JPEG thu nhỏ (khoảng 2 MB), mỗi ảnh mất 15–20 giây |

## Đèn báo trạng thái kết nối trên Trang chủ
Bốn nút Wi‑Fi, USB, Bluetooth và FTP đổi màu theo trạng thái, màu xám khi chưa kết nối:

| Màu sắc | Ý nghĩa |
|---|---|
| 🟢 Xanh lá | Đã kết nối hoặc sẵn sàng (Bluetooth xanh nhạt = đang chờ, sẵn sàng gửi khi tắt máy) |
| 🔵 Xanh dương | Đang truyền dữ liệu |
| 🟠 Cam | Đang kết nối (nhấp nháy), hoặc cần xử lý (thiếu quyền, bị treo, lỗi) |
| 🔴 Đỏ | Wi‑Fi hoặc Bluetooth trên điện thoại đang tắt |

---

## Bluetooth (miễn phí, thay thế SnapBridge)

### Ghép nối
1. Trên máy ảnh: **MENU → Menu mạng (Network menu) → Kết nối với thiết bị thông minh (Connect to smart device) → Ghép nối (Bluetooth) (Pairing (Bluetooth)) → Bắt đầu ghép nối (Start pairing)**.
2. Nếu máy ảnh từng ghép nối với SnapBridge, hãy xóa ghép nối trong SnapBridge trước và hủy ghép nối trong danh sách Bluetooth của điện thoại (hai ứng dụng không thể ghép nối cùng lúc với một máy ảnh).
3. Trong AeroCam: Trang chủ «Bluetooth» → **Ghép nối máy ảnh** → Bắt đầu. Điện thoại và máy ảnh sẽ hiện cùng một dãy số, hãy xác nhận trên cả hai thiết bị. Trên máy ảnh sẽ hiển thị tên `AeroCam_<tên mẫu điện thoại>`.

📷 Ảnh chụp màn hình: thẻ Bluetooth

### Sau khi ghép nối
Sau khi ghép nối, tính năng này luôn bật cho đến khi bạn hủy ghép nối (có hộp thoại xác nhận).
- Bình thường AeroCam chỉ **lắng nghe** tín hiệu Bluetooth ở chế độ nền, không đánh thức máy ảnh đang ngủ.
- **Khi bật máy ảnh**: kết nối một lần để đồng bộ giờ và vị trí GPS của điện thoại (giúp máy ảnh ghi vị trí vào ảnh khi chụp), sau đó tự ngắt.
- **Khi máy ảnh có ảnh cần gửi**: bật mục **Gửi khi tắt máy** (Send while off) trong menu «Connect to smart device» của máy ảnh; máy ảnh sẽ tự dùng Bluetooth gửi ảnh sang điện thoại kể cả khi đã tắt nguồn.
- Ảnh nhận được là tệp JPEG khoảng 2 MB do máy ảnh tạo ra (chụp RAW cũng được máy ảnh chuyển sang JPEG trước), mất khoảng 15–20 giây mỗi ảnh. Muốn lấy tệp gốc hãy dùng Wi‑Fi, USB hoặc FTP.
- Muốn nhận ngay lập tức, nhấn **Nhận ngay** trên thẻ Bluetooth.
- Khi bật/tắt Bluetooth điện thoại, khởi động lại điện thoại hoặc cập nhật ứng dụng, dịch vụ sẽ tự khôi phục. Trong lúc chờ, thanh thông báo sẽ có một thông báo thường trực mức ưu tiên thấp (theo quy định của Android), bạn có thể ẩn đi trong cài đặt hệ thống.

### Trạng thái trên thẻ Bluetooth
🟢 Máy ảnh ở gần · Đang bật / 🟢 Xanh nhạt: Chờ (sẵn sàng gửi khi tắt máy) / ⚪ Không thấy máy ảnh (hiển thị lần cuối nhìn thấy) / 🔵 Đang truyền / 🟠 Có vẻ bị treo / 🔴 Bluetooth điện thoại đang tắt.

Bluetooth không duy trì kết nối liên tục nên khu vực này hiển thị trạng thái «có nghe thấy tín hiệu máy ảnh không» và «đang làm gì».

### Khi bị treo kết nối
- Nếu đang truyền mà 30 giây không có dữ liệu, ứng dụng sẽ tự ngắt kết nối và máy ảnh sẽ gửi lại sau; nếu 20 giây không có tiến triển, thẻ sẽ chuyển màu vàng báo «Có vẻ bị treo».
- **Ngắt và kết nối lại**: chỉ ngắt phiên truyền hiện tại.
- **⋮ → Khởi động lại dịch vụ Bluetooth**: khởi động lại toàn bộ dịch vụ nền Bluetooth nhưng vẫn giữ nguyên ghép nối.
- Khi chụp RAW, máy ảnh phải chuyển đổi sang JPEG trước khi gửi; thao tác trên máy ảnh lúc đang truyền (nhấn nửa cò, chụp ảnh) sẽ khiến máy ảnh hủy truyền. Tốt nhất bạn nên chụp xong rồi tắt máy để máy tự gửi ngầm.

---

## Wi‑Fi (Pro): ba phương thức

| Phương thức | Cách hoạt động | Khi nào nên dùng |
|---|---|---|
| **Kết nối một chạm** (khuyên dùng) | Dùng Bluetooth ra lệnh cho máy ảnh tự phát Wi‑Fi, điện thoại tự động kết nối vào | Ngoài trời, không muốn bật điểm phát sóng |
| **Điểm phát sóng di động** (khuyên dùng trong hướng dẫn) | Máy ảnh kết nối vào điểm phát sóng (hotspot) của điện thoại | Khi kết nối một chạm không ổn định, hoặc khi cần dùng FTP hay chụp không thẻ nhớ |
| **Cùng mạng Wi‑Fi** | Điện thoại và máy ảnh cùng kết nối vào một bộ phát Wi‑Fi (router) | Ở nhà hoặc trong studio |

### Kết nối một chạm
1. Hoàn tất **ghép nối Bluetooth** trước.
2. Trang chủ Wi‑Fi → «Kết nối một chạm».
3. Lần đầu tiên cần nhập **mật khẩu** Wi‑Fi của máy ảnh (tên mạng được ứng dụng tự điền, dạng `NIKON_…`), mật khẩu chỉ lưu trên điện thoại của bạn.
4. Khi Android hỏi có cho phép kết nối mạng Wi‑Fi không, hãy chọn Cho phép.
5. Khi hiện «Đã kết nối Wi‑Fi máy ảnh», việc duyệt thẻ, chụp từ xa và nhận tự động đều đi qua kết nối này. Nhấn «Ngắt kết nối» để quay về mạng Wi‑Fi ban đầu.

Khi duyệt thẻ hoặc chụp từ xa chưa kết nối, trên màn hình cũng hiện sẵn nút «Kết nối bằng Wi‑Fi của máy ảnh».

> - Khi đang nối Wi‑Fi của máy ảnh, điện thoại sẽ dùng dữ liệu di động (4G/5G) để truy cập Internet.
> - Kết nối một chạm **không dùng chung được với FTP**, và cũng **không hỗ trợ chụp không thẻ nhớ** (khi máy ảnh không lắp thẻ nhớ, hãy dùng điểm phát sóng di động hoặc cùng mạng Wi‑Fi).

📷 Ảnh chụp màn hình: thẻ kết nối một chạm và trạng thái đã kết nối

### Điểm phát sóng di động / Cùng mạng Wi‑Fi (ghép nối lần đầu)
1. Trên máy ảnh: **MENU → Menu mạng (Network menu) → Kết nối với máy tính (Connect to PC)**, tạo hồ sơ mạng (kết nối vào điểm phát sóng của điện thoại hoặc Wi‑Fi nhà bạn).
   - Các dòng máy mới (có mục «Connection type» trong menu): chọn **Connection type (Loại kết nối)** là **Image transfer (Truyền hình ảnh)**.
   - Các dòng máy cũ hơn: chỉ cần chọn **Connect to PC**.
2. Trên AeroCam: **Trang chủ → «＋» Thêm máy ảnh**, chọn phương thức kết nối (Cùng mạng Wi‑Fi hoặc Điểm phát sóng di động). Ứng dụng sẽ kiểm tra mạng và tự tìm máy ảnh; nếu không thấy có thể nhập thủ công địa chỉ IP.
3. Màn hình máy ảnh hiện **mã xác nhận 4 chữ số**, hãy nhập mã này trên điện thoại rồi nhấn OK trên máy ảnh.
4. Hoàn tất sẽ lưu thành một «Hồ sơ máy ảnh», những lần sau mở ứng dụng là kết nối trực tiếp được ngay. Bạn có thể lưu nhiều máy ảnh, nhiều mạng; sau khi cập nhật ứng dụng **không cần ghép nối lại**; ngay cả khi máy ảnh đổi địa chỉ IP ứng dụng vẫn tự tìm ra.

> Nếu máy ảnh báo «Đã ghép nối với thiết bị khác», nghĩa là cấu hình mạng đó trên máy ảnh đang dùng cho ứng dụng khác. Hãy tạo một hồ sơ mới trên máy ảnh rồi ghép nối lại.

📷 Ảnh chụp màn hình: trình hướng dẫn thêm máy ảnh và màn hình nhập mã PIN

### Kiểm tra trước khi kết nối
- Khi nhấn «Bắt đầu nhận», hoặc vào Thư viện / Chụp từ xa, ứng dụng sẽ kiểm tra mạng trước. Nếu hồ sơ là «Điểm phát sóng di động» nhưng bạn chưa bật phát sóng, hoặc «Cùng mạng Wi‑Fi» nhưng điện thoại chưa vào mạng đó, màn hình sẽ hiện khung cảnh báo màu vàng (ví dụ «Vui lòng bật điểm phát sóng di động trước») kèm nút tắt «Cài đặt điểm phát sóng» và «Cài đặt Wi‑Fi». Bật xong quay lại AeroCam, khung vàng sẽ tự biến mất.
- Khi không tìm thấy máy ảnh trên cả Wi‑Fi lẫn điểm phát sóng, Trang chủ sẽ báo «Không tìm thấy máy ảnh trên mạng», phần lớn do mục «Connect to PC» trên máy ảnh chưa bật; bên cạnh có nút «Xem hướng dẫn kết nối».

### Mục «Connection type» (Loại kết nối) trên máy ảnh
Các dòng máy mới (Z9, Z8, Z6III, Zf, Z5II, Z50II…): **MENU → Menu mạng (Network menu) → Connect to PC → Connection type**
- **Image transfer** (Truyền hình ảnh): dùng cho tự động nhận ảnh và duyệt thẻ nhớ máy ảnh.
- **Camera control** (Điều khiển máy ảnh): dùng cho chụp từ xa và chụp không thẻ nhớ.

Sau khi chuyển đổi, Wi‑Fi của máy ảnh sẽ ngắt một lát rồi AeroCam tự động kết nối lại, không cần ghép nối lại. Nếu vào Chụp từ xa khi máy ảnh vẫn đang ở «Image transfer», ứng dụng sẽ hiển thị các bước hướng dẫn chuyển đổi.

---

## Cáp USB
Nhanh và ổn định hơn Wi‑Fi, **không cần ghép nối** và không cần thêm máy ảnh trước.
1. Đặt tùy chọn USB trên máy ảnh thành **MTP/PTP** (không chọn «iPhone» hay «UVC/UAC»).
2. Dùng cáp USB‑C **có hỗ trợ truyền dữ liệu** (một số cáp chỉ sạc được). Cáp USB 3 ghi chuẩn 5Gbps / 10Gbps sẽ cho tốc độ cao hơn.
3. Trên Trang chủ, thẻ USB hiện «Đã phát hiện Z f · Cần cấp quyền truy cập» → nhấn «Cho phép truy cập» và xác nhận hộp thoại của Android một lần.

### Màu sắc của thẻ USB
| Màu sắc | Ý nghĩa |
|---|---|
| ⚪ Xám | Không có máy ảnh (hoặc cáp chỉ hỗ trợ sạc) |
| 🟠 Cam | Đã phát hiện máy ảnh, cần cấp quyền truy cập |
| 🔴 Đỏ | Cài đặt USB không phải MTP/PTP, chưa cấp quyền hoặc kiểm tra thất bại (có hiển thị lý do) |
| 🟢 Xanh lá | Đã kết nối qua cáp USB |

### Khi đang cắm cáp
- Thư viện ảnh, Chụp từ xa và Tự động nhận đều **tự động chuyển sang đường truyền USB**; rút cáp sẽ tự động quay về Wi‑Fi. Ngay cả khi đang chụp từ xa qua Wi‑Fi mà cắm cáp vào cũng tự chuyển sang USB (trừ lúc đang chạy chụp giãn cách, chụp bù trừ phơi sáng hoặc phơi sáng Bulb).
- **Nhận qua USB** (Pro): nhấn «Bắt đầu nhận» trên thẻ USB để lưu ảnh mới chụp và ảnh chọn «Send to PC» trên máy ảnh sang điện thoại. Mặc định cắm cáp là tự động bắt đầu nhận (**Cài đặt → Chụp ảnh → «Tự động bắt đầu nhận khi cắm cáp USB»**).
- **Đồng bộ thời gian**: tự đồng bộ giờ máy ảnh một lần khi cắm cáp (chỉ chỉnh khi lệch quá 2 giây; nếu lệch trên 1 ngày sẽ hỏi trước).
- **Giữ máy thức**: khi đang mở Thư viện hoặc Chụp từ xa, cứ 10 giây ứng dụng gửi một tín hiệu nhỏ để máy ảnh không ngủ; tự dừng sau 30 phút không thao tác hoặc khi máy ảnh yếu pin.
- Điện thoại có thể đang cấp nguồn sạc ngược cho máy ảnh, nếu dùng lâu bạn nên cắm thêm pin dự phòng.
- **Kiểm tra USB** (dấu ⋮ góc trên bên phải thẻ USB): kiểm tra kết nối, thông tin máy ảnh, thẻ nhớ, tốc độ khung hình xem trước và tốc độ đọc.

📷 Ảnh chụp màn hình: thẻ USB

---

## FTP
Máy ảnh chụp xong tự động đẩy ảnh sang điện thoại, xem chi tiết tại [Chương 8](08-ftp.md).
