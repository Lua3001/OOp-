# ==================== DATABASE (In-memory) ====================
db = {
    "khuvuc": [
        {"MaKV": "KV001", "TenKV": "Tầng 1", "TrangThai": "Hoạt động"},
        {"MaKV": "KV002", "TenKV": "Tầng 2", "TrangThai": "Hoạt động"},
        {"MaKV": "KV003", "TenKV": "Ngoài trời", "TrangThai": "Hoạt động"},
    ],
    "ban": [
        {"MaBan": "B01", "TrangThai": True,  "MaKV": "KV001"},
        {"MaBan": "B02", "TrangThai": False, "MaKV": "KV001"},
        {"MaBan": "B03", "TrangThai": True,  "MaKV": "KV001"},
        {"MaBan": "B04", "TrangThai": False, "MaKV": "KV002"},
        {"MaBan": "B05", "TrangThai": True,  "MaKV": "KV002"},
        {"MaBan": "B06", "TrangThai": True,  "MaKV": "KV003"},
    ],
    "nhomsp": [
        {"MaNhomSP": "NSP001", "TenNhomSP": "Món ăn chính"},
        {"MaNhomSP": "NSP002", "TenNhomSP": "Đồ uống"},
        {"MaNhomSP": "NSP003", "TenNhomSP": "Tráng miệng"},
    ],
    "sanpham": [
        {"MaSP": "SP001", "TenSP": "Phở bò",      "Anh": "🍜", "DVT": "Tô",  "DonGia": 65000, "MaNhomSP": "NSP001"},
        {"MaSP": "SP002", "TenSP": "Bún bò Huế",  "Anh": "🍲", "DVT": "Tô",  "DonGia": 60000, "MaNhomSP": "NSP001"},
        {"MaSP": "SP003", "TenSP": "Cà phê sữa",  "Anh": "☕", "DVT": "Ly",  "DonGia": 30000, "MaNhomSP": "NSP002"},
        {"MaSP": "SP004", "TenSP": "Nước ép cam",  "Anh": "🍊", "DVT": "Ly",  "DonGia": 35000, "MaNhomSP": "NSP002"},
        {"MaSP": "SP005", "TenSP": "Chè ba màu",  "Anh": "🍮", "DVT": "Ly",  "DonGia": 25000, "MaNhomSP": "NSP003"},
    ],
    "nguyenlieu": [
        {"MaNL": "NL001", "TenNL": "Thịt bò",   "DVT": "kg",  "DonGia": 250000, "SL": 20},
        {"MaNL": "NL002", "TenNL": "Bánh phở",  "DVT": "kg",  "DonGia": 30000,  "SL": 50},
        {"MaNL": "NL003", "TenNL": "Rau thơm",  "DVT": "kg",  "DonGia": 15000,  "SL": 10},
    ],
    "nhacungcap": [
        {"MaNCC": "NCC001", "SDT": "0901234567", "TenNCC": "Công ty thực phẩm ABC",   "DiaChi": "123 Lê Lợi",          "CongNo": 0,      "GhiChu": ""},
        {"MaNCC": "NCC002", "SDT": "0912345678", "TenNCC": "Hộ kinh doanh Minh Hà",  "DiaChi": "456 Trần Hưng Đạo",   "CongNo": 500000, "GhiChu": "Thanh toán cuối tháng"},
    ],
    "hoadonnhaphang": [
        {"MaHDNH": "HDNH001", "NgayNhap": "2025-01-15", "MaNV": "NV001", "MaNCC": "NCC001"},
        {"MaHDNH": "HDNH002", "NgayNhap": "2025-01-20", "MaNV": "NV002", "MaNCC": "NCC002"},
    ],
    "chitietnhaphang": [
        {"MaCTNH": "CTNH001", "MaHDNH": "HDNH001", "MaSP": "SP001", "MaNL": "NL001", "SL": 5,  "MaLP": "LP001"},
        {"MaCTNH": "CTNH002", "MaHDNH": "HDNH002", "MaSP": "SP002", "MaNL": "NL002", "SL": 10, "MaLP": "LP001"},
    ],
    "phanquyen": [
        {"MaPQ": "PQ001", "TenQuyen": "Quản lý",    "mucLuong": 12000000, "DVT": "Tháng"},
        {"MaPQ": "PQ002", "TenQuyen": "Thu ngân",   "mucLuong": 7000000,  "DVT": "Tháng"},
        {"MaPQ": "PQ003", "TenQuyen": "Phục vụ",    "mucLuong": 5500000,  "DVT": "Tháng"},
        {"MaPQ": "PQ004", "TenQuyen": "Bếp trưởng", "mucLuong": 10000000, "DVT": "Tháng"},
    ],
    "nhanvien": [
        {"MaNV": "NV001", "Ho": "Nguyễn Văn", "Ten": "An",    "GioiTinh": True,  "SDT": "0901111111", "CCCD": "012345678901", "TrangThai": True,  "TaiKhoan": "admin",    "MatKhau": "123456", "MaQP": "PQ001"},
        {"MaNV": "NV002", "Ho": "Trần Thị",   "Ten": "Bình",  "GioiTinh": False, "SDT": "0902222222", "CCCD": "012345678902", "TrangThai": True,  "TaiKhoan": "binhtran", "MatKhau": "123456", "MaQP": "PQ002"},
        {"MaNV": "NV003", "Ho": "Lê Minh",    "Ten": "Cường", "GioiTinh": True,  "SDT": "0903333333", "CCCD": "012345678903", "TrangThai": True,  "TaiKhoan": "cuongle",  "MatKhau": "123456", "MaQP": "PQ003"},
    ],
    "chamcong": [
        {"MaCC": "CC001", "MaNV": "NV001", "NgayCong": "2025-01-20"},
        {"MaCC": "CC002", "MaNV": "NV002", "NgayCong": "2025-01-20"},
        {"MaCC": "CC003", "MaNV": "NV003", "NgayCong": "2025-01-20"},
    ],
    "hoadonbanhang": [
        {"MaHDBH": "HDB001", "GioVao": "2025-01-20T08:00:00", "GioRa": "2025-01-20T09:30:00", "MaNV": "NV002", "MaBan": "B02"},
        {"MaHDBH": "HDB002", "GioVao": "2025-01-20T10:00:00", "GioRa": "",                    "MaNV": "NV003", "MaBan": "B04"},
    ],
    "chitiethoadon": [
        {"MaCTHD": "CT001", "MaHDBH": "HDB001", "MaSP": "SP001", "SL": 2},
        {"MaCTHD": "CT002", "MaHDBH": "HDB001", "MaSP": "SP003", "SL": 2},
        {"MaCTHD": "CT003", "MaHDBH": "HDB002", "MaSP": "SP002", "SL": 3},
    ],
    "loaiphieu": [
        {"MaLP": "LP001", "TenLP": "Phiếu nhập kho"},
        {"MaLP": "LP002", "TenLP": "Phiếu xuất kho"},
    ],
    "thanhpham": [
        {"MaTP": "TP001", "SL": 10, "NgayXuat": "2025-01-20", "MaSP": "SP001", "MaNL": "NL001"},
    ],
}
 
