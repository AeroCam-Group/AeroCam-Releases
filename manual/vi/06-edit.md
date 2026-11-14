<!-- translated from zh-TW at commit 968641f -->

# 6. Chỉnh sửa ảnh và phong cách màu

## Chỉnh sửa ảnh (miễn phí)
Mở ảnh lớn trong «Ảnh trên điện thoại» → **Chỉnh sửa**. Bên dưới có ba thẻ: **Cắt**, **Điều chỉnh**, **.np3**.

📷 Ảnh chụp màn hình: trình chỉnh sửa (Cắt, Điều chỉnh, .np3)

### Cắt
- Tỷ lệ: Gốc, Tự do, 1:1, 4:5, 3:2, 16:9 và các tỷ lệ điện ảnh 1.66, 1.85, 2, 2.20, 2.39. Ảnh chụp dọc tự động dùng khung dọc.
- Kéo khung cắt để di chuyển, kéo bốn góc để đổi kích thước.
- Căn thẳng đường chân trời ±45°, ↺ xoay 90°.

### Điều chỉnh
Một hàng công cụ, nhấn vào một mục để chỉnh bằng thước chia độ, nhấn «Xong» để quay lại thanh công cụ; những mục đã chỉnh sẽ có dấu chấm nhỏ:
- **Ánh sáng**: Phơi sáng, Tương phản, Vùng sáng, Vùng tối, Điểm trắng, Điểm đen.
- **Màu sắc**: Nhiệt độ màu, Sắc thái, Độ bão hòa, Độ tươi màu.
- **Chi tiết**: Độ trong trẻo, Độ sắc nét, Tối góc.

Thước chia độ: khi kéo chỉ dừng ở từng nấc nguyên (phơi sáng 0,1 EV, căn thẳng 1°, các mục khác 1 đơn vị), mỗi nấc rung nhẹ phản hồi; nhấn giữ hai đầu để tăng giảm liên tục; nhấn vào con số để nhập trực tiếp; chạm đúp hoặc nhấn `↺` để đưa về 0.

### Thao tác chung
- **↶ ↷** Hoàn tác / Làm lại.
- Nhấn giữ **Ảnh gốc** để xem trước khi chỉnh sửa.
- **◧ Đối chiếu**: dùng đường chia trái phải để so sánh ảnh gốc và ảnh đã chỉnh, khi phóng to bằng hai ngón tay cả hai bên cùng phóng đồng bộ.
- Góc dưới bên phải có thể mở rộng «Biểu đồ sáng».

### Lưu ảnh
- Ảnh gốc từ máy ảnh (vẫn còn trên thẻ nhớ): **lưu lại sẽ thay thế bản trên điện thoại**, ứng dụng lưu dự phòng bản gốc trong 7 ngày, trong thời gian này màn hình xem ảnh lớn có nút «Khôi phục ảnh gốc». Khi không kết nối máy ảnh sẽ hỏi trước muốn «Thay thế» hay «Lưu thành bản sao».
- Ảnh chỉ có trên điện thoại (chụp không thẻ, ảnh ghép toàn cảnh, thành phẩm Shake) luôn lưu thành tệp mới, tên tệp thêm hậu tố `_E`.
- Khi lưu giữ nguyên thông số chụp (EXIF), chất lượng JPEG 95. Nếu đang lưu mà bị gián đoạn, lần sau mở ứng dụng sẽ tự hoàn tất.
- Mục lọc **Đã chỉnh sửa** trên thanh lọc «Ảnh trên điện thoại» liệt kê các ảnh đã qua chỉnh sửa, góc dưới bên trái ảnh thu nhỏ có biểu tượng `✎` nhỏ.
- Khi chỉnh sửa bản nén (`JPEG.S`), ứng dụng sẽ nhắc bạn nên chỉnh trên ảnh gốc của máy ảnh để đạt chất lượng tốt hơn.
- Không hỗ trợ chỉnh sửa video.

---

## Chỉnh sửa RAW trên điện thoại (thử nghiệm)
Tệp NEF cũng dùng được trình chỉnh sửa này và lưu thành tệp `DSC_xxxx_E.JPG` nằm ngay bên cạnh (lưu lại sẽ cập nhật chính tệp đó), **tệp NEF gốc không bao giờ bị sửa đổi**, thông số chụp được giữ nguyên.
- **NEF nén không mất dữ liệu (Lossless compressed)**: giải mã trực tiếp trên điện thoại (dùng cân bằng trắng của máy ảnh).
- **NEF Hiệu suất cao / Hiệu suất cao★ (High efficiency / High efficiency★)**: định dạng nén này điện thoại chưa tự giải mã được nên sẽ dùng ảnh JPEG kích thước đầy đủ nhúng sẵn bên trong NEF để chỉnh sửa. Phía trên trình chỉnh sửa sẽ hiện «JPEG nhúng 8 bit» và «Đã áp phong cách máy ảnh: xxx».
- Những tệp chỉ có ảnh xem trước nhỏ, không có JPEG kích thước đầy đủ sẽ không chỉnh sửa được và có thông báo lý do.

