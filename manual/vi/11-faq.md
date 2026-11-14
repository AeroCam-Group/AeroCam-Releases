<!-- translated from zh-TW at commit 968641f -->

# 11. Câu hỏi thường gặp và khắc phục sự cố

## Chung
**Không nâng cấp Pro thì có chuyển ảnh từ máy ảnh sang điện thoại được không?**
Được. Bản miễn phí có thể tự động nhận ảnh JPEG thu nhỏ khoảng 2 megapixel qua Bluetooth, hoặc dùng cáp USB để duyệt thư viện máy ảnh, chọn thủ công và tải về tệp gốc.

**Bản Beta hay khóa thử nghiệm có mất tiền không?**
Không. Tất cả đều chỉ phát hành miễn phí trên GitHub tại AeroCam-Releases. Nếu có ai thu tiền của bạn, đó không phải kênh chính thức.

**Mở ứng dụng hiện thông báo «Đây không phải phiên bản chính thức»**
Ứng dụng này đã bị người khác đóng gói lại, sẽ không nhận khóa thử nghiệm và có thể bị chèn thêm mã lạ. Hãy gỡ bỏ và tải lại từ AeroCam-Releases.

**Sau khi cập nhật không thấy máy ảnh đã ghép nối và mất khóa thử nghiệm**
Từ bản 92.03.09 trở đi, bản mới cài đặt thành một ứng dụng riêng nên không mang dữ liệu từ bản cũ sang. Bạn hãy ghép nối lại máy ảnh và nhập lại khóa thử nghiệm.

**Ảnh được lưu ở đâu**
Ảnh lưu tại `Pictures/AeroCam`, video tại `Movies/AeroCam`, các tệp khác tại `Download/AeroCam`. Google Photos và các ứng dụng thư viện khác đều thấy ngay. Các tệp do bản cũ trước 92.03.09 lưu vẫn nằm ở thư mục cũ và không bị di chuyển.

**Đã xóa ảnh trên điện thoại, muốn truyền lại thì làm sao?**
Chỉ cần gửi lại từ máy ảnh, ứng dụng sẽ tự nhận biết tệp trên điện thoại không còn nữa và lưu lại.

**Khôi phục ảnh từ thùng rác điện thoại hoặc cài lại ứng dụng xong không thấy ảnh trong thư viện**
Vào **Cài đặt → Bộ nhớ và pin → «Quét lại ảnh trên điện thoại»**.

---

## Kết nối
**Không kết nối được với máy ảnh qua Wi‑Fi**
1. Đảm bảo máy ảnh đang dừng ở màn hình «Connect to PC» và trên màn hình có biểu tượng Wi‑Fi; nếu màn hình máy ảnh tắt hãy nhấn nửa cò để đánh thức.
2. Đúng loại kết nối (Connection type): tự động nhận, duyệt thẻ ＝ Image transfer; chụp từ xa, chụp không thẻ ＝ Camera control.
3. Cách dùng điểm phát sóng di động: kiểm tra điểm phát sóng đã bật và máy ảnh đang nối đúng vào mạng này.
4. Cách dùng cùng mạng Wi‑Fi: điện thoại và máy ảnh phải nối cùng một tên mạng Wi‑Fi (đôi khi điện thoại tự nhảy sang Wi‑Fi khác hoặc dữ liệu di động).
5. Thử dùng **Kết nối một chạm**, không cần bật điểm phát sóng cũng không cần bộ phát Wi‑Fi.
6. Nhấn biểu tượng **ⓘ** và làm lại từng bước theo hướng dẫn kết nối.

**Dùng Wi‑Fi khách sạn, triển lãm không bao giờ tìm thấy máy ảnh**
Wi‑Fi công cộng thường chặn các thiết bị kết nối nội bộ với nhau. Hãy chuyển sang điểm phát sóng di động hoặc kết nối một chạm.

**Máy ảnh báo «Đã ghép nối với thiết bị khác»**
Cấu hình mạng đó trên máy ảnh đang được ứng dụng khác sử dụng. Hãy tạo một hồ sơ mạng mới trên máy ảnh rồi ghép nối lại.

**Kết nối một chạm không tìm thấy Wi‑Fi của máy ảnh**
Sau khi nhận lệnh qua Bluetooth, máy ảnh mất 10–30 giây để bật Wi‑Fi, ứng dụng sẽ tự động thử lại. Nếu vẫn thất bại, hãy kiểm tra lại mật khẩu Wi‑Fi của máy ảnh đã đúng chưa.

**Điểm phát sóng di động hay tự tắt**
Một số điện thoại tự tắt điểm phát sóng khi thấy không có thiết bị dùng Internet. Vào cài đặt điểm phát sóng trên điện thoại tắt mục «Tự động tắt điểm phát sóng», hoặc chuyển sang dùng kết nối một chạm.