# ==================== HELPERS ====================
def get_name(table, key_field, key_val, name_field):
    for item in db[table]:
        if item.get(key_field) == key_val:
            return item.get(name_field, key_val)
    return key_val
 
def tinh_tong_hdb(ma_hdb):
    total = 0
    for ct in db["chitiethoadon"]:
        if ct["MaHDBH"] == ma_hdb:
            sp = next((s for s in db["sanpham"] if s["MaSP"] == ct["MaSP"]), None)
            if sp:
                total += sp["DonGia"] * ct["SL"]
    return total
 
def fmt_money(n):
    return f"{n:,.0f}đ".replace(",", ".")
 
# ==================== CONTEXT HELPERS ====================
def get_context():
    """Common context passed to all templates"""
    return {
        "khuvuc_list": db["khuvuc"],
        "nhomsp_list": db["nhomsp"],
        "sanpham_list": db["sanpham"],
        "nhanvien_list": db["nhanvien"],
        "nhacungcap_list": db["nhacungcap"],
        "phanquyen_list": db["phanquyen"],
        "ban_list": db["ban"],
        "hoadonbanhang_list": db["hoadonbanhang"],
        "loaiphieu_list": db["loaiphieu"],
        "get_name": get_name,
        "tinh_tong_hdb": tinh_tong_hdb,
        "fmt_money": fmt_money,
    }
 
# ==================== ROUTES ====================
 
@app.route("/")
def dashboard():
    tong_dt = sum(tinh_tong_hdb(h["MaHDBH"]) for h in db["hoadonbanhang"])
    ban_dang_dung = len([b for b in db["ban"] if not b["TrangThai"]])
    nv_active = len([n for n in db["nhanvien"] if n["TrangThai"]])
    ctx = get_context()
    ctx.update({
        "page": "dashboard",
        "tong_dt": fmt_money(tong_dt),
        "ban_dang_dung": ban_dang_dung,
        "tong_ban": len(db["ban"]),
        "so_sp": len(db["sanpham"]),
        "nv_active": nv_active,
        "recent_hoadon": db["hoadonbanhang"][-5:][::-1],
    })
    return render_template("index.html", **ctx)
 
