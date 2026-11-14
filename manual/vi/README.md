<!-- translated from zh-TW at commit 968641f -->

# Hướng dẫn sử dụng AeroCam (Tiếng Việt)

> Tương ứng với **Beta 92.04.08.10** (cập nhật ngày 2026-11-15). Các dòng có ký hiệu 📷 là vị trí dành sẵn để bổ sung ảnh chụp màn hình sau.

AeroCam giúp chuyển ảnh từ máy ảnh trực tiếp sang điện thoại Android, đồng thời cho phép điều khiển máy ảnh từ xa, chỉnh sửa ảnh trên điện thoại và ghi cấu hình màu vào máy ảnh. Hiện hỗ trợ **dòng Nikon Z** và sẽ mở rộng thêm nhiều hãng khác trong thời gian tới.

AeroCam là ứng dụng bên thứ ba được phát triển độc lập, không có bất kỳ mối quan hệ hợp tác hay ủy quyền nào từ Nikon hoặc bất kỳ hãng máy ảnh nào khác.

## Mục lục

1. [Cài đặt và bắt đầu sử dụng](01-install.md): cài đặt, quyền truy cập, tổng quan giao diện, khóa thử nghiệm, cập nhật, ngôn ngữ
2. [Kết nối máy ảnh](02-connect.md): Bluetooth, Wi‑Fi (Kết nối một chạm / điểm phát sóng di động / cùng mạng Wi‑Fi), cáp USB, cách chọn, hướng dẫn kết nối
3. [Tự động nhận và lưu tệp](03-receive.md): bắt đầu/tạm dừng nhận, quy tắc nhận, thư mục và tên tệp, chụp không cần thẻ nhớ, vị trí ảnh, bảng điều khiển máy ảnh, lịch sử
4. [Thư viện ảnh](04-gallery.md): thẻ nhớ máy ảnh, ảnh trên điện thoại, tải về và xóa, đánh giá sao, sao lưu thẻ nhớ, chia sẻ qua mã QR
5. [Chụp từ xa và điều khiển](05-remote.md): chụp từ xa qua Wi‑Fi/USB, phương thức chụp, công cụ hỗ trợ chụp, điều khiển từ xa Bluetooth, màn hình giám sát quay phim, chế độ chụp sao đêm
6. [Chỉnh sửa ảnh và phong cách màu](06-edit.md): trình chỉnh sửa, xem trước phong cách .np3, chỉnh sửa RAW trên điện thoại, phong cách máy ảnh C1–C9, ghép ảnh toàn cảnh, ghép giảm nhiễu (Shake)
7. [Giải thích từng mục cài đặt](07-settings.md)
8. [Nhận ảnh qua FTP](08-ftp.md): máy ảnh tự động đẩy ảnh sang điện thoại ngay sau khi chụp
9. [Miễn phí / Pro / Cine](09-tiers.md)
10. [Quyền riêng tư và thống kê ẩn danh](10-privacy.md)
11. [Câu hỏi thường gặp và khắc phục sự cố](11-faq.md)
12. [Báo cáo sự cố](12-report.md)

## Máy ảnh được hỗ trợ

| Dòng máy | Tự động nhận, thư viện máy ảnh | Chụp từ xa | Trạng thái |
|---|---|---|---|
| Z9, Z8, Z6III, Zf, Z5II, Z50II, ZR và các máy có mục «Connection type» (Loại kết nối) trong menu | ✅ | ✅ | Đã thử nghiệm thực tế trên Zf; hoan nghênh báo cáo từ các máy khác |
| Z6, Z7, Z6II, Z7II, Z5, Z50, Zfc, Z30 và các đời máy cũ hơn | ✅ | ❌ (giao thức kết nối của các dòng máy này không hỗ trợ) | Hoan nghênh báo cáo |
| Canon, Sony, Fujifilm | Đang chuẩn bị | Đang chuẩn bị | |

Nếu bạn đã thử nghiệm trên dòng máy khác, hãy cho chúng tôi biết tính năng nào hoạt động và chưa hoạt động qua biểu mẫu [Báo cáo dòng máy](https://github.com/AeroCam-Group/AeroCam-Releases/issues/new/choose).

## Yêu cầu hệ thống
- Điện thoại chạy Android 10 trở lên.
- Máy ảnh dòng Nikon Z.

## Thuật ngữ dùng trong tài liệu
| Thuật ngữ | Ý nghĩa |
|---|---|
| Thư viện máy ảnh / thẻ nhớ máy ảnh | Ảnh nằm trên thẻ nhớ của máy ảnh, được duyệt trực tiếp trên điện thoại thông qua kết nối |
| Ảnh trên điện thoại | Ảnh đã được lưu sẵn trên điện thoại |
| RAW | Tệp NEF của Nikon |
| JPEG.S | Ảnh JPEG đã nén (JPEG trích xuất từ RAW, JPEG được điện thoại nén lại hoặc bản thu nhỏ gửi qua Bluetooth), tên tệp kết thúc bằng `_S.JPG` |
| Picture Control | Cấu hình màu của máy ảnh, ví dụ Standard hoặc Flat; các cấu hình tùy chỉnh được lưu ở C1–C9 |
| Pro / Cine | Các gói trả phí; trong giai đoạn Beta, chỉ cần nhập khóa thử nghiệm miễn phí để dùng toàn bộ tính năng — xem [Chương 9](09-tiers.md) |