**Tắt rồi bật lại điểm phát sóng thì máy ảnh không kết nối lại được**
Địa chỉ IP điểm phát sóng của điện thoại có thể đã thay đổi. Khi dùng tự động nhận qua Wi‑Fi ứng dụng sẽ tự tìm lại; còn dùng FTP thì bạn phải đối chiếu và sửa lại địa chỉ máy chủ trên máy ảnh.

**Cắm cáp USB vào không có phản ứng gì**
1. Cài đặt USB trên máy ảnh phải là **MTP/PTP**.
2. Dây cáp phải truyền được dữ liệu (một số dây chỉ sạc được).
3. Khi điện thoại hiện hộp thoại «Cho phép truy cập» phải nhấn Cho phép.
4. Nhấn dấu `⋮` góc trên bên phải thẻ USB → **Kiểm tra USB** để xem lỗi ở bước nào.

**Nhận ảnh chạy ngầm hay bị ngắt giữa chừng**
Vào **Cài đặt → Bộ nhớ và pin** tắt tối ưu hóa pin. Trên điện thoại Xiaomi, OPPO và một số hãng cần vào thêm cài đặt hệ thống đặt AeroCam ở mức «Không hạn chế» pin.

---

## Bluetooth
**Truyền ảnh qua Bluetooth bị treo**
- Khi chụp RAW, máy ảnh phải chuyển sang JPEG rồi mới gửi; thao tác trên máy ảnh lúc đang truyền sẽ làm máy ảnh hủy gửi. Tốt nhất chụp xong hãy tắt máy ảnh để máy tự truyền ngầm.
- Nhấn **Ngắt và kết nối lại** trên thẻ Bluetooth, hoặc **⋮ → Khởi động lại dịch vụ Bluetooth**, ghép nối vẫn được giữ nguyên.

**Nhấn AF trên điều khiển từ xa Bluetooth máy không lấy nét**
Máy ảnh cần cho phép nhấn nửa cò để lấy nét. Nếu bạn quen dùng nút AF‑ON, hãy kiểm tra trong Cài đặt tùy chỉnh của máy ảnh xem mục **AF activation** (Kích hoạt AF) có đang bật cho nút chụp hay không.

**Nhận cùng một ảnh qua cả Bluetooth và Wi‑Fi có bị lưu thành hai bản không?**
Mặc định là không: khi Wi‑Fi nhận được ảnh gốc, ứng dụng tự động xóa bản thu nhỏ của Bluetooth. Bạn có thể đổi tùy chọn này tại **Cài đặt → Nhận tệp và thông báo → «Ảnh đã nhận qua Bluetooth»**.

---

## Chụp từ xa
**Không chỉnh được tốc độ màn trập hoặc ISO**
- Tốc độ màn trập chỉ chỉnh được ở chế độ S / M, khẩu độ ở chế độ A / M; muốn chỉnh ISO thủ công phải tắt ISO tự động trước.
- Với các máy có vòng xoay vật lý như Zf: xoay vòng tốc độ màn trập về **1/3 STEP**, vòng ISO về **C**.

**Chạm màn hình nhưng điểm lấy nét không di chuyển**
Vùng AF trên máy ảnh phải chọn chế độ cho phép di chuyển điểm nét (ví dụ AF điểm đơn). Ở chế độ AF vùng tự động máy ảnh sẽ tự quyết định.

**Bảng điều khiển Trang chủ thiếu một số mục (ống kính, số ảnh còn lại, số lần chụp)**
Một số thông tin máy ảnh chỉ cung cấp ở chế độ nhất định, hãy chuyển sang «Camera control» và vào giao diện Chụp từ xa thì thường sẽ đọc được. Số lần chụp yêu cầu thẻ nhớ phải có ít nhất một bức ảnh.

**Xem nhiệt độ màu (độ K) ở đâu?**
Nikon chỉ lưu giá trị độ K thực tế dưới dạng mã hóa trong tệp ảnh, nên mục «Chi tiết» chỉ hiển thị chế độ cân bằng trắng.

---

## Nơi lưu tệp và chụp không cần thẻ nhớ
**Máy ảnh không lắp thẻ nhớ, bấm nút chụp không phản ứng**
Kiểm tra mục **Slot empty release lock** trên máy ảnh đã đặt thành **Enable release** chưa, và ứng dụng đã kết nối máy ảnh chưa (thanh trạng thái hiện «chỉ điện thoại»).