# --- BAN ---
@app.route("/ban")
def ban():
    kv_filter = request.args.get("kv", "")
    ban_list = db["ban"]
    if kv_filter:
        ban_list = [b for b in ban_list if b["MaKV"] == kv_filter]
    ctx = get_context()
    ctx.update({"page": "ban", "ban_filtered": ban_list, "kv_filter": kv_filter})
    return render_template("index.html", **ctx)
 
@app.route("/ban/toggle/<ma_ban>", methods=["POST"])
def toggle_ban(ma_ban):
    for b in db["ban"]:
        if b["MaBan"] == ma_ban:
            b["TrangThai"] = not b["TrangThai"]
            break
    return redirect(url_for("ban"))
 
@app.route("/ban/add", methods=["POST"])
def add_ban():
    db["ban"].append({
        "MaBan": request.form["MaBan"],
        "TrangThai": request.form.get("TrangThai", "true") == "true",
        "MaKV": request.form["MaKV"],
    })
    return redirect(url_for("ban"))
 
@app.route("/ban/delete/<ma_ban>", methods=["POST"])
def delete_ban(ma_ban):
    db["ban"][:] = [b for b in db["ban"] if b["MaBan"] != ma_ban]
    return redirect(url_for("ban"))
 
# --- KHU VUC ---
@app.route("/khuvuc")
def khuvuc():
    ctx = get_context()
    ctx.update({"page": "khuvuc"})
    return render_template("index.html", **ctx)
 
@app.route("/khuvuc/add", methods=["POST"])
def add_khuvuc():
    db["khuvuc"].append({
        "MaKV": request.form["MaKV"],
        "TenKV": request.form["TenKV"],
        "TrangThai": request.form.get("TrangThai", "Hoạt động"),
    })
    return redirect(url_for("khuvuc"))
 
@app.route("/khuvuc/delete/<ma_kv>", methods=["POST"])
def delete_khuvuc(ma_kv):
    db["khuvuc"][:] = [k for k in db["khuvuc"] if k["MaKV"] != ma_kv]
    return redirect(url_for("khuvuc"))
 
# --- NHOM SP ---
@app.route("/nhomsp")
def nhomsp():
    ctx = get_context()
    ctx.update({"page": "nhomsp"})
    return render_template("index.html", **ctx)
 
@app.route("/nhomsp/add", methods=["POST"])
def add_nhomsp():
    db["nhomsp"].append({
        "MaNhomSP": request.form["MaNhomSP"],
        "TenNhomSP": request.form["TenNhomSP"],
    })
    return redirect(url_for("nhomsp"))
 
@app.route("/nhomsp/delete/<ma>", methods=["POST"])
def delete_nhomsp(ma):
    db["nhomsp"][:] = [n for n in db["nhomsp"] if n["MaNhomSP"] != ma]
    return redirect(url_for("nhomsp"))
 
# --- SAN PHAM ---
@app.route("/sanpham")
def sanpham():
    ctx = get_context()
    ctx.update({"page": "sanpham"})
    return render_template("index.html", **ctx)
 
@app.route("/sanpham/add", methods=["POST"])
def add_sanpham():
    db["sanpham"].append({
        "MaSP": request.form["MaSP"],
        "TenSP": request.form["TenSP"],
        "Anh": "🍽️",
        "DVT": request.form["DVT"],
        "DonGia": int(request.form.get("DonGia", 0)),
        "MaNhomSP": request.form["MaNhomSP"],
    })
    return redirect(url_for("sanpham"))
 
@app.route("/sanpham/delete/<ma>", methods=["POST"])
def delete_sanpham(ma):
    db["sanpham"][:] = [s for s in db["sanpham"] if s["MaSP"] != ma]
    return redirect(url_for("sanpham"))
 
# --- NGUYEN LIEU ---
@app.route("/nguyenlieu")
def nguyenlieu():
    ctx = get_context()
    ctx.update({"page": "nguyenlieu", "nguyenlieu_list": db["nguyenlieu"]})
    return render_template("index.html", **ctx)
 
