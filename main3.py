print("=================== HỆ THỐNG QUẢN LÝ NHÂN SỰ ĐIỆN TỬ ===================\n")

for i in range(1, 4):
    print(f"--- LƯỢT NHẬP LIỆU THỨ {i}/3 ---")
    
    # Tiếp nhận dữ liệu đầu vào từ chuyên viên HR
    employee_id = input("Nhập Mã nhân viên (Ví dụ: NV001, DEV099...): ")
    full_name = input("Nhập Họ và tên nhân viên: ")
    department = input("Nhập Phòng ban công tác (Ví dụ: IT, Marketing...): ")
    
    # XỬ LÝ EDGE CASES (BẪY DỮ LIỆU):
    # .strip() giúp loại bỏ các khoảng trắng thừa. Nếu chuỗi chỉ có khoảng trắng sẽ trở thành chuỗi rỗng.
    if not employee_id.strip() or not full_name.strip():
        print("\n[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        print("-" * 60 + "\n")
        continue  # Bỏ qua quy trình in phiếu bên dưới, chuyển sang người tiếp theo
    
    # HIỂN THỊ KẾT QUẢ (Nếu dữ liệu hợp lệ hoàn toàn)
    # Chuẩn hóa lại dữ liệu hiển thị (loại bỏ khoảng trắng thừa đầu cuối)
    clean_id = employee_id.strip()
    clean_name = full_name.strip()
    clean_dept = department.strip() if department.strip() else "Chưa cập nhật"

    print("\n" + "*" * 22 + " PHIẾU HỒ SƠ ĐIỆN TỬ " + "*" * 22)
    print(f"  |  Mã nhân viên: {clean_id:<37}|")
    print(f"  |  Họ và tên:    {clean_name:<37}|")
    print(f"  |  Phòng ban:    {clean_dept:<37}|")
    print("*" * 65)
    print("-" * 60 + "\n")

# Thông báo sau khi kết thúc vòng lặp kiểm tra đủ 3 người
print("================ HỆ THỐNG ĐÃ HOÀN THÀNH QUÁ TRÌNH XỬ LÝ ================")