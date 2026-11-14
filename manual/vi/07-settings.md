<!-- translated from zh-TW at commit 968641f -->

# 7. Giải thích từng mục cài đặt

**Cài đặt** chia làm năm nhóm chính, nhấn vào từng nhóm để xem các mục chi tiết. Bản miễn phí sẽ ẩn đi những cài đặt không dùng tới. Nếu có góp ý hoặc thấy giá trị mặc định nào chưa hợp lý, hãy [báo cáo cho chúng tôi](12-report.md).

## Nhận tệp và thông báo

### Nhận tệp
| Cài đặt | Tùy chọn | Mặc định | Giải thích |
|---|---|---|---|
| Loại tệp nhận về | Tất cả tệp / Chỉ JPG / JPG + RAW / Ảnh + video / Tùy chỉnh; kèm Chỉ lưu JPEG từ tệp RAW, Lưu bản JPEG nén, Thay thế bản nén khi nhận được ảnh gốc (Pro) | Tất cả tệp | Xem [Chương 3](03-receive.md#loại-tệp-nhận-về) |
| Thư mục lưu | Theo máy ảnh / Theo ngày / Theo máy ảnh và ngày / Theo loại tệp | Theo máy ảnh và ngày | Cách chia thư mục con bên trong `Pictures/AeroCam` và `Movies/AeroCam` |
| Tên tệp | Tên gốc từ máy ảnh / Thêm tiền tố ngày / Thêm tiền tố ngày giờ | Tên gốc từ máy ảnh | Chỉ áp dụng cho tệp lưu sau này; kiểm tra trùng lặp vẫn dựa trên tên gốc từ máy ảnh |
| Chế độ nhận (Pro) | Nhận liên tục / Nhận từng tệp | Nhận liên tục | Từng tệp ＝ nhận xong một tệp thì dừng |
| Không tự động nhận video lớn (Pro) | Giá trị (MB) | 1024 MB | Video vượt ngưỡng được ghi là «Đã lọc», cần tải thủ công |
| Khi không tìm thấy máy ảnh qua Wi‑Fi | 30 giây / 1 / 2 / 3 / 5 / 10 phút / Không giới hạn | 3 phút | Quá thời gian tự dừng nhận để tránh thử lại liên tục gây hao pin |
| Tự tắt FTP sau bao lâu không nhận được ảnh | Không tự tắt / 5 / 10 / 30 phút | Không tự tắt | Tính từ tấm ảnh cuối cùng nhận được, không tắt khi đang truyền dở |
| Ảnh đã nhận qua Bluetooth | Thay bằng ảnh gốc khi nhận qua Wi‑Fi / Không tải lại qua Wi‑Fi / Giữ cả hai bản | Thay bằng ảnh gốc | Ảnh nhận qua Bluetooth là bản thu nhỏ khoảng 2 MB |

### Vị trí ảnh
| Cài đặt | Mặc định | Giải thích |
|---|---|---|
| Gửi vị trí cho máy ảnh (Bluetooth) | Bật | Khi bật máy ảnh hoặc gửi ảnh qua Bluetooth, điện thoại gửi vị trí sang máy ảnh để ghi vào ảnh |
| Bổ sung vị trí cho ảnh JPEG nhận về (điện thoại) | Tắt (sẽ hỏi ở lần nhận đầu tiên) | Ảnh JPEG nhận qua Wi‑Fi, USB, FTP được điện thoại ghi tọa độ dựa theo giờ chụp; tệp RAW không sửa |

Xem chi tiết tại [Chương 3 Vị trí ảnh](03-receive.md#vị-trí-ảnh-gps).

### Thư viện ảnh
| Cài đặt | Tùy chọn | Mặc định | Giải thích |
|---|---|---|---|
| Chất lượng ảnh JPEG nén (Pro) | 60 / 70 / 80 / 90% | 80% | Chất lượng ảnh JPEG do điện thoại nén lại (ảnh 24 MP nặng khoảng 3–4 MB) |
| Lựa chọn sau khi tải về / xóa | Luôn hỏi / Luôn giữ / Luôn bỏ chọn | Luôn hỏi | Tránh giữ nguyên vùng chọn rồi bấm nhầm «Xóa khỏi máy ảnh» |
| Đếm ngược hộp thoại hỏi | 3 / 5 / 8 / 10 giây | 5 giây | Khi chọn «Luôn hỏi», hết giờ không trả lời sẽ tự động bỏ chọn |
| Dừng chia sẻ mã QR sau bao lâu | 15 / 30 / 60 phút | 30 phút | Hết thời gian đường dẫn tự động hết hiệu lực |

### Thông báo
| Cài đặt | Mặc định | Giải thích |
|---|---|---|
| Không làm phiền | Tắt | Tắt toàn bộ thông báo của AeroCam (thông báo thường trực «Đang nhận» vẫn giữ lại theo quy định của Android) |
| Khi bắt đầu truyền | Tắt | |
| Khi nhận được ảnh | Bật | |
| Sự cố truyền tải | Bật | Bị treo, máy ảnh hủy truyền, điện thoại thiếu dung lượng |
| Ẩn thông báo thường trực | — | Mở phần cài đặt thông báo của Android để tắt hiển thị tại đó; việc nhận ảnh vẫn chạy bình thường |
| Cảnh báo pin yếu máy ảnh | Bật, 15% | Các mức ngưỡng 10 / 15 / 20 / 30%; chỉ kiểm tra khi đang kết nối máy ảnh |

## Chụp ảnh

### Nơi lưu tệp
| Cài đặt | Tùy chọn | Giải thích |
|---|---|---|
| Nơi lưu tệp | Thẻ nhớ / Thẻ nhớ + điện thoại (Pro) | Áp dụng khi máy ảnh có lắp thẻ; khi không có thẻ tự chuyển sang chỉ lưu điện thoại (Pro). Khi kết nối máy ảnh sẽ hiện trạng thái thẻ hiện tại. Xem [Chương 3](03-receive.md#nơi-lưu-tệp-và-chụp-không-cần-thẻ-nhớ) |

### Chụp từ xa
| Cài đặt | Tùy chọn | Mặc định | Giải thích |
|---|---|---|---|
| Mặc định bật khi vào Chụp từ xa | Lấy nét trước khi chụp, Biểu đồ sáng, Cảnh báo cháy sáng, Báo nét peaking, Thanh đo sáng | Lấy nét trước khi chụp, Thanh đo sáng | Trong lúc chụp vẫn bật/tắt tùy ý được |
| Màu thanh đo sáng | Tự động / Trắng / Đen | Tự động | Tự động ＝ đổi theo độ sáng vùng nền phía sau |
| Màu báo nét peaking | Đỏ / Vàng / Xanh dương / Trắng | Đỏ | Khi chủ thể thiên về màu đỏ có thể đổi màu khác cho dễ nhìn |
| Giữ màn hình luôn sáng khi chụp từ xa | Bật / Tắt | Bật | Giữ màn hình điện thoại không tắt khi chụp giãn cách hoặc phơi sáng lâu |
| Chế độ tay trái | Bật / Tắt | Tắt | Khi cầm ngang sẽ chuyển nút chụp sang góc dưới bên trái |

### Kết nối có dây (USB‑C)
| Cài đặt | Tùy chọn | Mặc định | Giải thích |
|---|---|---|---|
| Tần số khung hình xem trước USB | 30 / 60 fps / Không giới hạn | 30 fps | 30 fps tiết kiệm pin và mát máy; 60 fps mượt hơn |
| Xem trước USB kích thước lớn | Bật / Tắt | Bật | Hình nét hơn, tốc độ khung hình có thể giảm nhẹ; tự lùi về chuẩn thường nếu máy ảnh không hỗ trợ |
| Tự động bắt đầu nhận khi cắm cáp USB (Pro) | Bật / Tắt | Bật | Cắm cáp là tự động chạy nhận ảnh qua USB |
| Đồng bộ giờ máy ảnh khi kết nối | Bật / Tắt | Bật | Chỉ chỉnh khi lệch quá 2 giây; lệch trên 1 ngày sẽ hỏi trước |
| Giữ máy ảnh thức khi cắm dây | Bật / Tắt | Bật | Cứ 10 giây gửi một tín hiệu nhỏ; tự dừng sau 30 phút không thao tác hoặc khi pin yếu |

## Giao diện và ngôn ngữ
| Cài đặt | Tùy chọn | Mặc định |
|---|---|---|
| Chủ đề | Theo hệ thống / Sáng / Tối / Sao đêm (ánh sáng đỏ) | Theo hệ thống |
| Giảm độ sáng màn hình ứng dụng xuống mức thấp nhất | Bật / Tắt (khi dùng chế độ sao đêm) | Tắt |
| Ngôn ngữ | Theo hệ thống / 繁中 / 简中 / 日本語 / English / 한국어 / Deutsch / Français / Español / Tiếng Việt / ไทย / Bahasa Indonesia | Theo hệ thống |

## Bộ nhớ và pin
| Mục | Giải thích |
|---|---|
| Bộ nhớ đệm ảnh thu nhỏ | Hiển thị dung lượng đang chiếm và cho phép xóa (khi cần sẽ tự đọc lại từ máy ảnh) |
| Tệp tạm tải xuống chưa hoàn tất | Hiển thị dung lượng và cho phép xóa |
| Quét lại ảnh trên điện thoại | Tìm lại các ảnh vừa quay lại điện thoại, ví dụ ảnh khôi phục từ thùng rác hoặc ảnh lưu trước khi cài lại ứng dụng |
| Tối ưu hóa pin | Khuyên dùng tắt tối ưu hóa (hiển thị «Không tối ưu hóa ✓»), nếu không việc nhận ảnh ngầm dễ bị hệ thống ngắt |

## Hỗ trợ
| Mục | Giải thích |
|---|---|
| Sao chép thông tin chẩn đoán | Dán khi báo lỗi: phiên bản ứng dụng, trạng thái điện thoại và mạng, khả năng hỗ trợ của máy ảnh, lịch sử lệnh gần nhất, lỗi thoát đột ngột lần cuối. Số sê-ri máy ảnh chỉ giữ lại 4 ký tự cuối |
| Xóa nhật ký | Xóa nhật ký phiên hiện tại, phiên trước đó và lịch sử lỗi thoát ứng dụng |
| Kiểm tra cập nhật | Kiểm tra thủ công phiên bản mới; bên dưới hiển thị phiên bản hiện tại |
| Khóa thử nghiệm | «Lấy khóa miễn phí» mở trang AeroCam-Releases; «Nhập khóa thử nghiệm» để dán khóa; hiển thị gói hiện tại và ngày hết hạn |
| Giấy phép mã nguồn mở | Các thành phần bên thứ ba sử dụng trong ứng dụng (ví dụ LibRaw dùng để giải mã RAW) |
| Gửi thống kê sử dụng ẩn danh | Một công tắc duy nhất, mặc định bật. Xem [Quyền riêng tư và thống kê ẩn danh](10-privacy.md) |