@app.route("/nguyenlieu/add", methods=["POST"])
def add_nguyenlieu():
    db["nguyenlieu"].append({
        "MaNL": request.form["MaNL"],
        "TenNL": request.form["TenNL"],
        "DVT": request.form["DVT"],
        "DonGia": int(request.form.get("DonGia", 0)),
        "SL": int(request.form.get("SL", 0)),
    })
    return redirect(url_for("nguyenlieu"))
 
@app.route("/nguyenlieu/delete/<ma>", methods=["POST"])
def delete_nguyenlieu(ma):
    db["nguyenlieu"][:] = [n for n in db["nguyenlieu"] if n["MaNL"] != ma]
    return redirect(url_for("nguyenlieu"))
 
# --- NHA CUNG CAP ---
@app.route("/nhacungcap")
def nhacungcap():
    ctx = get_context()
    ctx.update({"page": "nhacungcap"})
    return render_template("index.html", **ctx)
 
@app.route("/nhacungcap/add", methods=["POST"])
def add_nhacungcap():
    db["nhacungcap"].append({
        "MaNCC": request.form["MaNCC"],
        "TenNCC": request.form["TenNCC"],
        "SDT": request.form["SDT"],
        "DiaChi": request.form["DiaChi"],
        "CongNo": int(request.form.get("CongNo", 0)),
        "GhiChu": request.form.get("GhiChu", ""),
    })
    return redirect(url_for("nhacungcap"))
 
@app.route("/nhacungcap/delete/<ma>", methods=["POST"])
def delete_nhacungcap(ma):
    db["nhacungcap"][:] = [n for n in db["nhacungcap"] if n["MaNCC"] != ma]
    return redirect(url_for("nhacungcap"))
 
# --- HOA DON NHAP HANG ---
@app.route("/hoadonnhaphang")
def hoadonnhaphang():
    ctx = get_context()
    ctx.update({"page": "hoadonnhaphang", "hoadonnhaphang_list": db["hoadonnhaphang"]})
    return render_template("index.html", **ctx)
 
@app.route("/hoadonnhaphang/add", methods=["POST"])
def add_hoadonnhaphang():
    db["hoadonnhaphang"].append({
        "MaHDNH": request.form["MaHDNH"],
        "NgayNhap": request.form["NgayNhap"],
        "MaNV": request.form["MaNV"],
        "MaNCC": request.form["MaNCC"],
    })
    return redirect(url_for("hoadonnhaphang"))
 
@app.route("/hoadonnhaphang/delete/<ma>", methods=["POST"])
def delete_hoadonnhaphang(ma):
    db["hoadonnhaphang"][:] = [h for h in db["hoadonnhaphang"] if h["MaHDNH"] != ma]
    return redirect(url_for("hoadonnhaphang"))
 
# --- PHAN QUYEN ---
@app.route("/phanquyen")
def phanquyen():
    ctx = get_context()
    ctx.update({"page": "phanquyen"})
    return render_template("index.html", **ctx)
 
@app.route("/phanquyen/add", methods=["POST"])
def add_phanquyen():
    db["phanquyen"].append({
        "MaPQ": request.form["MaPQ"],
        "TenQuyen": request.form["TenQuyen"],
        "mucLuong": int(request.form.get("mucLuong", 0)),
        "DVT": request.form.get("DVT", "Tháng"),
    })
    return redirect(url_for("phanquyen"))
 
@app.route("/phanquyen/delete/<ma>", methods=["POST"])
def delete_phanquyen(ma):
    db["phanquyen"][:] = [p for p in db["phanquyen"] if p["MaPQ"] != ma]
    return redirect(url_for("phanquyen"))
 
# --- NHAN VIEN ---
@app.route("/nhanvien")
def nhanvien():
    ctx = get_context()
    ctx.update({"page": "nhanvien"})
    return render_template("index.html", **ctx)
 
@app.route("/nhanvien/add", methods=["POST"])
def add_nhanvien():
    db["nhanvien"].append({
        "MaNV": request.form["MaNV"],
        "Ho": request.form["Ho"],
        "Ten": request.form["Ten"],
        "GioiTinh": request.form.get("GioiTinh", "true") == "true",
        "SDT": request.form["SDT"],
        "CCCD": request.form["CCCD"],
        "TrangThai": True,
        "TaiKhoan": request.form["TaiKhoan"],
        "MatKhau": request.form["MatKhau"],
        "MaQP": request.form["MaQP"],
    })
    return redirect(url_for("nhanvien"))
 