### RAW chỉnh sửa được trên điện thoại (chuyển chuẩn nén RAW của máy ảnh)
Nếu muốn các tệp NEF chụp sau này đều giải mã trực tiếp được trên điện thoại, bạn có thể chuyển máy ảnh sang «Nén không mất dữ liệu» ngay từ điện thoại:
- Lối vào: nút «Chụp RAW không mất dữ liệu từ lần sau» trên thanh thông báo High efficiency của trình chỉnh sửa, hoặc nhấn vào nhãn chất lượng ở góc trên bên phải thẻ nhớ tại Trang chủ (chỉ nhấn được khi máy ảnh đang đặt chụp RAW).
- Luôn hỏi xác nhận trước; ghi vào máy ảnh xong sẽ đọc lại để kiểm tra, thành công sẽ báo sự thay đổi số ảnh còn chụp được (tệp không mất dữ liệu nặng hơn nên số ảnh còn lại sẽ giảm đi).
- Ứng dụng ghi nhớ cài đặt ban đầu của máy ảnh này để sau này bạn có thể «Khôi phục». Nếu bạn đã tự đổi trên thân máy ảnh rồi thì ứng dụng sẽ không ghi đè.

---

## Xem trước phong cách .np3 (miễn phí)
Thẻ **.np3** trong trình chỉnh sửa: áp dụng tệp Nikon Picture Control (`.np3`, `.ncp`) lên ảnh để xem trước hiệu ứng ngay trên điện thoại.
- Nhấn vào một phong cách là áp dụng ngay, chỉnh cường độ 0–100%, sau đó có thể sang thẻ «Điều chỉnh» để tinh chỉnh thêm.
- Vuốt trái/phải trên ảnh để đổi nhanh phong cách, nhấn giữ để xem ảnh gốc. Bên dưới có mục lọc `★` Yêu thích và Dùng gần đây.
- Nhấn **Tất cả N ▴** để mở rộng toàn bộ thư viện phong cách (xem bên dưới), có thể tìm kiếm và lọc.
- Ứng dụng mô phỏng đường cong (curve) và độ bão hòa: tệp có sẵn đường cong sẽ dùng đường cong trong tệp; tệp chỉnh màu bằng thanh trượt Flexible Color (gắn nhãn «Tông màu thanh trượt») sẽ dùng đường cong quy đổi từ kết quả đo thực tế trên NX Studio. **Bộ trộn màu (Color Blender) và phân loại màu (Color Grading) hiện chưa mô phỏng**, nên hiệu ứng chỉ mang tính gần đúng.
- Dùng trên tệp NEF cho kết quả tốt nhất; nếu ảnh JPEG lúc chụp đã áp sẵn phong cách màu trên máy ảnh thì hiệu ứng sẽ cộng dồn và ứng dụng sẽ nhắc bạn.

📷 Ảnh chụp màn hình: thẻ .np3

---

## Phong cách máy ảnh C1–C9 (Pro)
Quản lý các ô cấu hình màu tùy chỉnh C1–C9 trên máy ảnh ngay từ điện thoại. Nhấn thẻ **Phong cách máy ảnh** ở Trang chủ để vào (cần kết nối Wi‑Fi hoặc USB với máy ảnh).
- Mỗi ô hiển thị hình xem trước, tên gọi, kèm nhãn đang dùng, có đường cong hay Flexible Color.
- **Nhấn vào một ô** để chọn một phong cách từ thư viện và ghi vào máy ảnh; ghi xong ứng dụng tự đọc lại đối chiếu, khớp hoàn toàn mới đánh dấu `✓`. **Nhấn giữ** hoặc nhấn `⋮` để xóa trống ô đó. Nếu đang nhận ảnh, ứng dụng sẽ chờ tấm hiện tại truyền xong rồi mới ghi.
- Chỉ khi mở màn hình này, nhấn `↻`, ghi hoặc xóa thì mới đọc/ghi dữ liệu với máy ảnh; Trang chủ hiển thị nội dung và thời gian đọc được lần gần nhất.
- Phía dưới là 9 công thức của Nikon Imaging Cloud (chỉ đọc, muốn thêm cần thao tác qua Nikon Imaging Cloud).

