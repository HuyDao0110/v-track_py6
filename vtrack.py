import streamlit as st

# Địa chỉ cơ sở đến thư mục chứa ảnh trên GitHub của bạn (Hãy thay bằng link của bạn)
# Lưu ý: Kết thúc bằng dấu gạch chéo /
GITHUB_IMAGE_BASE = "https://raw.githubusercontent.com/HuyDao0110/#image/main/"

st.set_page_config(page_title="YTrack - GitHub Cloud", layout="wide")

# --- KHỞI TẠO ĐIỀU HƯỚNG ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

# 1. Thanh điều hướng hàng ngang
nav = st.columns([2, 4, 2, 2])

with nav[0]:
    # Tải LOGO trực tiếp từ GitHub
    st.image(GITHUB_IMAGE_BASE + "logo.png", width=110)

with nav[1]:
    st.text_input("Tìm kiếm...", label_visibility="collapsed")

with nav[2]:
    c1, c2 = st.columns(2)
    if c1.button("🏠 Home"):
        st.session_state.page = "Home"
    if c2.button("📚 Thư viện"):
        st.session_state.page = "Thư viện"

with nav[3]:
    c3, c4 = st.columns(2)
    if c3.button("Đăng nhập"):
        st.session_state.page = "Đăng nhập"
    if c4.button("Đăng ký"):
        st.session_state.page = "Đăng ký"

st.write("---")

# --- 2. QUẢN LÝ HIỂN THỊ TRANG ---
if st.session_state.page == "Home":
    st.write("# Nghe gì hôm nay, User?")
    
    # Tải BANNER chính từ GitHub
    st.image(GITHUB_IMAGE_BASE + "best_notification.png", use_container_width=True)

    st.write("## Nghệ sĩ phổ biến")
    art_cols = st.columns(5)
    artists = [
        ("Sơn Tùng M-TP", "A01son_tung.jpg"),
        ("SOOBIN", "A02soobin.jpg"),
        ("bùi trường linh", "A03buitruonglinh.png"),
        ("Trang Pháp", "A04trang_phap.jpg"),
        ("Xem thêm", "A05more.png")
    ]
    for i, (name, img_file) in enumerate(artists):
        with art_cols[i]:
            # Ghép link gốc GitHub với tên file tương ứng
            st.image(GITHUB_IMAGE_BASE + img_file, use_container_width=True)
            if st.button(name, key=f"art_{i}", use_container_width=True):
                if name == "Trang Pháp":
                    st.session_state.page = "Nghệ sĩ"

    st.write("## Album nổi bật")
    alb_cols = st.columns(6)
    albums = [
        "B01mtp_mtp.jpg", "B02ai_cung_phai_bat_dau_tu_dau_do.jpg", 
        "B03danh_doi.jpg", "B04bat_no_len.jpg", 
        "B05tung_ngay_nhu_mai_mai.jpg", "B06more.png"
    ]
    for i, alb in enumerate(albums):
        with alb_cols[i]:
            st.image(GITHUB_IMAGE_BASE + alb, use_container_width=True)

    st.write("## BXH bài hát nổi bật *Tháng này*")
    bxh_l, bxh_r = st.columns([4, 6])
    with bxh_l:
        st.image(GITHUB_IMAGE_BASE + "come_my_way.jpg", use_container_width=True)
            
    with bxh_r:
        songs = [
            ("2", "Em", "Binz"), 
            {"rank": "3", "title": "Nếu như ta chẳng còn", "artist": "RPT MCK"},
            {"rank": "4", "title": "IDK", "artist": "RPT MCK"},
            {"rank": "5", "title": "Nguyễn Văn Mười", "artist": "RPT MCK"},
            {"rank": "6", "title": "người còn thương em không", "artist": "Tóc Tiên"}
        ]
        for s in songs:
            if isinstance(s, tuple):  # Xử lý phần dữ liệu cũ
                rank, title, artist = s
            else:
                rank, title, artist = s["rank"], s["title"], s["artist"]
            sl, sr = st.columns([8, 2])
            sl.write(f"{rank}. {title}")
            sr.write(f"**{artist}**")

elif st.session_state.page == "Nghệ sĩ":
    if st.button("⬅ Quay lại"):
        st.session_state.page = "Home"
    st.write("---")
    l, r = st.columns([4, 6])
    with l:
        st.image(GITHUB_IMAGE_BASE + "trang_phap.jpg", use_container_width=True)
    with r:
        st.write("# Trang Pháp và hành trình")
        st.write("▶ Phát tất cả | 7 bài hát")
        st.write("---")
        for i, s in enumerate(["MOONLIGHT", "Nghệ thuật Gia Vị Đại", "Là Anh", "Ego-holic"], 1):
            st.write(f"{i}. {s}")

elif st.session_state.page == "Thư viện":
    st.image(GITHUB_IMAGE_BASE + "thu_vien_yeu_thich.png", use_container_width=True)
    if st.button("Trở về"):
        st.session_state.page = "Home"

elif st.session_state.page in ["Đăng nhập", "Đăng ký"]:
    if st.button(" Trở về"):
        st.session_state.page = "Home"
    st.write(f"### Trang {st.session_state.page}")
    st.text_input("Username")
    st.text_input("Password", type="password")
    if st.button("Xác nhận"):
        st.session_state.page = "Home"