**Ảnh xuất hiện chữ «DEMO»**
Khi máy ảnh không lắp thẻ nhớ mà lại không kết nối chế độ «chỉ điện thoại» của ứng dụng, máy ảnh sẽ đánh dấu ảnh là **DEMO** và không lưu. Hãy lắp thẻ nhớ vào, hoặc kết nối với AeroCam rồi mới chụp.

**Ảnh không vào điện thoại, phía trên Trang chủ hiện băng rôn màu đỏ**
- Ghi «Máy ảnh đang ở chế độ "Image transfer"»: chụp không thẻ nhớ phải dùng **Camera control**. Chuyển xong máy ảnh sẽ tự kết nối lại và truyền những ảnh đã chụp sang.
- Ghi «Wi‑Fi một chạm: không có thẻ nhớ»: kết nối một chạm không hỗ trợ chụp không thẻ, hãy lắp thẻ hoặc đổi sang điểm phát sóng / cùng mạng Wi‑Fi.

**Hiện thông báo «Mất kết nối»**
Khi chọn chỉ lưu điện thoại, mất kết nối quá 10 giây mới hiện cảnh báo vì ảnh chụp trong khoảng thời gian này có thể không lưu vào thẻ nhớ; sau khi kết nối lại ứng dụng sẽ tự động khôi phục.

---

## Chỉnh sửa và phong cách màu
**Không mở được hoặc không chỉnh sửa được tệp NEF**
Tệp NEF nén High efficiency / High efficiency★ sẽ dùng ảnh JPEG nhúng bên trong để chỉnh sửa; tệp chỉ có ảnh xem trước nhỏ thì không chỉnh được. Muốn giải mã RAW đầy đủ trên điện thoại, hãy chuyển máy ảnh sang **Lossless compression** (Nén không mất dữ liệu), xem [Chương 6](06-edit.md#raw-chỉnh-sửa-được-trên-điện-thoại-chuyển-chuẩn-nén-raw-của-máy-ảnh).

**Hiệu ứng áp .np3 trên điện thoại khác với trên máy ảnh**
Điện thoại mô phỏng đường cong và độ bão hòa, chưa mô phỏng bộ trộn màu và phân loại màu nên hiệu ứng chỉ gần đúng. Nếu ảnh JPEG lúc chụp đã áp sẵn phong cách màu trên máy ảnh thì hiệu ứng sẽ cộng dồn.

**Ghi .np3 vào máy ảnh xong màu sắc hiển thị khác**
Ô tùy chỉnh trên máy ảnh chỉ nhận **Nền ＋ Đường cong ＋ Làm nét**, không ghi được độ bão hòa, bộ trộn màu và phân loại màu. Muốn có hiệu ứng trọn vẹn, hãy chép tệp `.np3` vào thẻ nhớ và nhập qua menu trên máy ảnh.

**Ghép toàn cảnh thất bại hoặc bị thiếu vài tấm**
Mỗi tấm cần chồng lên tấm liền kề khoảng 30%. Những tấm không nối được sẽ liệt kê tên tệp; kiểu ghép theo lưới nếu thiếu một ô sẽ không xuất ảnh.

---

## FTP
**Máy ảnh báo lỗi Err.31 hoặc Err.32**
Hãy cập nhật lên bản Beta mới nhất. Đồng thời kiểm tra địa chỉ IP, cổng `2121`, tài khoản `aerocam`, mật khẩu nhập trên máy ảnh đã khớp hoàn toàn chưa và chế độ thụ động (PASV) phải bật.

**Máy ảnh báo đăng nhập thất bại**
Mật khẩu phải giống hệt chuỗi hiển thị trên thẻ FTP của AeroCam (phân biệt chữ hoa chữ thường). Nếu bạn đã nhấn «Tạo lại mật khẩu» thì trên máy ảnh cũng phải sửa lại theo.

**Đang bật FTP thì Thư viện ảnh hoặc Chụp từ xa không kết nối được**
Khi máy ảnh đang ở chế độ FTP sẽ không nhận kết nối Wi‑Fi cho Thư viện và Chụp từ xa. Hãy cắm cáp USB, hoặc dừng nhận FTP rồi chuyển máy ảnh lại về «Connect to PC».

---

## Khác
**Ứng dụng bị thoát đột ngột (crash)**
Mở lại ứng dụng, vào **Cài đặt → Hỗ trợ → «Sao chép thông tin chẩn đoán»**, dán vào biểu mẫu khi [báo cáo sự cố](12-report.md), bên trong có sẵn thông tin vị trí lỗi của lần thoát đột ngột gần nhất.

**Làm sao tắt thống kê sử dụng ẩn danh?**
Vào **Cài đặt → Hỗ trợ → «Gửi thống kê sử dụng ẩn danh»** và tắt đi là được, xem [Quyền riêng tư và thống kê ẩn danh](10-privacy.md).
