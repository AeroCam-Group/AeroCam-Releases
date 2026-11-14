<!-- translated from zh-TW at commit 968641f -->

# 1. Cài đặt và bắt đầu sử dụng

## Cài đặt
1. Tải về tệp Beta APK mới nhất (`…-Beta-xx.xx.xx.apk`) từ [Releases](https://github.com/AeroCam-Group/AeroCam-Releases/releases/latest).
2. Mở tệp APK trên điện thoại. Lần đầu cài đặt, Android sẽ yêu cầu cho phép «Cài đặt ứng dụng không xác định» — hãy cho phép.
3. Khi có phiên bản mới, bạn chỉ cần tải về và cài đè lên bản cũ; dữ liệu ghép nối và cài đặt đều được giữ nguyên.

> Chỉ tải ứng dụng từ AeroCam-Releases. Tệp APK từ các nguồn khác có thể đã bị chỉnh sửa. Nếu khi mở ứng dụng xuất hiện thông báo «Đây không phải phiên bản chính thức», nghĩa là ứng dụng đã bị bên thứ ba đóng gói lại: ứng dụng đó sẽ không nhận khóa thử nghiệm và có thể bị chèn mã lạ, hãy gỡ cài đặt và tải lại từ AeroCam-Releases.

> Nếu bạn từng dùng **bản Beta cũ trước 92.03.09**: bản mới sẽ cài đặt thành một ứng dụng riêng biệt. Hãy ghép nối lại máy ảnh và nhập lại khóa thử nghiệm, kiểm tra mọi thứ hoạt động ổn định rồi mới gỡ bản cũ.

📷 Ảnh chụp màn hình: màn hình hệ thống «Cài đặt ứng dụng không xác định»

## Quyền truy cập
Ứng dụng chỉ yêu cầu quyền khi bạn dùng đến tính năng cần quyền đó, bạn có thể từ chối những quyền không cần thiết:

| Quyền | Mục đích sử dụng |
|---|---|
| Bluetooth, Thiết bị ở gần | Ghép nối Bluetooth, truyền ảnh qua Bluetooth, điều khiển từ xa Bluetooth; trên Android 13 trở lên cũng cần để tìm máy ảnh Wi‑Fi |
| Vị trí | Gửi vị trí điện thoại sang máy ảnh để ghi vào ảnh, hoặc bổ sung vị trí cho ảnh JPEG nhận về; Android cũng yêu cầu quyền này để đọc tên mạng Wi‑Fi |
| Thông báo | Tiến trình nhận ảnh, thông báo khi nhận xong ảnh, lỗi truyền tải, cảnh báo pin yếu của máy ảnh |
| Ảnh và video | Hiển thị và sắp xếp ảnh trên điện thoại |

Xem giải thích chi tiết về từng quyền tại [Quyền riêng tư và thống kê ẩn danh](10-privacy.md).

## Tổng quan giao diện
Phía dưới màn hình có bốn thẻ:

| Thẻ | Nội dung |
|---|---|
| **Trang chủ** | Bảng điều khiển máy ảnh (pin, ống kính, thẻ nhớ, trạng thái kết nối), bốn phương thức kết nối (Wi‑Fi, USB, Bluetooth, FTP), trạng thái và lịch sử truyền, phong cách máy ảnh, quản lý máy ảnh |
| **Cuộn camera** | Gồm hai thẻ con «Ảnh trên điện thoại» và «Thẻ SD máy ảnh» — xem [Chương 4](04-gallery.md) |
| **Chụp từ xa** | Xem hình ảnh trực tiếp từ máy ảnh trên điện thoại, chỉnh thông số, chụp ảnh và quay phim — xem [Chương 5](05-remote.md) |
| **Cài đặt** | Năm nhóm cài đặt — xem [Chương 7](07-settings.md) |

Khi chưa biết cách kết nối máy ảnh, hãy nhấn biểu tượng **ⓘ** bên cạnh trạng thái kết nối ở Trang chủ, hoặc ở góc trên bên phải mỗi bước trong mục «Thêm máy ảnh» để mở hướng dẫn minh họa bằng hình ảnh.

📷 Ảnh chụp màn hình: Trang chủ

## Khóa thử nghiệm (mở khóa Pro, Cine)
Bản Beta mặc định ở gói miễn phí.
1. Truy cập [trang chủ AeroCam-Releases](https://github.com/AeroCam-Group/AeroCam-Releases) để sao chép khóa thử nghiệm hiện tại. Trong ứng dụng, mục **Cài đặt → Hỗ trợ → «Lấy khóa miễn phí»** sẽ mở thẳng trang đó.
2. Vào **Cài đặt → Hỗ trợ → «Nhập khóa thử nghiệm»**, dán toàn bộ chuỗi ký tự rồi nhấn «Áp dụng». Khi nhấn vào một tính năng bị khóa, hộp thoại hiện ra cũng có nút «Nhập khóa thử nghiệm».
3. Mỗi khóa có hiệu lực 14 ngày và được làm mới vào thứ Hai hằng tuần. Khi hết hạn, ứng dụng trở về gói miễn phí — bạn chỉ cần dán khóa mới vào.

> Cả bản Beta lẫn khóa thử nghiệm đều hoàn toàn **miễn phí** và chỉ phát hành trên GitHub tại AeroCam-Releases. Nếu có ai thu phí của bạn, đó không phải kênh chính thức.

## Kiểm tra cập nhật
Bản Beta tự động kiểm tra cập nhật một lần mỗi ngày khi mở ứng dụng lần đầu. Bạn cũng có thể kiểm tra thủ công tại **Cài đặt → Hỗ trợ → «Kiểm tra cập nhật»**.

## Ngôn ngữ
Giao diện hỗ trợ Tiếng Trung phồn thể, Tiếng Trung giản thể, Tiếng Nhật, Tiếng Anh, 한국어, Deutsch, Français, Español, Tiếng Việt, ไทย và Bahasa Indonesia. Mặc định ứng dụng theo ngôn ngữ hệ thống của điện thoại, hoặc bạn có thể đổi tại **Cài đặt → Giao diện và ngôn ngữ → Ngôn ngữ**.

Tiếng Anh, Tiếng Trung phồn thể và Tiếng Nhật luôn đầy đủ 100%; các tính năng mới ở những ngôn ngữ khác có thể hiển thị tiếng Anh trước rồi bổ sung bản dịch sau. Nếu phát hiện chỗ dịch chưa chuẩn, hãy báo cho chúng tôi qua biểu mẫu «Lỗi dịch thuật» tại [Báo cáo sự cố](12-report.md).

## Thống kê sử dụng ẩn danh
Sau lần kết nối máy ảnh đầu tiên, ứng dụng sẽ giải thích một lần về «Gửi thống kê sử dụng ẩn danh», bạn có thể chọn «OK» hoặc «Tắt» — trước khi bạn trả lời, ứng dụng không gửi bất kỳ dữ liệu nào. Sau này bạn có thể tắt bất cứ lúc nào tại **Cài đặt → Hỗ trợ**. Chi tiết dữ liệu nào được gửi và tuyệt đối không gửi xem tại [Quyền riêng tư và thống kê ẩn danh](10-privacy.md).