@app.route("/nhanvien/delete/<ma>", methods=["POST"])
def delete_nhanvien(ma):
    db["nhanvien"][:] = [n for n in db["nhanvien"] if n["MaNV"] != ma]
    return redirect(url_for("nhanvien"))
 
# --- CHAM CONG ---
@app.route("/chamcong")
def chamcong():
    ctx = get_context()
    ctx.update({"page": "chamcong", "chamcong_list": db["chamcong"]})
    return render_template("index.html", **ctx)
 
@app.route("/chamcong/add", methods=["POST"])
def add_chamcong():
    db["chamcong"].append({
        "MaCC": request.form["MaCC"],
        "MaNV": request.form["MaNV"],
        "NgayCong": request.form["NgayCong"],
    })
    return redirect(url_for("chamcong"))
 
@app.route("/chamcong/delete/<ma>", methods=["POST"])
def delete_chamcong(ma):
    db["chamcong"][:] = [c for c in db["chamcong"] if c["MaCC"] != ma]
    return redirect(url_for("chamcong"))
 
# --- HOA DON BAN HANG ---
@app.route("/hoadonbanhang")
def hoadonbanhang():
    ctx = get_context()
    ctx.update({"page": "hoadonbanhang"})
    return render_template("index.html", **ctx)
 
@app.route("/hoadonbanhang/add", methods=["POST"])
def add_hoadonbanhang():
    ma_ban = request.form["MaBan"]
    db["hoadonbanhang"].append({
        "MaHDBH": request.form["MaHDBH"],
        "GioVao": datetime.now().isoformat(),
        "GioRa": "",
        "MaNV": request.form["MaNV"],
        "MaBan": ma_ban,
    })
    for b in db["ban"]:
        if b["MaBan"] == ma_ban:
            b["TrangThai"] = False
    return redirect(url_for("hoadonbanhang"))
 
@app.route("/hoadonbanhang/checkout/<ma>", methods=["POST"])
def checkout_hoadonbanhang(ma):
    for h in db["hoadonbanhang"]:
        if h["MaHDBH"] == ma:
            h["GioRa"] = datetime.now().isoformat()
            for b in db["ban"]:
                if b["MaBan"] == h["MaBan"]:
                    b["TrangThai"] = True
    return redirect(url_for("hoadonbanhang"))
 
@app.route("/hoadonbanhang/delete/<ma>", methods=["POST"])
def delete_hoadonbanhang(ma):
    db["hoadonbanhang"][:] = [h for h in db["hoadonbanhang"] if h["MaHDBH"] != ma]
    return redirect(url_for("hoadonbanhang"))
 
# --- CHI TIET HOA DON ---
@app.route("/chitiethoadon")
def chitiethoadon():
    ctx = get_context()
    ctx.update({"page": "chitiethoadon", "chitiethoadon_list": db["chitiethoadon"],
                "tinh_thanh_tien": lambda ma_sp, sl: next(
                    (s["DonGia"] * sl for s in db["sanpham"] if s["MaSP"] == ma_sp), 0)})
    return render_template("index.html", **ctx)
 
@app.route("/chitiethoadon/add", methods=["POST"])
def add_chitiethoadon():
    db["chitiethoadon"].append({
        "MaCTHD": request.form["MaCTHD"],
        "MaHDBH": request.form["MaHDBH"],
        "MaSP": request.form["MaSP"],
        "SL": int(request.form.get("SL", 1)),
    })
    return redirect(url_for("chitiethoadon"))
 
@app.route("/chitiethoadon/delete/<ma>", methods=["POST"])
def delete_chitiethoadon(ma):
    db["chitiethoadon"][:] = [c for c in db["chitiethoadon"] if c["MaCTHD"] != ma]
    return redirect(url_for("chitiethoadon"))
 
# --- LOAI PHIEU ---
@app.route("/loaiphieu")
def loaiphieu():
    ctx = get_context()
    ctx.update({"page": "loaiphieu"})
    return render_template("index.html", **ctx)
 
@app.route("/loaiphieu/add", methods=["POST"])
def add_loaiphieu():
    db["loaiphieu"].append({
        "MaLP": request.form["MaLP"],
        "TenLP": request.form["TenLP"],
    })
    return redirect(url_for("loaiphieu"))
 
@app.route("/loaiphieu/delete/<ma>", methods=["POST"])
def delete_loaiphieu(ma):
    db["loaiphieu"][:] = [l for l in db["loaiphieu"] if l["MaLP"] != ma]
    return redirect(url_for("loaiphieu"))
 
if __name__ == "__main__":
    app.run(debug=True, port=5000)
