<!-- translated from zh-TW at commit 968641f -->

# 8. Nhận ảnh qua FTP (Pro)

Sau khi bấm máy chụp, máy ảnh sẽ **tự động đẩy ảnh sang điện thoại qua FTP** mà bạn không cần chọn ảnh trên máy ảnh hay mở thư viện. Thử nghiệm thực tế trên Nikon Zf, mỗi tệp RAW (khoảng 18 MB) chỉ mất khoảng 1 giây để sang tới điện thoại.

Bản thân AeroCam đã đóng vai trò là máy chủ FTP nên **bạn không cần cài đặt thêm bất kỳ máy chủ nào khác**.

## Phù hợp cho
- Sự kiện, đám cưới, thể thao: vừa chụp vừa đẩy ảnh trực tiếp sang điện thoại.
- Chụp xong muốn xem ngay trên màn hình lớn của điện thoại hoặc đăng mạng xã hội tức thì.

## Điều kiện cần
- Máy ảnh có tích hợp tính năng tải lên FTP (Nikon Z f, Z 8, Z 9, Z 6III, v.v.).
- Điện thoại bật **điểm phát sóng di động** và máy ảnh kết nối vào điểm phát sóng này (hoặc điện thoại và máy ảnh cùng nối vào một bộ phát Wi‑Fi).
- Máy ảnh phải lắp thẻ nhớ: giao thức FTP truyền các tệp nằm trên thẻ nhớ.

## Thiết lập (lần đầu)
1. Bật điểm phát sóng di động trên điện thoại.
2. Trên Trang chủ AeroCam, vào **FTP** → nhấn **Bắt đầu nhận** ở trên cùng. Màn hình sẽ hiển thị các thông số để bạn nhập vào máy ảnh, chạm vào từng mục để sao chép nhanh:
   - Địa chỉ máy chủ (ví dụ `10.14.29.30`)
   - Cổng (Port): `2121`
   - Tài khoản: `aerocam`
   - Mật khẩu: mã 8 ký tự do ứng dụng tạo (có thể nhấn «Tạo lại»)
   - Chế độ thụ động (PASV): **Bật**
3. Trên máy ảnh: **MENU → Menu mạng (Network menu) → Kết nối với máy chủ FTP (Connect to FTP server) → Cài đặt mạng (Network settings) → Tạo hồ sơ (Create profile)**:
   - Mục Wi‑Fi chọn điểm phát sóng của điện thoại.
   - Loại máy chủ chọn `FTP`, điền địa chỉ, cổng, tài khoản, mật khẩu ở trên và bật chế độ thụ động (PASV).
4. Kích hoạt kết nối FTP này trên máy ảnh. Khi trạng thái FTP trên AeroCam báo «Đã kết nối» là hoàn tất.
5. Trong menu FTP của máy ảnh, bật **Tự động gửi sau khi chụp** (Auto send), từ lúc này hễ bấm máy là ảnh sẽ tự động chuyển sang điện thoại.

Khi chưa chắc chắn cách cài đặt, hãy nhấn biểu tượng **ⓘ** cạnh thẻ FTP để xem hướng dẫn minh họa.

📷 Ảnh chụp màn hình: giao diện cài đặt FTP khi mở rộng

## Trong quá trình sử dụng
- Đèn trạng thái: Tắt, Đang chạy · Chờ máy ảnh, Đã kết nối, Đang nhận, Lỗi.
- Thanh thông báo hiện «Đang nhận FTP · Đã nhận N ảnh» kèm tên tệp hiện tại và tốc độ truyền.
- Ảnh được lưu theo đúng quy tắc trong **Cài đặt → Nhận tệp và thông báo** (thư mục, tên tệp, chỉ nhận JPEG, chỉ lưu JPEG từ tệp RAW…), trong lịch sử ghi nguồn là `FTP`.
- Nếu đường truyền bị ngắt giữa chừng hoặc máy ảnh tắt ngang, tệp chưa nhận xong sẽ tự động bị xóa để không để lại tệp lỗi trong thư viện.
- Sau khi tắt máy ảnh khoảng 1 phút, trạng thái sẽ báo chưa kết nối; khi bật máy ảnh kết nối lại, ứng dụng tự tiếp tục nhận.
- **Tự tắt khi nhàn rỗi**: **Cài đặt → Nhận tệp và thông báo → «Tự tắt FTP sau bao lâu không nhận được ảnh»** (Không tự tắt, 5, 10, 30 phút). Đếm từ tấm cuối cùng nhận được, không tắt khi đang truyền dở và có thông báo khi tự tắt.

## Lưu ý quan trọng
- **Phải giữ điểm phát sóng luôn bật**. Một số điện thoại tự tắt điểm phát sóng khi thấy không có lưu lượng Internet, hãy vào cài đặt điểm phát sóng của điện thoại và tắt mục «Tự động tắt điểm phát sóng».
- Sau khi tắt điểm phát sóng rồi bật lại, địa chỉ IP của điện thoại có thể thay đổi, bạn cần đối chiếu lại địa chỉ đã nhập trong máy ảnh.
- Nhận qua FTP và **tự động nhận qua Wi‑Fi chỉ bật được một trong hai**, bật tính năng này thì tính năng kia sẽ tự động dừng.
- Khi đang bật FTP, máy ảnh ở chế độ FTP nên **Thư viện ảnh và Chụp từ xa không thể kết nối qua Wi‑Fi**. Muốn dùng hãy cắm cáp USB, hoặc dừng nhận FTP rồi chuyển máy ảnh lại về «Connect to PC».
- Máy chủ FTP chỉ mở trong mạng cục bộ của điểm phát sóng hoặc Wi‑Fi, tuyệt đối không mở ra ngoài Internet.
- «Kết nối một chạm» không dùng chung được với FTP (kết nối một chạm là máy ảnh tự phát Wi‑Fi, còn FTP yêu cầu máy ảnh kết nối vào mạng của điện thoại).

## Gửi trực tiếp tới NAS
Mục FTP trên máy ảnh cũng có thể cấu hình gửi thẳng tới ổ cứng mạng NAS tại nhà mà không cần qua điện thoại. Đây là tính năng sẵn có của máy ảnh, không cần dùng AeroCam.
