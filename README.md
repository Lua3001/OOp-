                                                     Hệ thống quản lý quán coffee
                            Theo dõi bàn, hóa đơn bán hàng, chi tiết bán hàng, nhân viên chấm công , nhà cung cấp

🌟	Điểm Mạnh & Tính Năng Nổi Bật: 
1. Kiến trúc tổng thể rất gọn gàng: một SPA hoàn chỉnh không cần framework, không cần server — chỉ một file HTML duy nhất chạy được ngay trên trình duyệt. Điều này cực kỳ dễ triển khai và chia sẻ.
2. Object db trung tâm là điểm thiết kế thông minh nhất: toàn bộ 11 bảng dữ liệu (bàn, hóa đơn, nhân viên...) đều nằm trong một object duy nhất, dễ đọc, dễ debug, và các hàm helper như getNV(), getSP(), tinhTongHDB() truy vấn rất hiệu quả.
3. Reactive render không cần virtual DOM: sau mỗi thao tác (thêm/xóa/sửa), hệ thống gọi lại hàm renderXxx() tương ứng để cập nhật giao diện — đơn giản nhưng hiệu quả tốt cho quy mô nhà hàng.

🏗️ Tư Duy Lập Trình Hướng Đối Tượng (OOP)
Dự án ứng dụng triệt để 4 tính chất của OOP để tạo ra một Framework dễ mở rộng:
1. Tính trừu tượng (Abstraction) : Các hàm helper như getNV(), getSP(), tinhTongHDB() ẩn đi logic phức tạp, người gọi không cần biết bên trong làm gì — đây là abstraction tốt.
2. Tính đóng gói (Encapsulation) : Object db gom toàn bộ dữ liệu vào một chỗ, các hàm save*() và render*() đóng vai trò method — nhưng chúng chưa được gắn trực tiếp vào object, đây là hạn chế lớn nhất.
3. Tính đa hình và tính kế thừa (Inheritance & Polymorphism): Gần như vắng mặt hoàn toàn. Mỗi module (bàn, nhân viên, sản phẩm...) có bộ hàm riêng lặp lại cùng cấu trúc, thay vì kế thừa từ một lớp cha chung.

Sơ đồ lớp (Class Diagram) 

<img width="881" height="732" alt="701888844_27183896301233924_3285500143628248412_n (1)" src="https://github.com/user-attachments/assets/9c525b71-30a1-4db3-b6ba-e63b4bef8aef" />

🔄 Luồng Dữ Liệu (Data Flow Activity)

Làn 1 — Quản lý bàn: Hệ thống kiểm tra TrangThai trước khi cho phép ngồi. Nếu bàn đang bận, vòng lặp buộc chọn lại. Khi xác nhận, toggleBan() lật cờ false (đang phục vụ).

Làn 2 — Tạo hóa đơn: saveHDB() ghi nhận thời điểm GioVao, gắn MaNV (nhân viên phụ trách) và MaBan — tạo khóa ngoại liên kết hai chiều.

Làn 3 — Ghi chi tiết: Đây là vòng lặp cốt lõi — khách có thể gọi nhiều món. Mỗi lần saveCTBH() tạo một bản ghi ChiTietHoaDon mới với MaHDBH làm khóa ngoại.

Làn 4 — Thanh toán: tinhTongHDB() cộng toàn bộ SL × DonGia của các chi tiết. Sau khi ghi GioRa, bàn tự động được giải phóng (TrangThai = true).

Làn 5 — Dashboard phản ứng: Ba điểm trong luồng đều kích hoạt cập nhật dashboard song song — doanh thu, badge đếm bàn, và danh sách hóa đơn gần đây — thể hiện cơ chế reactive đơn giản nhưng hiệu quả của hệ thống.

🛠️ Hướng dẫn sử dụng: 

Bước 1: Truy cập vào:
https://github.com/Lua3001/OOp-/blob/main/code%20httml?fbclid=IwY2xjawSCPHVleHRuA2FlbQIxMABicmlkETFOcmhEVEo2cjIwM1RDVTVnc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHkxLDCVI0BYGLBdOYIllgPqvKPyAH0d9W2f-9RJK5tpqdd6NGS16pdVbUH-g_aem_cwO_ZuQq1jSKWrrHtxCuPQ

Bước 2: Copy phần code.

Bước 3: Truy cập đường link: 
https://onecompiler.com/html?fbclid=IwY2xjawSCPP5leHRuA2FlbQIxMABicmlkETFOcmhEVEo2cjIwM1RDVTVnc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHkxLDCVI0BYGLBdOYIllgPqvKPyAH0d9W2f-9RJK5tpqdd6NGS16pdVbUH-g_aem_cwO_ZuQq1jSKWrrHtxCuPQ

Bước 4: Paste phần code đã copy ở bước 2 bào đường link bước 3 và khởi chạy (Run).

Bước 5: Sử dụng.






