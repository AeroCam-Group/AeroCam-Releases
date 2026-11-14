<!-- translated from zh-TW at commit 968641f -->

# 10. Quyền riêng tư và thống kê ẩn danh

AeroCam không có hệ thống tài khoản, ảnh chỉ truyền trực tiếp giữa máy ảnh và điện thoại của bạn, **không tải lên bất kỳ máy chủ nào**. Chỉ một lượng nhỏ dữ liệu liệt kê dưới đây rời khỏi điện thoại.

## Các tính năng có kết nối mạng
| Tính năng | Dữ liệu gửi đi | Có tắt được không |
|---|---|---|
| Kiểm tra cập nhật (Beta) | Chỉ truy vấn phiên bản mới nhất trên GitHub | Tự động mỗi ngày một lần |
| Thống kê sử dụng ẩn danh | Xem bên dưới | Có, Cài đặt → Hỗ trợ |
| Chia sẻ qua mã QR | Chỉ hoạt động trong mạng cục bộ của bạn (cùng Wi‑Fi hoặc điểm phát sóng di động) để người quét mã xem ảnh bạn đã chọn | Kết thúc khi bạn nhấn dừng hoặc hết giờ |

## Thống kê sử dụng ẩn danh
Dùng để nắm sơ bộ có bao nhiêu người đang dùng, những dòng máy ảnh và tính năng nào được dùng nhiều, chỗ nào hay gặp lỗi để quyết định ưu tiên phát triển tiếp theo. **Không bán cho bất kỳ ai và cũng không dùng cho quảng cáo.**

- **Công tắc**: **Cài đặt → Hỗ trợ → «Gửi thống kê sử dụng ẩn danh»**, mặc định bật.
- Sau lần đầu kết nối máy ảnh sẽ giải thích một lần, bạn có thể chọn «OK» hoặc «Tắt». **Trước khi bạn trả lời, không gửi bất kỳ dữ liệu nào.**
- **Sau khi tắt**: ngừng gửi ngay lập tức, đồng thời xóa mã ID ngẫu nhiên nêu dưới đây và toàn bộ dữ liệu chưa kịp gửi. Nếu bật lại sẽ tạo một mã ID mới.
- Khi không có mạng Internet (ví dụ đang nối vào Wi‑Fi của máy ảnh), dữ liệu tạm lưu trên điện thoại và gửi đi khi có mạng trở lại.
- Bản dựng phát triển (Dev) không ghi nhận và không gửi thống kê.

### Dữ liệu sẽ gửi đi
- **Mã ID ngẫu nhiên do ứng dụng tự tạo**: không lấy từ điện thoại hay máy ảnh; cài lại ứng dụng hoặc tắt thống kê sẽ đổi sang mã khác.
- Tên dòng máy ảnh (ví dụ Nikon Z f), chỉ gửi tên mẫu máy.
- Phương thức kết nối (Bluetooth, Wi‑Fi, USB, FTP), loại Wi‑Fi (Wi‑Fi của máy ảnh, điểm phát sóng di động, bộ phát router).
- Các tính năng đã dùng trong ngày (chỉ ghi tên tính năng, mỗi ngày một lần), bao gồm cả việc nhấn vào các tính năng đang bị khóa.
- Số lần kết nối thành công hoặc thất bại; khi thất bại chỉ gửi mã phân loại (ví dụ «hết thời gian chờ»), không gửi nội dung thông báo lỗi.
- Các bước thêm máy ảnh: bắt đầu, thành công, không tìm thấy máy ảnh, nguyên nhân thất bại.
- Số lượng ảnh nhận được mỗi ngày (bao nhiêu ảnh JPEG, RAW, video, chỉ ghi số lượng).
- Trạng thái quyền là cho phép hay từ chối.
- Gói hiện tại (Miễn phí, khóa Beta…), phiên bản ứng dụng, ngôn ngữ ứng dụng, phiên bản chính của Android.
- Quốc gia: xác định qua kết nối mạng, chỉ lưu mã quốc gia.

### Tuyệt đối không truyền đi
Số sê-ri máy ảnh, tên chủ sở hữu hoặc thông tin bản quyền cài trong máy ảnh, vị trí (GPS), ảnh và video, tên tệp, thông số chụp (EXIF), tên và mật khẩu Wi‑Fi, mã định danh điện thoại (IMEI, Android ID, ID quảng cáo), họ tên, Email, tài khoản, nội dung thông báo lỗi.

### Thời gian lưu trữ
- Dữ liệu chi tiết hằng ngày của từng điện thoại được lưu 90 ngày, sau đó chỉ giữ lại tổng số liệu chung của từng ngày.
- Mã ID không hoạt động trong khoảng 13 tháng sẽ bị xóa.
- Khi máy chủ xử lý kết nối tất yếu sẽ thấy địa chỉ IP, nhưng chỉ dùng để xác định quốc gia và chống lạm dụng, **không bao giờ lưu vào dữ liệu thống kê**.

## Thông tin vị trí
- **Gửi vị trí cho máy ảnh (Bluetooth)**: điện thoại gửi vị trí sang máy ảnh để máy ảnh tự ghi vào ảnh.
- **Bổ sung vị trí cho ảnh JPEG nhận về (điện thoại)**: mặc định tắt. Khi bật, tọa độ điện thoại ghi lại trong thời gian nhận chỉ lưu trên điện thoại này và tự xóa sau 24 giờ.
- Cả hai công tắc đều nằm tại **Cài đặt → Nhận tệp và thông báo → Vị trí ảnh**, xem [Chương 3](03-receive.md#vị-trí-ảnh-gps).
- Tọa độ lưu trong ảnh sẽ đi theo tệp ảnh, khi chia sẻ tệp gốc người nhận cũng xem được. **Chia sẻ mã QR mặc định sẽ xóa thông tin vị trí**.

## Mục đích sử dụng quyền
| Quyền | Mục đích |
|---|---|
| Bluetooth, Thiết bị ở gần | Ghép nối với máy ảnh, truyền ảnh Bluetooth, điều khiển từ xa Bluetooth, tìm máy ảnh Wi‑Fi |
| Vị trí | Gửi sang máy ảnh hoặc bổ sung vào ảnh; Android cũng cần quyền này để đọc tên mạng Wi‑Fi |
| Thông báo | Tiến trình nhận, thông báo nhận được ảnh, sự cố truyền tải, cảnh báo pin yếu máy ảnh |
| Ảnh và video | Hiển thị và sắp xếp ảnh trong mục Ảnh trên điện thoại |

## Thông tin chẩn đoán
**Cài đặt → Hỗ trợ → «Sao chép thông tin chẩn đoán»** chỉ sao chép văn bản vào bộ nhớ tạm, **do bạn tự quyết định** có dán gửi cho chúng tôi hay không. Nội dung gồm phiên bản ứng dụng, trạng thái điện thoại và mạng, khả năng hỗ trợ của máy ảnh, nhật ký kết nối gần nhất; số sê-ri máy ảnh chỉ giữ lại 4 ký tự cuối. Trước khi dán lên GitHub Issue công khai, vui lòng kiểm tra lại xem có thông tin nào bạn không muốn công khai hay không.
