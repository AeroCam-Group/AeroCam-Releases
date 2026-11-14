<!-- translated from zh-TW at commit 968641f -->

# 3. Tự động nhận và lưu tệp

## Bảng điều khiển máy ảnh
Sau khi kết nối máy ảnh, phần trên cùng của Trang chủ sẽ hiển thị trạng thái hiện tại của máy ảnh:

| Mục | Nội dung |
|---|---|
| Dòng máy, ống kính | Ví dụ «Nikon Z f», «NIKKOR Z 24–120 mm f/4» |
| Pin | Phần trăm pin (chuyển đỏ khi từ 20% trở xuống) |
| Phương thức kết nối | Điểm phát sóng di động, Cùng mạng Wi‑Fi, Wi‑Fi máy ảnh, USB |
| Thẻ nhớ | Dung lượng đã dùng / tổng dung lượng và số ảnh còn chụp được của từng thẻ; khe thẻ kép hiển thị tách biệt |
| Chất lượng ảnh | Ví dụ `RAW`, `JPEG fine★ L`; tự động cập nhật khi bạn đổi chất lượng trên máy ảnh hoặc tháo lắp thẻ |
| Nơi lưu tệp | Ví dụ «Lưu vào: thẻ nhớ ✓», xem thêm mục [Nơi lưu tệp và chụp không cần thẻ nhớ](#nơi-lưu-tệp-và-chụp-không-cần-thẻ-nhớ) bên dưới |
| Truyền tệp | Trạng thái hiện tại, góc trên bên phải có nút «Lịch sử ›» |
| Phong cách máy ảnh | Các thiết lập C1–C9 đọc được lần gần nhất, xem [Chương 6](06-edit.md#phong-cách-máy-ảnh-c1c9-pro) |

Những thông số mà máy ảnh không cung cấp ở chế độ hiện tại sẽ được ẩn đi. Khi chuyển sang «Camera control» và vào giao diện Chụp từ xa, ứng dụng thường đọc được nhiều thông số hơn.

### Quản lý máy ảnh
Mở rộng mục **Quản lý máy ảnh (n)** bên dưới bảng điều khiển để chỉnh sửa, xóa hoặc thêm máy ảnh. Trang «Chi tiết» của mỗi máy ảnh hiển thị:
- Tên dòng máy, số sê-ri (che các số ở giữa, nhấn vào để xem đầy đủ), phiên bản phần mềm (firmware), **số lần chụp (shutter count)** và ngày đọc dữ liệu.
- **Số lần chụp hằng tháng**: biểu đồ cột 6 tháng gần nhất (có dữ liệu tính từ lúc bắt đầu ghi nhận).
- Thời gian kết nối lần cuối, phương thức, ống kính, mức pin và dung lượng trống trên thẻ nhớ.
- Số tệp đã chuyển sang điện thoại, ngày kết nối đầu tiên và cấu hình mạng đã lưu.

Số lần chụp được đọc từ thông tin của bức ảnh mới nhất trên thẻ nhớ, vì vậy thẻ nhớ cần có ít nhất một bức ảnh.

### Cảnh báo pin yếu
Gửi thông báo khi pin máy ảnh giảm xuống ngưỡng cài đặt (mặc định 15%); chỉ nhắc lại sau khi pin đã sạc lên cao hơn ngưỡng ít nhất +5%. Bạn có thể chỉnh ngưỡng hoặc tắt trong **Cài đặt → Nhận tệp và thông báo**.

📷 Ảnh chụp màn hình: Bảng điều khiển máy ảnh

---

## Tự động nhận (Pro)
1. Trang chủ Wi‑Fi → **Bắt đầu nhận**. Ứng dụng sẽ duy trì kết nối ngầm với máy ảnh (hiển thị trên thanh thông báo).
2. Khi xem lại ảnh trên máy ảnh, nhấn **i → Send to PC / Select to send** (Gửi đến máy tính / Chọn để gửi, tên menu tùy dòng máy), ảnh sẽ được truyền ngay sang điện thoại.

Nếu muốn chụp xong là ảnh tự đẩy ngay sang điện thoại, hãy dùng [Nhận ảnh qua FTP](08-ftp.md). Khi đang cắm cáp USB, việc nhận ảnh sẽ tự động chuyển sang dùng USB.

### Tạm dừng nhận
Khi đang bật tự động nhận qua Wi‑Fi, nhấn **⏸ Tạm dừng** ở góc trên bên phải ô «Truyền tệp» hoặc nút «Tạm dừng» trên thông báo để tạm dừng:
- Wi‑Fi vẫn giữ kết nối nên Thư viện ảnh và Chụp từ xa vẫn dùng bình thường.
- Các ảnh chờ gửi sẽ nằm lại trên máy ảnh; khi nhấn **Tiếp tục nhận**, ứng dụng sẽ nhận bù theo đúng thứ tự. Ảnh đang truyền dở sẽ được truyền xong trước.
- Chế độ tạm dừng tự động hủy khi bạn nhấn «Tiếp tục», dừng nhận, vuốt tắt ứng dụng khỏi danh sách đa nhiệm, mất Wi‑Fi, tắt máy ảnh hoặc cắm cáp USB.

### Khi bị mất kết nối
- Mất kết nối ứng dụng sẽ tự động kết nối lại; nếu thử lại vài lần không được, ứng dụng sẽ tìm lại bằng mã định danh máy ảnh nên dù máy ảnh đổi IP vẫn tìm thấy.
- **Máy ảnh chuyển sang gửi ảnh qua Bluetooth**: máy ảnh chỉ có một chip không dây nên khi gửi qua Bluetooth sẽ tạm tắt Wi‑Fi. Lúc này Trang chủ hiện «Máy ảnh đang gửi ảnh qua Bluetooth… Gửi xong sẽ tự kết nối lại Wi‑Fi» và không tính là lỗi ngắt kết nối.
- **Thư viện / Chụp từ xa mượn kết nối máy ảnh**: tại một thời điểm máy ảnh chỉ nhận một kết nối. Khi bạn vào Thư viện hoặc Chụp từ xa, tính năng tự động nhận sẽ tạm nhường kết nối và tự khôi phục sau khi bạn thoát ra.
- **Khi không tìm thấy máy ảnh qua Wi‑Fi**: quá thời gian cài đặt (mặc định 3 phút), ứng dụng tự dừng nhận và gửi thông báo để tránh hao pin. Thời gian này chỉnh tại **Cài đặt → Nhận tệp và thông báo**.

---

## Quy tắc nhận tệp
Chỉnh tại **Cài đặt → Nhận tệp và thông báo**, áp dụng chung cho cả Wi‑Fi, USB và FTP.

### Loại tệp nhận về
Chọn loại tệp muốn lưu: Tất cả tệp, Chỉ JPG, JPG + RAW, Ảnh + video, hoặc Tùy chỉnh (JPEG, RAW, HEIF, TIFF, Video, Khác).

Kèm ba công tắc mở rộng (Pro):

| Công tắc | Giải thích |
|---|---|
| **Chỉ lưu JPEG từ tệp RAW** | Khi nhận tệp RAW, chỉ trích xuất ảnh JPEG kích thước đầy đủ nhúng sẵn bên trong (thường 2–5 MB thay vì tệp RAW 20–50 MB), giữ nguyên độ phân giải và đầy đủ thông số chụp, lưu dưới dạng `DSC_1234_S.JPG`. Rất tiện để đăng mạng xã hội hoặc xem nhanh hằng ngày |
| **Lưu bản JPEG nén** | Khi nhận ảnh JPEG từ máy ảnh, điện thoại sẽ nén lại rồi lưu (`_S.JPG`, giữ nguyên kích thước điểm ảnh, chất lượng theo cài đặt thư viện) |
| **Thay thế bản nén khi nhận được ảnh gốc** | Khi lưu tệp JPEG gốc, tự động xóa bản nén của cùng bức ảnh đó trên điện thoại |

> Để nhận được tệp RAW, chất lượng ảnh trên máy ảnh phải đặt là RAW hoặc RAW+JPEG, đồng thời trong tùy chọn tải lên của mục «Connect to PC» trên máy ảnh phải chọn RAW+JPEG (không chọn «JPEG only»). Tên menu cụ thể tùy thuộc từng dòng máy.

### Các quy tắc khác
| Quy tắc | Giải thích |
|---|---|
| Chế độ nhận | Nhận liên tục, hoặc nhận xong một tệp thì dừng |
| Video dung lượng lớn | Video vượt ngưỡng (mặc định 1024 MB) không tự động nhận mà ghi là «Đã lọc», cần tải thủ công |
| Thư mục lưu | Theo máy ảnh, Theo ngày, Theo máy ảnh và ngày, Theo loại tệp |
| Tên tệp | Tên gốc từ máy ảnh (`DSC_1234.NEF`), thêm tiền tố ngày (`20261011_DSC_1234.NEF`), thêm tiền tố ngày giờ (`20261011_153012_DSC_1234.NEF`, giúp sắp xếp ảnh từ nhiều máy ảnh theo đúng thời gian chụp). Chỉ áp dụng cho các tệp lưu sau khi đổi cài đặt |

### Vị trí lưu trữ
- Ảnh: `Pictures/AeroCam/…`
- Video: `Movies/AeroCam/…`
- Tệp khác: `Download/AeroCam/…`

Các ứng dụng khác như Google Photos đều nhìn thấy ngay. Sau khi gỡ rồi cài lại ứng dụng, bạn có thể dùng **Cài đặt → Bộ nhớ và pin → «Quét lại ảnh trên điện thoại»** để đưa các ảnh cũ trở lại thư viện.

### Nhận diện tệp trùng lặp
- Kiểm tra dựa trên số sê-ri máy ảnh, tên tệp, dung lượng, thời gian chụp và nội dung tệp; tệp trùng sẽ không lưu lại và được ghi chú «Trùng lặp» trong lịch sử.
- Nếu bạn đã xóa ảnh trên điện thoại (kể cả đưa vào thùng rác), khi gửi lại từ máy ảnh ứng dụng sẽ lưu lại.
- Gửi lại cùng một ảnh không cần phải dừng rồi bắt đầu nhận lại.

### Khi nhận cùng một ảnh qua cả Bluetooth và Wi‑Fi
Tệp qua Wi‑Fi đầy đủ hơn (kích thước gốc), nên ưu tiên theo bản Wi‑Fi:
- Nhận qua Wi‑Fi trước, sau đó Bluetooth gửi lại: bỏ qua bản Bluetooth.
- Nhận qua Bluetooth trước, sau đó Wi‑Fi nhận cùng ảnh đó, xử lý theo **Cài đặt → Nhận tệp và thông báo → «Ảnh đã nhận qua Bluetooth»**:
  - **Thay bằng ảnh gốc khi nhận qua Wi‑Fi** (khuyên dùng): lưu bản kích thước đầy đủ và tự xóa bản thu nhỏ Bluetooth trên điện thoại.
  - **Không tải lại qua Wi‑Fi**.
  - **Giữ cả hai bản**.
- Tệp RAW gốc luôn được nhận đầy đủ.

---

## Nơi lưu tệp và chụp không cần thẻ nhớ
Quyết định ảnh sẽ lưu vào đâu sau khi bấm nút chụp. Ứng dụng tự đọc trạng thái lắp thẻ của máy ảnh để chọn:
- **Máy ảnh có thẻ nhớ**: làm theo lựa chọn tại **Cài đặt → Chụp ảnh → Nơi lưu tệp**:
  - **Thẻ nhớ**: lưu trên thẻ nhớ của máy ảnh.
  - **Thẻ nhớ + điện thoại** (Pro): lưu vào thẻ nhớ đồng thời chép thêm một bản sang điện thoại.
- **Máy ảnh không lắp thẻ nhớ** (Pro): tự động chuyển sang **Chỉ lưu điện thoại (chụp không thẻ)**. Bạn vẫn bấm nút chụp bình thường và ảnh truyền thẳng về điện thoại, đặt tên theo thời gian chụp (ví dụ `AC_20261025_193805.JPG`). Khi lắp thẻ lại sẽ tự động quay về chế độ cũ.

Dùng được ở Trang chủ, Thư viện và Chụp từ xa, hỗ trợ cả Wi‑Fi lẫn USB.

**Cần thiết lập trước cho lần đầu:**
1. Trong menu Cài đặt tùy chỉnh (Custom Settings) của máy ảnh, đổi mục **Slot empty release lock** (Khóa nhả màn trập khi trống khe thẻ) thành **Enable release** (Cho phép nhả màn trập), nếu không máy ảnh sẽ khóa nút chụp khi không có thẻ.
2. Khi kết nối Wi‑Fi, loại kết nối (Connection type) của máy ảnh phải để **Camera control**. Nếu đang ở «Image transfer», khoảng 3 giây sau tấm đầu tiên ứng dụng sẽ nhắc bạn chuyển đổi; ảnh vẫn nằm trong bộ nhớ đệm máy ảnh và tự động truyền sang sau khi bạn chuyển. Kết nối USB không gặp hạn chế này.
3. Kết nối một chạm không hỗ trợ chụp không thẻ nhớ, vui lòng chuyển sang dùng điểm phát sóng di động hoặc cùng mạng Wi‑Fi.

**Cách đọc thanh trạng thái** (phía trên Trang chủ và Cuộn camera):

| Hiển thị | Ý nghĩa |
|---|---|
| Lưu vào: thẻ nhớ ✓ | Lưu vào thẻ nhớ trên máy ảnh |
| Lưu vào: thẻ nhớ + điện thoại ✓ | Lưu vào thẻ nhớ và chép thêm sang điện thoại |
| Lưu vào: chỉ điện thoại (máy ảnh không có thẻ nhớ) | Ảnh truyền trực tiếp về điện thoại |
| Máy ảnh đang ở chế độ «Image transfer»… (chữ đỏ) | Vui lòng chuyển sang «Camera control» |
| Wi‑Fi một chạm: không có thẻ nhớ, không thể chụp (chữ đỏ) | Hãy lắp thẻ nhớ, hoặc đổi sang điểm phát sóng / cùng Wi‑Fi |
| Thẻ nhớ đã đầy (chữ đỏ) | Hãy thay thẻ hoặc giải phóng dung lượng (không tự chuyển sang chỉ lưu điện thoại) |
| Máy ảnh không có thẻ nhớ, không thể chụp (chữ đỏ) | Đang ở bản miễn phí, hoặc điện thoại còn dưới 1 GB trống |

> Khi không lắp thẻ nhớ, máy ảnh không thể quay video và tốc độ chụp liên tiếp sẽ chậm hơn (mỗi tấm phải chờ truyền xong sang điện thoại).

---

## Vị trí ảnh (GPS)
**Cài đặt → Nhận tệp và thông báo → Vị trí ảnh** có hai công tắc:
- **Gửi vị trí cho máy ảnh (Bluetooth)** (mặc định bật): khi bật máy ảnh hoặc truyền ảnh qua Bluetooth, điện thoại gửi tọa độ vị trí sang máy ảnh để máy tự ghi vào ảnh lúc chụp.
- **Bổ sung vị trí cho ảnh JPEG nhận về (điện thoại)**: các ảnh JPEG nhận qua Wi‑Fi, USB, FTP, tải từ thư viện hoặc chụp từ xa sẽ được điện thoại đối chiếu theo giờ chụp để ghi tọa độ lúc đó. Lần đầu bắt đầu nhận sẽ hỏi xác nhận một lần.
  - Tệp RAW không bị chỉnh sửa; ảnh đã có sẵn tọa độ sẽ giữ nguyên tọa độ gốc.
  - Dữ liệu vị trí điện thoại ghi lại trong lúc nhận chỉ lưu cục bộ trên máy này và tự xóa sau 24 giờ.
  - Nếu giờ chụp không khớp với mốc thời gian nào thì không ghi, thà để trống còn hơn ghi sai vị trí.
  - Cần bắt đầu nhận khi đang mở AeroCam thì mới ghi nhận được vị trí.

> Tọa độ chụp được lưu trong ảnh sẽ đi kèm tệp gốc khi chia sẻ. Khi chia sẻ bằng mã QR, mặc định ứng dụng sẽ xóa thông tin vị trí — xem [Chương 4](04-gallery.md#chia-sẻ-qua-mã-qr).

---

## Lịch sử
Góc trên bên phải ô «Truyền tệp» ở Trang chủ có nút **Lịch sử ›**, liệt kê toàn bộ kết quả nhận tự động, tải từ thư viện và lưu khi chụp từ xa: thành công, trùng lặp, đã bỏ qua, thất bại, mỗi mục đều có ảnh thu nhỏ.
- Nhấn vào để xem toàn màn hình ngay trong ứng dụng.
- Có thể tìm kiếm, lọc theo máy ảnh hoặc xóa lịch sử. Xóa lịch sử không làm mất tệp ảnh trên điện thoại.