### Dữ liệu nào được ghi vào máy ảnh
Các ô tùy chỉnh trên máy ảnh chỉ nhận **Picture Control nền ＋ các thông số tinh chỉnh**, chứ không nhận nguyên tệp `.np3`:
- Nút **＋ Thêm phong cách** trong thư viện cho phép chọn nền (Standard, Flat, Creative Picture Control…) và chỉnh độ sắc nét, độ trong trẻo, tương phản, độ sáng, độ bão hòa, sắc độ.
- **Ghi `.np3` / `.ncp` vào máy ảnh (gần đúng)**: các tệp có đường cong và tệp «Tông màu thanh trượt» (đã quy đổi sang đường cong) có thể ghi **Tên ＋ Đường cong ＋ Làm nét (Độ sắc nét, Làm nét dải trung, Độ trong trẻo)** vào ô C, phần nền do bạn tự chọn. **Độ bão hòa, bộ trộn màu và phân loại màu không ghi vào được**, trước khi ghi ứng dụng sẽ liệt kê toàn bộ thông số trong tệp và đánh dấu rõ phần nào không ghi được.
- Để có hiệu ứng trọn vẹn 100%, bạn vẫn nên chép `.np3` vào thẻ nhớ và nhập trực tiếp qua menu trên máy ảnh.

### Thư viện phong cách
- Lưu tối đa 256 phong cách, hỗ trợ `.np3` và `.ncp`.
- Có thanh tìm kiếm `🔍`, bộ lọc (Tất cả, `★`, Dùng gần đây, Có đường cong, Đã có trên máy, Ghi được vào máy) và nút **＋ Thêm**.
- Mỗi phong cách đều có ảnh thu nhỏ xem trước. Ảnh xem trước dùng chính ảnh mẫu bạn nhập vào (`＋ → «Ảnh mẫu xem trước…»`), khi chưa nhập sẽ dùng bảng màu chuẩn.

📷 Ảnh chụp màn hình: Phong cách máy ảnh C1–C9, thư viện phong cách

---

## Xử lý hình ảnh: ghép toàn cảnh, ghép giảm nhiễu (Pro)
Trong «Ảnh trên điện thoại», chọn vài bức ảnh rồi **vuốt thanh thao tác dưới cùng lên trên** (hoặc nhấn vào thanh nắm) để mở «Xử lý hình ảnh».

### Ghép ảnh (Toàn cảnh)
- Chọn bên trong một chồng ảnh «Toàn cảnh»: ghép đúng theo vị trí ô lưới lúc chụp, thành phẩm lưu lại vào chính chồng ảnh đó với nhãn «Toàn cảnh».
- Chọn bất kỳ vài tấm ảnh có phần chồng mép trong thư viện thông thường: ứng dụng tự nhận diện tấm nào nối với tấm nào, thành phẩm lưu thành một chồng ảnh mới.
- Những tấm không khớp sẽ không làm hỏng cả nhóm: ứng dụng vẫn ghép nhóm lớn nhất nối được với nhau và liệt kê tên các tệp bị bỏ ra. Với kiểu chụp theo lưới, nếu thiếu mất một ô thì sẽ không xuất ảnh để tránh thành phẩm bị khuyết lỗ.
- Chụp đủ một vòng 360° sẽ xuất ra ảnh toàn cảnh 360°; thành phẩm luôn cân bằng đường chân trời (nhờ dữ liệu thước cân bằng lưu lúc chụp), không bị bóng ma và giữ nguyên thông số chụp.
- Xem cách chụp tại [Chương 5 Ghép toàn cảnh](05-remote.md#ghép-toàn-cảnh-panorama).

### Ghép giảm nhiễu (Shake)
- Các ảnh đã chọn được căn chỉnh khớp vị trí rồi tính trung bình để giảm nhiễu mà chi tiết không thay đổi; vùng có chuyển động chỉ lấy từ một tấm nên không bị bóng ma.
- Chọn bên trong chồng ảnh «Shake» thì lưu ngay lại vào chồng ảnh đó (thành phẩm gắn nhãn «Đã ghép»), hoặc bạn có thể nhấn nút **Ghép** / **Ghép lại** phía trên chồng ảnh.
- Xem cách chụp tại [Chương 5 Shake](05-remote.md#shake-ghép-giảm-nhiễu).

> Mỗi lần chỉ chạy một tác vụ ghép toàn cảnh hoặc ghép giảm nhiễu, tiến độ hiển thị trực tiếp trên màn hình, hoàn tất chỉ cần nhấn vào là mở xem ngay.
